from Pyfhel import Pyfhel, PyPtxt, PyCtxt

# Initialize and generate keys
HE = Pyfhel()
HE.keyGen()

cc_number = input("Enter your credit card number: ")

print("Your public key is: " + str(HE.pubKey))
print("Your secret key is: " + str(HE.secKey))
print("Your relin key is: " + str(HE.relinKey))
print("Your galois key is: " + str(HE.galoisKey))
print("Your key switch matrix is: " + str(HE.keySwitchMatrix))


# Convert the credit card number to a list of integers
cc_digits = [int(d) for d in cc_number]
# Create a plaintext object from the credit card digits
cc_ptxt = PyPtxt(cc_digits)

# Encrypt the plaintext object
cc_enc = HE.encrypt(cc_ptxt)

# Perform Luhn's Algorithm on the encrypted data
# it is done by reversing the list and multiplying every other digit by 2 then subtracting 9 to numbers over 9 
cc_enc_list = cc_enc.toList()
cc_enc_list.reverse()
for i in range(len(cc_enc_list)):
    if i % 2 == 1:
        cc_enc_list[i] *= 2
        if cc_enc_list[i] > 9:
            cc_enc_list[i] -= 9
cc_enc_sum = sum(cc_enc_list)

# Decrypt the result and check if its valid
cc_sum = HE.decrypt(cc_enc_sum)
if cc_sum % 10 == 0:
    print("Credit card number is valid!")
else:
    print("Credit card number is invalid.")