
### ECDH and Diffie-Hellman Key Exchange Comparison

# This code compares the ECDH (Elliptic Curve Diffie-Hellman) key exchange with the traditional Diffie-Hellman (DH) key exchange. 
# It generates private and public keys for both Alice and Bob, computes shared secrets using both methods, and measures the time taken for each key exchange.
# The results are displayed, highlighting the advantages of ECDH in terms of speed. The `tqdm` library is used to visualize the progress of the computations.


!pip install cryptography
!pip install tqdm

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric import dh
import time
from tqdm import tqdm

# Generate Alice's private key and public key for ECDH
alice_private_key_ec = ec.generate_private_key(ec.SECP256R1(), default_backend())
alice_public_key_ec = alice_private_key_ec.public_key()

# Generate Bob's private key and public key for ECDH
bob_private_key_ec = ec.generate_private_key(ec.SECP256R1(), default_backend())
bob_public_key_ec = bob_private_key_ec.public_key()

# Alice computes the shared secret with Bob's public key for ECDH
start_time_ecdh = time.time()
with tqdm(total=100, position=0, leave=True) as pbar:
    for _ in range(100):
        alice_shared_secret_ec = alice_private_key_ec.exchange(ec.ECDH(), bob_public_key_ec)
        pbar.update(1)
end_time_ecdh = time.time()

# Bob computes the shared secret with Alice's public key for ECDH
with tqdm(total=100, position=0, leave=True) as pbar:
    for _ in range(100):
        bob_shared_secret_ec = bob_private_key_ec.exchange(ec.ECDH(), alice_public_key_ec)
        pbar.update(1)

# Compare the shared secrets to ensure they match for ECDH
if alice_shared_secret_ec == bob_shared_secret_ec:
    print()
    print("ECDH Shared Secret:", alice_shared_secret_ec.hex())
    print("ECDH Key Exchange took", end_time_ecdh - start_time_ecdh, "seconds")
else:
    print("Shared secrets do not match for ECDH!")

# Generate Alice's and Bob's parameters for Diffie-Hellman
parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

# Generate Alice's and Bob's private keys
alice_private_key = parameters.generate_private_key()
bob_private_key = parameters.generate_private_key()

# Generate Alice's and Bob's public keys
alice_public_key = alice_private_key.public_key()
bob_public_key = bob_private_key.public_key()

# Alice computes the shared secret with Bob's public key
start_time_dh = time.time()
with tqdm(total=100, position=0, leave=True) as pbar:
    for _ in range(100):
        alice_shared_secret = alice_private_key.exchange(bob_public_key)
        pbar.update(1)
end_time_dh = time.time()

# Bob computes the shared secret with Alice's public key
with tqdm(total=100, position=0, leave=True) as pbar:
    for _ in range(100):
        bob_shared_secret = bob_private_key.exchange(alice_public_key)
        pbar.update(1)

# Compare the shared secrets to ensure they match
if alice_shared_secret == bob_shared_secret:
    print()
    print("Diffie-Hellman Shared Secret:", alice_shared_secret.hex())
    print("Diffie-Hellman Key Exchange took", end_time_dh - start_time_dh, "seconds")
else:
    print("Shared secrets do not match for Diffie-Hellman!")

