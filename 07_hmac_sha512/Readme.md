# **HMAC-SHA-512 Implementation**

## Overview
This project provides an implementation of the **Hash-Based Message Authentication Code (HMAC)** using the **SHA-512** hash function. HMAC is used to verify both the data integrity and authenticity of a message. The implementation involves:
1. Padding the secret key to the correct block size.
2. Applying XOR operations to create inner and outer pads.
3. Using the SHA-512 hash function to compute the inner and outer hashes to generate the final HMAC.

### Key Concepts
1. **HMAC**: A construction for creating a message authentication code based on a cryptographic hash function.
2. **SHA-512**: A cryptographic hash function used to produce a fixed-size hash (512 bits).
3. **Key Padding**: Ensures the key is the correct block size (128 bytes for SHA-512).
4. **Inner and Outer Pads**: Special values XORed with the key to ensure HMAC’s security properties.

## Code Functionality
### 1. **HMAC-SHA-512 Implementation**
   - The `hmac_sha512` function implements the HMAC process using SHA-512. It takes a secret key and message as input and returns the computed HMAC.

### 2. **Verification**
   - The implementation is cross-verified by comparing the result from the custom function with the result obtained using the Python `hmac` module. If they match, the implementation is correct.

### 3. **Test Input**
   - The provided input string is `"This input string is being used to test my own implementation of HMAC-SHA-512."` for testing.

### 4. **Key Selection**
   - The secret key used for HMAC is `"Rakshita"`.

### 5. **Results**
   - The custom HMAC-SHA-512 result and the library result are printed for comparison.

## Example Output

```
Input String: This input string is being used to test my own implementation of HMAC-SHA-512.
Secret Key: Rakshita
Custom HMAC-SHA-512 Result: 5d53dda4777e901ac5355ffd06fcfd53efccc344426507af5c112c0e11992d0461405b4256a35efd9df23009c4c6779165d8470ee84c382481e427d9304cf8c5
Library HMAC-SHA-512 Result: 5d53dda4777e901ac5355ffd06fcfd53efccc344426507af5c112c0e11992d0461405b4256a35efd9df23009c4c6779165d8470ee84c382481e427d9304cf8c5

HMAC-SHA-512 implementation is correct.
```

## Future Relevance
Understanding HMAC and SHA-512 is essential for:
1. **Cryptographic Security**: HMAC is widely used in securing communications and ensuring data integrity in systems like SSL/TLS.
2. **Blockchain**: Many blockchain protocols use HMAC for verifying transactions and maintaining security.
3. **APIs & Authentication**: HMAC is frequently used in API key generation and secure token-based authentication systems.
4. **Data Integrity**: Ensuring data is not tampered with during transmission in secure systems.

## Lessons Learned
1. **HMAC Construction**: Implementing HMAC teaches you how cryptographic algorithms are designed to provide both authentication and integrity.
2. **Key Management**: The importance of key padding and handling keys securely in cryptographic applications.
3. **SHA-512**: SHA-512 provides strong security with a 512-bit hash, and understanding how to use it in HMAC is key for building secure systems.
4. **Verification**: Verifying custom cryptographic implementations against trusted libraries is crucial to ensure correctness.

## Conclusion
This project illustrates how to implement HMAC-SHA-512 from scratch and cross-verify the implementation. By understanding and implementing HMAC, we gain deeper insights into how secure communication and data integrity are maintained in modern systems. The ability to work with cryptographic algorithms is essential for anyone working in cybersecurity, blockchain, and secure communication technologies.
