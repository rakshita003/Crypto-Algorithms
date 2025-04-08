# Miller-Rabin Probabilistic Primality Testing Algorithm
# This code demonstrates the Miller-Rabin probabilistic primality testing algorithm, which checks the primality of multiple numbers. 
# It performs the tests with a user-defined number of iterations (t=6) and provides results for each number tested
import random

def is_probable_prime(n, t=6):
    # Check for small values of n
    if n <= 1:
        return False
    if n <= 3:
        return True

    # Write n - 1 as 2^s * d, where d is odd
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # Perform Miller-Rabin tests with t random values of 'a'
    for _ in range(t):
        # Generate a random integer 'a' in the range [2, n-2]
        a = random.randint(2, n - 2)

        # Compute x = a^d % n
        x = pow(a, d, n)

        # If x is 1 or n - 1, continue to the next test
        if x == 1 or x == n - 1:
            continue

        # Repeat s - 1 times
        for _ in range(s - 1):
            # Compute x = x^2 % n
            x = pow(x, 2, n)

            # If x is n - 1, break the loop
            if x == n - 1:
                break
        else:
            # If the loop completes without finding a non-trivial square root of 1, n is composite
            return False

    # If all tests pass, n is probably prime
    return True

def main():
    # Test multiple numbers for primality
    numbers_to_test = [101, 16383, 1777, 9973, 10007]

    for n in numbers_to_test:
        result = is_probable_prime(n)
        if result:
            print(f"{n} is probably prime.")
        else:
            print(f"{n} is composite.")

if __name__ == "__main__":
    main()
