# ECDH vs DH Key Exchange Performance Comparison

## Overview

This repository contains code that compares the **Elliptic Curve Diffie-Hellman (ECDH)** and **Diffie-Hellman (DH)** key exchange protocols. The key exchange is a cryptographic technique that enables two parties to securely share a secret key over an insecure channel. This code demonstrates both protocols, computes their shared secrets, and compares the speed at which each method operates.

The project uses the **`cryptography`** and **`tqdm`** libraries for elliptic curve and Diffie-Hellman key generation, shared secret computation, and progress visualization. The key comparison between **ECDH** and **DH** is based on their performance in terms of **time taken** to complete the key exchange.

## Key Features

- **Elliptic Curve Diffie-Hellman (ECDH)**: A modern cryptographic method using elliptic curve cryptography to create secure key exchanges. It offers a higher security level with shorter key sizes, making it more efficient than traditional DH for the same security level.
  
- **Diffie-Hellman (DH)**: A classic cryptographic method based on modular arithmetic that allows two parties to generate a shared secret key, traditionally using large prime numbers.

- **Performance Comparison**: The code measures the time taken for both protocols to compute the shared secret, providing a performance comparison between ECDH and DH at the same security level.

## Prerequisites

To run this code, you'll need to install the following Python packages:

- **cryptography**: Provides the necessary cryptographic algorithms for ECDH and DH.
- **tqdm**: A library for displaying progress bars to track the completion of operations.

You can install these dependencies using `pip`:

```bash
pip install cryptography
pip install tqdm
```

## Structure

The repository contains the following code:

### 1. **ECDH Key Exchange**:
   - Alice and Bob each generate their private and public keys using **Elliptic Curve** cryptography.
   - Alice computes the shared secret using Bob's public key and vice versa.
   - The shared secret is compared to ensure both parties compute the same secret.
   - The time taken for 100 computations is measured to assess performance.

### 2. **Diffie-Hellman Key Exchange**:
   - Alice and Bob each generate their private and public keys using **Diffie-Hellman**.
   - The shared secret is computed by both Alice and Bob using each other’s public keys.
   - The time taken for 100 computations is measured for performance comparison.

### 3. **Performance Comparison**:
   - Both methods are compared for the same security level (2048-bit key size for DH).
   - The performance results (in terms of time taken) are displayed for both ECDH and DH key exchanges.

## How to Run

To run the code and see the comparison:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name/ECDH_vs_DH_Comparison.git
   cd ECDH_vs_DH_Comparison
   ```

2. Install the required libraries:
   ```bash
   pip install cryptography tqdm
   ```

3. Execute the script:
   ```bash
   python ecdh_vs_dh_comparison.py
   ```

4. You will see the following outputs:
   - **ECDH Shared Secret** and the time it took to compute the shared secret.
   - **DH Shared Secret** and the time it took to compute the shared secret.

## Output Example

### ECDH Output:
```text
ECDH Shared Secret: abcdef1234567890
ECDH Key Exchange took 0.745 seconds
```

### Diffie-Hellman Output:
```text
Diffie-Hellman Shared Secret: abcdef1234567890
Diffie-Hellman Key Exchange took 2.543 seconds
```

### Observations:

- **ECDH** produces the same shared secret as **DH**, but takes considerably less time for computation due to the shorter key sizes used in elliptic curve cryptography.
- The speed difference highlights the advantage of using **ECDH** over **DH**, especially in performance-critical applications like mobile and embedded devices.

## Explanation of Code

### Libraries Used

1. **cryptography**:
   - The `cryptography` package provides tools for secure cryptographic operations such as key generation and shared secret computation for both ECDH and DH protocols.

2. **tqdm**:
   - The `tqdm` library is used to display a progress bar while computing the shared secret, offering a visual indicator of the ongoing computations.

### Key Exchange Process

1. **ECDH**:
   - **Private keys** are generated using the **SECP256R1** elliptic curve.
   - **Public keys** are derived from the private keys.
   - Alice and Bob exchange public keys and compute a shared secret using the `exchange()` method.

2. **Diffie-Hellman**:
   - Parameters for the DH key exchange are generated using a 2048-bit prime.
   - Private and public keys are generated, and the shared secret is computed using the `exchange()` method.

### Time Measurement

The script measures the time taken to compute the shared secret for both protocols, using `time.time()` for precise timing.

### Performance Visualization

A progress bar is displayed during the shared secret computation using `tqdm`, allowing you to track the operation's progress.

## Conclusion

This code demonstrates the **Elliptic Curve Diffie-Hellman** protocol's efficiency over the traditional **Diffie-Hellman** key exchange. ECDH achieves the same level of security with smaller key sizes and significantly faster computation, making it a more efficient choice in modern cryptographic applications.

