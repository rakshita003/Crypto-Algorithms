# Crypto Algorithms 

This repository presents a collection of cryptographic algorithms and protocols, implemented in Python to demonstrate various aspects of modern cryptography. The algorithms showcased here span multiple cryptographic techniques, from primality testing to secure key exchange, digital signatures, and message authentication. Each algorithm is designed to explore both foundational concepts and specific vulnerabilities within cryptographic systems, offering insights into the inner workings and potential security risks.

## Folder Structure

- `01_miller_rabin/` - Implementation of the Miller-Rabin primality test for probabilistic prime number generation.
- `02_rsa_crt/` - Optimized RSA implementation leveraging the Chinese Remainder Theorem (CRT) for faster modular exponentiation.
- `03_ECDH_vs_DH_Comparison/` - A detailed comparison between Elliptic Curve Diffie-Hellman (ECDH) and traditional Diffie-Hellman (DH) key exchange protocols.
- `04_dsa_signing/` - Digital Signature Algorithm (DSA) for secure signing and verification of messages.
- `05_dsa_k_reuse_attack/` - A demonstration of a cryptographic vulnerability when the random value `k` is reused in DSA signatures, illustrating the risks of poor key management.
- `06_dsa_break_discrete_log/` - An exploration of the discrete logarithm problem and how it can be exploited to break DSA signatures.
- `07_hmac_sha512/` - Implementation of HMAC (Hash-based Message Authentication Code) using SHA-512 for verifying message integrity and authenticity.

## In-Depth Exploration of Cryptographic Concepts

Each implementation not only demonstrates a working algorithm but also aims to provide practical insights into the theory and application of cryptography. The focus is on understanding the mathematical underpinnings and cryptographic principles behind each algorithm, as well as showcasing potential security flaws and how they can be mitigated.

For example, the repository delves into:
- **Primality testing** with Miller-Rabin, a widely used probabilistic test in cryptographic key generation.
- **RSA optimizations** using the Chinese Remainder Theorem, which significantly improves performance for large integers in RSA encryption and decryption.
- **Key exchange mechanisms** comparing the performance and security between classic Diffie-Hellman and modern Elliptic Curve Diffie-Hellman (ECDH).
- **Digital signature security** and attacks, such as demonstrating how poor randomness in DSA key generation can lead to severe vulnerabilities.

## Conclusion

This repository serves as a learning tool and a practical guide for anyone looking to deepen their understanding of cryptographic protocols and security. It’s a resource that highlights the critical role cryptography plays in securing modern communication and data, while also revealing the importance of secure implementation practices.

