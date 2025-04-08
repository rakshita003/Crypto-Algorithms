# Cryptographic Algorithms and Protocols in Python

This repository showcases a variety of **cryptographic algorithms** and **security protocols**, all implemented in Python. It serves as a practical guide for exploring key cryptographic concepts, from prime number generation to secure key exchange, digital signatures, and message authentication. Each implementation not only demonstrates the algorithm’s functionality but also delves into the underlying mathematical principles and vulnerabilities, offering deeper insights into modern cryptography and its application in securing data and communications.

## Folder Structure

- [**01_miller_rabin/**](./01_miller_rabin) - Implementation of the **Miller-Rabin primality test**, a probabilistic method for generating prime numbers used in key generation.
- [**02_rsa_crt/**](./02_rsa_crt) - Optimized **RSA encryption** using the **Chinese Remainder Theorem (CRT)** for faster modular exponentiation in encryption and decryption.
- [**03_ECDH_vs_DH_Comparison/**](./03_ECDH_vs_DH_Comparison) - A **comparison** between **Elliptic Curve Diffie-Hellman (ECDH)** and traditional **Diffie-Hellman (DH)** key exchange protocols.
- [**04_dsa_signing/**](./04_dsa_signing) - **Digital Signature Algorithm (DSA)** for secure message signing and verification.
- [**05_dsa_k_reuse_attack/**](./05_dsa_k_reuse_attack) - Demonstration of a **vulnerability in DSA** when the random value `k` is reused, exposing cryptographic risks.
- [**06_dsa_break_discrete_log/**](./06_dsa_break_discrete_log) - **Exploration** of the **discrete logarithm problem** and how it can be exploited to break DSA signatures.
- [**07_hmac_sha512/**](./07_hmac_sha512) - Implementation of **HMAC** (Hash-based Message Authentication Code) using **SHA-512** to verify message integrity and authenticity.

## In-Depth Exploration of Cryptographic Concepts

This repository goes beyond simply implementing algorithms. It aims to provide:

- **Theoretical Insights**: Learn the foundational principles behind each cryptographic algorithm, such as modular arithmetic, prime number generation, and elliptic curve theory.
- **Security Considerations**: Understand common vulnerabilities (e.g., **key reuse** in DSA or poor randomness in cryptographic key generation) and how they can compromise cryptographic systems.
- **Practical Applications**: See how each algorithm is applied in real-world scenarios like secure communication, digital signatures, and data integrity.

### Highlights:
- **Primality Testing**: Explore the **Miller-Rabin** test, a fast, probabilistic method essential for **RSA** key generation.
- **RSA Optimizations**: Learn how applying **Chinese Remainder Theorem (CRT)** optimizes the **RSA** algorithm for large integers, improving performance significantly.
- **Key Exchange**: Understand how **ECDH** and **DH** work, comparing the security and efficiency of modern elliptic curve-based key exchange versus traditional methods.
- **Digital Signatures**: Investigate the **DSA** algorithm and how vulnerabilities like **key reuse** can lead to catastrophic failures in security.
- **HMAC for Authentication**: Study the **HMAC-SHA-512** algorithm for ensuring the integrity and authenticity of transmitted messages.

## Conclusion

This repository is a valuable resource for anyone interested in the inner workings of cryptographic protocols. It serves as both a **learning tool** and a **practical guide** to understanding the critical importance of secure cryptographic practices. By working through the examples, you’ll gain hands-on experience with the implementation and application of cryptographic algorithms, while also learning how vulnerabilities arise and how to mitigate them.

