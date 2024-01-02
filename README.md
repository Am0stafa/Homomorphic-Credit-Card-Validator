# Luhn's Algorithm and Homomorphic Encryption

## Homomorphic Encryption

Homomorphic Encryption (HE) is a form of encryption that allows computations to be carried out on ciphertexts, generating an encrypted result that, when decrypted, matches the result of operations performed on the plaintexts. This type of encryption enables the processing of encrypted data without giving access to the unencrypted data, ensuring the privacy and security of the data even while it's being used.

## BFV (Brakerski/Fan-Vercauteren) Scheme

The BFV scheme is a popular homomorphic encryption scheme that supports both addition and multiplication on encrypted integers. It is based on the Ring Learning With Errors (RLWE) problem and provides a balance between efficiency and security, making it suitable for a wide range of applications.

## CKKS (Cheon-Kim-Kim-Song) Scheme

The CKKS scheme is another HE scheme that allows approximate arithmetic on encrypted real or complex numbers. It is particularly useful for applications that require operations on fractional numbers and can tolerate slight approximation errors, such as machine learning and statistical analysis.

## Luhn's Algorithm

Luhn's Algorithm, also known as the "modulus 10" or "mod 10" algorithm, is a simple checksum formula used to validate a variety of identification numbers, most notably credit card numbers. The algorithm is designed to protect against accidental errors, such as a mistyped digit, but not malicious attacks.

## Steps of Luhn's Algorithm:
  1. Starting from the rightmost digit (the check digit) and moving left, double the value of every second digit. If the result of this doubling is greater than 9, then add the digits of the product (e.g., 16: 1 + 6 = 7, 18: 1 + 8 = 9) or subtract 9 from the product.
  2. Take the sum of all the digits.
  3. If the total modulo 10 is equal to 0, then the number is valid according to the Luhn formula; otherwise, it is not valid.

## Pyfhel: Python For Homomorphic Encryption Libraries

Pyfhel is a Python library that acts as a wrapper for several HE libraries, providing a Pythonic interface to perform HE operations. It simplifies the process of working with HE schemes like BFV and CKKS, abstracting away the complex underlying mathematics and allowing users to perform encrypted computations with syntax similar to regular arithmetic operations.

## Project Overview

This project demonstrates the use of Pyfhel to implement Luhn's Algorithm on encrypted credit card numbers. The goal is to validate credit card numbers without revealing or accessing the actual number in plaintext, thus preserving the privacy of sensitive data.

## Limitations and Workarounds

### Homomorphic Encryption Limitations

Homomorphic Encryption (HE) allows computations on encrypted data, enabling the development of privacy-preserving applications. However, it comes with several limitations:

1. **Computational Intensity**: HE operations are significantly more resource-intensive than their plaintext counterparts. This can lead to performance bottlenecks, especially when dealing with complex algorithms or large datasets.

   **Workaround**: Optimize algorithms to minimize the number of HE operations, use more powerful computing resources, or apply techniques like multi-threading and distributed computing.

2. **Lack of Native Conditional Logic**: HE does not support conditional operations like if-else statements or loops that depend on the encrypted data.

   **Workaround**: Convert conditional logic into equivalent arithmetic operations that HE can perform. For example, use multiplexer logic or threshold functions to simulate conditions.

3. **Noise Growth**: Each operation on ciphertexts introduces noise. If the noise grows beyond a certain threshold, it can lead to decryption errors.

   **Workaround**: Use relinearization and modulus switching techniques to manage noise growth. In the BFV scheme, relinearization reduces the size of ciphertexts after multiplication, and modulus switching can be used to reduce noise.

4. **Limited Precision in CKKS**: The CKKS scheme supports operations on real numbers but introduces approximation errors.

   **Workaround**: Carefully manage the scale parameter during encryption and after operations to maintain precision. Use rescaling operations to adjust the scale of ciphertexts.

5. **Complexity in Key Management**: Managing multiple keys (public, private, relinearization, rotation) can be complex and poses security risks if not handled properly.

   **Workaround**: Implement secure key management practices, store keys securely, and never expose the private key.

6. **Limited Integer Support**: HE is optimized for operations on integers. Working with non-integer numbers or requiring floating-point precision can be problematic, especially in the BFV scheme.

   **Workaround**: Use the CKKS scheme for operations that require real numbers and manage the scale to maintain precision.

### Pyfhel-Specific Limitations

Pyfhel is a Python wrapper for HE libraries, and it inherits some limitations from the underlying C++ libraries it wraps, as well as from the Python environment:

1. **Python Overhead**: Python can introduce additional overhead compared to native C++ implementations of HE.

   **Workaround**: Use Pyfhel's Cython extensions for performance-critical sections of code, or consider using the underlying C++ libraries directly for maximum performance.

2. **Serialization and Deserialization**: Saving and loading encrypted data and keys to and from disk can be slow and may introduce security risks.

   **Workaround**: Use serialization and deserialization features provided by Pyfhel carefully, ensuring encrypted data and keys are handled securely.

3. **Version Compatibility**: Pyfhel is under active development, and new versions may introduce changes that are not backward compatible.

   **Workaround**: Keep track of changes in the library, update code as necessary, and consider using virtual environments to manage dependencies.

By understanding these limitations and applying the appropriate workarounds, developers can effectively use Pyfhel for building privacy-preserving applications.

## Usage

To use this project, you will need Python 3 and the Pyfhel library installed on your system. You can install Pyfhel using pip:
```python
  pip install Pyfhel
```
## Encrypting a Credit Card Number:

To encrypt a credit card number and obtain the necessary keys:
```python
  python3 ccvalidate.py -e YOUR_CREDIT_CARD_NUMBER
```
This will output the encrypted number and a JSON string containing the keys.

## Verifying an Encrypted Credit Card Number:

To verify an encrypted credit card number using the provided keys:
```python
python3 ccvalidate.py -v ENCRYPTED_NUMBER -k '{"public_key": "...", "secret_key": "...", "relin_key": "...", "rotate_key": "..."}'
```

Replace ENCRYPTED_NUMBER and the keys with the actual values you received from the encryption step.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

  - The creators of the Luhn's Algorithm.
  - The developers of the Pyfhel library.
  - The cryptographic community for advancing the field of homomorphic encryption.
