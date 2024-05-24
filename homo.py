from concrete import fhe
import numpy as np

# Define the FHE-compatible Luhn algorithm function
@fhe.compiler({"x": "encrypted"})
def luhn_algorithm(x):
    n_digits = x.shape[0]
    sum_digits = 0
    for i in range(n_digits):
        digit = x[n_digits - 1 - i]
        if i % 2 == 1:
            doubled_digit = digit * 2
            correction = (doubled_digit > 9) * 9
            sum_digits += doubled_digit - correction
        else:
            sum_digits += digit
    return sum_digits % 10 == 0

# Test cases
test_cases = {
    "4532015112830366": True,
    "6011514433546201": True,
    "4485275742308327": True,
    "4532015112830365": False,
    "6011514433546200": False,
    "4485275742308326": False,
}

# Prepare the input set for the function
inputset = [np.array([int(digit) for digit in number], dtype=np.uint8) for number in test_cases.keys()]
circuit = luhn_algorithm.compile(inputset)

# Save and load the server
circuit.server.save("server.zip")
server = fhe.Server.load("server.zip")

# Serialize and deserialize client specs
serialized_client_specs = server.client_specs.serialize()
client_specs = fhe.ClientSpecs.deserialize(serialized_client_specs)

# Create the client with the deserialized specs
client = fhe.Client(client_specs)

# Generate the keys
client.keys.generate()

# Serialize the evaluation keys
serialized_evaluation_keys = client.evaluation_keys.serialize()

def test_luhn_algorithm():
    passed = 0
    failed = 0

    for number, expected in test_cases.items():
        # Encrypt the credit card number
        encrypted_credit_card_number = client.encrypt(np.array([int(digit) for digit in number], dtype=np.uint8))
        
        # Serialize the argument
        serialized_arg = encrypted_credit_card_number.serialize()
        
        # Deserialize the argument on the server
        deserialized_arg = fhe.Value.deserialize(serialized_arg)
        
        # Deserialize the evaluation keys on the server
        deserialized_evaluation_keys = fhe.EvaluationKeys.deserialize(serialized_evaluation_keys)
        
        # Perform computation on the server
        result = server.run(deserialized_arg, evaluation_keys=deserialized_evaluation_keys)
        
        # Decrypt the result
        is_valid = client.decrypt(result)
        
        # Print the result
        result_status = "passed" if is_valid == expected else "failed"
        print(f"Credit card number {number} is {'valid' if is_valid else 'invalid'} (Expected: {'valid' if expected else 'invalid'}) - Test {result_status}")
        
        # Update statistics
        if is_valid == expected:
            passed += 1
        else:
            failed += 1
    
    # Print statistics
    print(f"\nTest Summary: {passed} passed, {failed} failed")

# Run the tests
test_luhn_algorithm()