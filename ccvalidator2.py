from Pyfhel import Pyfhel, PyPtxt, PyCtxt
import numpy as np

# Initialize Pyfhel object
HE = Pyfhel()
# Key generation with large coefficient modulus for more complex computations
HE.contextGen(p=65537, m=8192, flagBatching=True)  # Enable batching
HE.keyGen()
HE.relinKeyGen()
HE.rotateKeyGen()

def encrypt_card_number(card_number):
    # Convert the credit card number to a list of integers
    cc_digits = [int(d) for d in card_number]
    # Encrypt the number as a whole, assuming batching is enabled
    plaintext = PyPtxt(cc_digits, HE)
    return HE.encrypt(plaintext)

def luhns_algorithm(HE, encrypted_number):
    # Decrypt the encrypted number for Luhn's Algorithm
    decrypted_number = HE.decrypt(encrypted_number)
    cc_digits = [int(d) for d in str(decrypted_number)]
    cc_digits.reverse()
    for i in range(len(cc_digits)):
        if i % 2 == 1:
            cc_digits[i] *= 2
            if cc_digits[i] > 9:
                cc_digits[i] -= 9
    return sum(cc_digits) % 10 == 0

def main():
    card_number = input("Enter your credit card number: ")
    encrypted_number = encrypt_card_number(card_number)

    # Output the encrypted number and keys
    print("Encrypted credit card number:", encrypted_number.to_bytes().hex())
    print("Public key:", HE.getpublicKey().to_bytes().hex())
    print("Secret key:", HE.getsecretKey().to_bytes().hex())
    print("Relin key:", HE.getrelinKey().to_bytes().hex())
    print("Rotate key:", HE.getrotateKey().to_bytes().hex())

    # Perform Luhn's Algorithm on the encrypted number
    is_valid = luhns_algorithm(HE, encrypted_number)
    print("The credit card number is valid!" if is_valid else "The credit card number is invalid.")

if __name__ == "__main__":
    main()