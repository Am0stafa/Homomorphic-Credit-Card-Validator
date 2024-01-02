import argparse
from Pyfhel import Pyfhel, PyPtxt, PyCtxt
import json

def setup_he():
    HE = Pyfhel()
    HE.contextGen(p=65537, m=8192, flagBatching=True)
    HE.keyGen()
    HE.relinKeyGen()
    HE.rotateKeyGen()
    return HE

def encrypt_number(HE, number):
    plaintext = PyPtxt([int(d) for d in number], HE)
    return HE.encrypt(plaintext)

def decrypt_and_verify(HE, encrypted_number_hex, keys):
    HE.restorepublicKey(bytes.fromhex(keys['public_key']))
    HE.restoresecretKey(bytes.fromhex(keys['secret_key']))
    HE.restorerelinKey(bytes.fromhex(keys['relin_key']))
    HE.restorerotateKey(bytes.fromhex(keys['rotate_key']))

    encrypted_number = PyCtxt(pyfhel=HE)
    encrypted_number.from_bytes(bytes.fromhex(encrypted_number_hex))
    decrypted_number = HE.decrypt(encrypted_number)
    return luhns_algorithm(decrypted_number)

def luhns_algorithm(cc_number):
    cc_digits = [int(d) for d in str(cc_number)]
    cc_digits.reverse()
    for i in range(len(cc_digits)):
        if i % 2 == 1:
            cc_digits[i] *= 2
            if cc_digits[i] > 9:
                cc_digits[i] -= 9
    return sum(cc_digits)

def main():
    parser = argparse.ArgumentParser(description='Credit Card Number Validator CLI')
    parser.add_argument('-e', '--encrypt', type=str, help='Encrypt a credit card number')
    parser.add_argument('-v', '--verify', type=str, help='Verify an encrypted credit card number')
    parser.add_argument('-k', '--keys', type=str, help='JSON string of all necessary keys for verification')

    args = parser.parse_args()
    HE = setup_he()

    if args.encrypt:
        encrypted_number = encrypt_number(HE, args.encrypt)
        keys = {
            'public_key': HE.getpublicKey().to_bytes().hex(),
            'secret_key': HE.getsecretKey().to_bytes().hex(),
            'relin_key': HE.getrelinKey().to_bytes().hex(),
            'rotate_key': HE.getrotateKey().to_bytes().hex()
        }
        print(json.dumps({
            "encrypted_number": encrypted_number.to_bytes().hex(),
            "keys": keys
        }))

    elif args.verify and args.keys:
        keys = json.loads(args.keys)
        is_valid = decrypt_and_verify(HE, args.verify, keys)
        print("Credit card number is valid!" if is_valid else "Credit card number is invalid.")

if __name__ == "__main__":
    main()