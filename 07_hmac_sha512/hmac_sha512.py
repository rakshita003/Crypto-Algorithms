#  HMAC-SHA-512 Implementation

# This code provides an implementation of the Hash-Based Message Authentication Code (HMAC) using the SHA-512 hash function.

import hashlib
import hmac

def hmac_sha512(key, message):
    block_size = 128  # 1024 bits
    sha512 = hashlib.sha512()

    # Key padding
    if len(key) > block_size:
        key = hashlib.sha512(key).digest()
    if len(key) < block_size:
        key += b'\x00' * (block_size - len(key))

    # XOR inner and outer padding with the key
    inner_pad = bytes(x ^ 0x36 for x in key)
    outer_pad = bytes(x ^ 0x5C for x in key)

    # Compute inner hash
    sha512.update(inner_pad + message.encode())
    inner_hash = sha512.digest()

    # Reset sha512 object for outer hash
    sha512 = hashlib.sha512()
    sha512.update(outer_pad + inner_hash)

    # Compute outer hash
    return sha512.digest()

# Given test input string
input_string = "This input string is being used to test my own implementation of HMAC-SHA-512."

# Secret key for HMAC
key = b'Rakshita'

# Use your implementation
result_custom = hmac_sha512(key, input_string)

# Use the hmac module to cross-verify
result_library = hmac.new(key, input_string.encode(), hashlib.sha512).digest()

# Print the information
print("Input String:", input_string)
print("Secret Key:", key.decode())
print("Custom HMAC-SHA-512 Result:", result_custom.hex())
print("Library HMAC-SHA-512 Result:", result_library.hex())
print()

# Check if the results match
if result_custom == result_library:
    print("HMAC-SHA-512 implementation is correct.")
else:
    print("HMAC-SHA-512 implementation is incorrect.")
