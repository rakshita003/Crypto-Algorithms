# RSA Encryption and Decryption with Chinese Remainder Theorem (CRT) Comparison
# This code demonstrates RSA encryption and decryption with the Chinese Remainder Theorem (CRT) comparison. It encrypts a message, 
# decrypts it using both CRT and normal methods, and measures the time taken for each decryption approach.
# The results are displayed, showing the advantages of CRT in terms of speed.
!pip install pycryptodome

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time

# Generate a 1024-bit RSA key pair
key = RSA.generate(1024)

# Public exponent
e = 65537

# Encrypt the message
message = 476921883457909
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message.to_bytes((message.bit_length() + 7) // 8, byteorder='big'))

# CRT Decryption
n = key.n
d = key.d
p = key.p
q = key.q
u = key.u

start_time_crt = time.time()

mp = pow(int.from_bytes(ciphertext, byteorder='big'), d % (p - 1), p)
mq = pow(int.from_bytes(ciphertext, byteorder='big'), d % (q - 1), q)
h = (u * (mp - mq)) % p

decrypted_message_crt = mq + h * q

end_time_crt = time.time()

# Normal Decryption (without CRT)
start_time_normal = time.time()
decrypted_message_normal = pow(int.from_bytes(ciphertext, byteorder='big'), d, n)
end_time_normal = time.time()

# Calculate the time taken for both decryption methods
time_taken_crt = end_time_crt - start_time_crt
time_taken_normal = end_time_normal - start_time_normal

# Display the results
print("Ciphertext:", ciphertext)
print("Decrypted Message using CRT:", decrypted_message_crt)
print("Decrypted Message without CRT:", decrypted_message_normal)
print("Time taken with CRT:", time_taken_crt, "seconds")
print("Time taken without CRT:", time_taken_normal, "seconds")
