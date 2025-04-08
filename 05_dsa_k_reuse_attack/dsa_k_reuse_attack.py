# DSA Insecurity-This code demonstrates the implementation of the Digital Signature Algorithm (DSA) using the cryptography library in Python with same k.

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dsa
import hashlib
import random
import base64

def generate_keys(p_bit_length, q_bit_length):
    private_key = dsa.generate_private_key(
        key_size=1024, backend=default_backend()
    )

    # Extract public key
    public_key = private_key.public_key()

    # Extract p, q, and g
    p = private_key.private_numbers().public_numbers.parameter_numbers.p
    q = private_key.private_numbers().public_numbers.parameter_numbers.q
    g = private_key.private_numbers().public_numbers.parameter_numbers.g

    # Extract private exponent x
    x = private_key.private_numbers().x

    return p, q, g, x, private_key, public_key

# Generate keys with specific bit lengths
p_bit_length = 1024
q_bit_length = 160
p, q, g, x, private_key, public_key = generate_keys(p_bit_length, q_bit_length)

def sign_message(message, p, q, g, x, fixed_k):
    # Use SHA-1 to generate the digest
    h = hashlib.sha1()
    h.update(message.encode())
    digest = int.from_bytes(h.digest(), byteorder='big')

    # Use the fixed value of k
    k = fixed_k

    # Calculate r = (g^k mod p) mod q
    r = pow(g, k, p) % q

    # Calculate s = (k^(-1) * (digest + x*r)) mod q
    k_inv = pow(k, -1, q)
    s = (k_inv * (digest + x * r)) % q

    return r, s

def verify_signature(message, signature, p, q, g, y):
    r, s = signature

    # Use SHA-1 to generate the digest
    h = hashlib.sha1()
    h.update(message.encode())
    digest = int.from_bytes(h.digest(), byteorder='big')

    # Verify the signature
    w = pow(s, -1, q)
    u1 = (w * digest) % q
    u2 = (w * r) % q

    # Extract the integer value from the DSA public key
    y_int = y.public_numbers().y

    v = ((pow(g, u1, p) * pow(y_int, u2, p)) % p) % q

    return v == r

# Common value of k for both messages
fixed_k = random.randint(1, q - 1)

# Original message to sign
message1 = "582346829557612"

# Sign the original message with the fixed value of k
signature1 = sign_message(message1, p, q, g, x, fixed_k)

# Verify the signature for the original message
verification_result1 = verify_signature(message1, signature1, p, q, g, public_key)

# New message to sign
message2 = "8161474912583"

# Sign the new message with the same fixed value of k
signature2 = sign_message(message2, p, q, g, x, fixed_k)

# Verify the signature for the new message
verification_result2 = verify_signature(message2, signature2, p, q, g, public_key)

print("Generated Keys:")
print(f"p: {p}")
print(f"q: {q}")
print(f"g: {g}")

print("\nOriginal Message to Sign:", message1)
print("Generated Signature for Original Message:", signature1)
print("Verification Result for Original Message:", verification_result1)

print("\nNew Message to Sign:", message2)
print("Generated Signature for New Message:", signature2)
print("Verification Result for New Message:", verification_result2)
