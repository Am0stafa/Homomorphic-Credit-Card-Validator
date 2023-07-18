# Luhn's Algorithm and Homomorphic Encryption

This project demonstrates the use of Luhn's Algorithm and homomorphic encryption to validate credit card numbers without revealing the actual credit card number. Luhn's Algorithm is a checksum formula used to validate identification numbers, such as credit card numbers. Homomorphic encryption is a form of encryption that allows computations to be performed on encrypted data without decrypting it first.
For This project, I used the Pyfhel library for homomorphic encryption.
The Pyfhel library uses the Paillier homomorphic encryption scheme to encrypt data. Paillier encryption is a probabilistic asymmetric encryption algorithm that allows for the homomorphic addition of ciphertexts.
Also, it uses a partially homomorphic encryption scheme, which supports homomorphic addition of ciphertexts but not homomorphic multiplication.
## Luhn's Algorithm

Luhn's Algorithm works by summing up the digits of an identification number and performing some mathematical operations on them to determine if the number is valid or not. For credit card numbers, the algorithm is used to check if the number is valid and to detect any errors in the number. The algorithm is widely used in the banking and finance industry to validate credit card numbers.

## Homomorphic Encryption
Homomorphic encryption is a form of encryption that allows computations to be carried out on ciphertext, thus generating an encrypted result which, when decrypted, matches the result of the operations as if they had been performed on the plaintext. This allows data to be encrypted while still allowing operations and computations to be performed without accessing the decrypted data.


## Usage

To use this project, simply run the `credit_card_validator.py` script and enter a credit card number when prompted. The script will encrypt the credit card number using homomorphic encryption and perform Luhn's Algorithm on the encrypted data to validate the credit card number. The script will then output whether the credit card number is valid or not.

## Dependencies

This project requires the Pyfhel library for homomorphic encryption. Pyfhel can be installed using pip:

```bash
pip install Pyfhel
```

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments

This project was inspired by the work of Hans Peter Luhn and the field of homomorphic encryption.
