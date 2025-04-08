# RSA Encryption and Decryption with Chinese Remainder Theorem (CRT) Comparison

This repository contains an implementation of RSA encryption and decryption, comparing the decryption process with and without using the Chinese Remainder Theorem (CRT). The goal is to demonstrate how CRT optimizes the decryption time for RSA-encrypted messages.

## Overview

The RSA algorithm is a widely-used cryptographic system that employs two keys: a public key for encryption and a private key for decryption. The Chinese Remainder Theorem (CRT) is a mathematical technique that can be used to speed up the decryption process in RSA by performing operations on smaller numbers (using the prime factorization of the modulus `n`).

In this implementation:
- We use 1024-bit prime numbers `p` and `q` to generate the RSA key pair.
- The public exponent `e` is set to 65537 (a common choice).
- We encrypt a message and compare the time it takes to decrypt it using the normal RSA decryption method and the optimized CRT-based method.

## Key Concepts

- **RSA Encryption**: RSA encryption involves exponentiation with the public key, followed by a modulus operation with the product of two large primes `p` and `q` (the modulus `n`).
- **Chinese Remainder Theorem (CRT)**: This technique improves the decryption speed by breaking down the decryption into smaller computations, which are faster when performed modulo `p` and `q` separately before combining them.

## Code Walkthrough

- **RSA Key Generation**: A 1024-bit RSA key pair is generated using the `pycryptodome` library.
- **Encryption**: A message (`m = 476921883457909`) is encrypted using the RSA public key with the OAEP padding scheme.
- **Decryption with CRT**: The ciphertext is decrypted using CRT, which reduces the computational complexity by exploiting the prime factors of `n`.
- **Normal Decryption**: The ciphertext is also decrypted using the standard RSA method without CRT for comparison.
- **Timing Comparison**: The time taken to decrypt the message using both methods is measured and compared.


### Example Output:
```
Ciphertext: b'/\x11\xe3\x02\x80\xc2\x91\xe87\x12w\x93\xa6W\x9d\x03i\x11Q\xc4\x89\x04\xf1\x8d\x19\x9a=\xec\x1b\xbc\xd3\xa2\xde> x\\z\x1aV\x9c\x13k\xff\xad\x02%\x02s\x19\xe3\xec5S\xb3Qve\xf10m\xf7\xcb\xf8-\xfb\x1e\xf0\xcb\xb5\xb4J\xc8\x18{\xfb\xc25\x06\x93\xc8\xac\x91\xf3\xcbv4OV\x1c\xca\x0bvq\xec\\\xf7x\xf7N.\x95<6\xde\x90U\xb5\xaa\x0fP\xdbe\x1a\xfa\xca\x8f\x16\xe2\xf5\x82\x9c\x85\xfc\xc8\xdf0$'
Decrypted Message using CRT: 32125330952783200598794909581942590702229869000544745034732406637631306718982566949102520763402875074640405088349349554711394537237469809805963544643852671182313823456511144274041392568567392231864144985188224113906680096675389868205860111952904206187818826655238113988117535765133398756184510895829945390513
Decrypted Message without CRT: 661982538219241941360211585195131912591413457973046508001059013744308456965917154403113197335332439464890640160742645700980803691133667534323085272972175749552598836706921193558434281098542512044452633090787619394227172514569848706640950499516487689721376266042791146764898535876637197471443551110842235302
Time taken with CRT: 0.003058195114135742 seconds
Time taken without CRT: 0.0055217742919921875 seconds
```

## Results

- **Decryption Time**: The results show that decryption using the Chinese Remainder Theorem (CRT) is faster than the standard RSA decryption method. In this case, CRT reduced the decryption time from **0.0055 seconds** to **0.0031 seconds**.
  
## Conclusion

Using the Chinese Remainder Theorem in RSA decryption provides a significant performance improvement. This optimization is crucial when dealing with large numbers, especially in real-world cryptographic applications where speed is important.
