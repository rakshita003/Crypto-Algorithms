# Miller-Rabin Primality Testing Algorithm

This repository contains an implementation of the Miller-Rabin probabilistic primality testing algorithm, which checks if a given number is a probable prime. This method is widely used due to its efficiency in primality testing for large numbers.

## Overview

The Miller-Rabin algorithm is a probabilistic test for primality. It is based on the idea that, for a prime number, certain mathematical conditions hold true when using modular exponentiation. By running multiple iterations of the test, we can determine whether a number is likely prime or composite.

This implementation checks for probable primality of multiple numbers and performs the test for a user-defined number of iterations (default: 6 iterations). The goal of this implementation is to find a 15-bit integer that is probably prime with a high confidence level.

## Features
- **Miller-Rabin Algorithm**: Implements the primality test directly without using external libraries.
- **Multiple Iterations**: Configurable iteration count for increased confidence in the test results (default: 6 iterations).
- **Tested Numbers**: A set of numbers is tested for primality, and the results are displayed in the console.

## Algorithm Explanation

1. **Miller-Rabin Primality Test**: The algorithm checks whether a given number `n` is prime or composite by performing multiple tests with random bases `a`. For each base, the algorithm checks whether certain modular conditions hold true.
2. **Probabilistic Nature**: The test is probabilistic, meaning that after running the test a certain number of times (`t` iterations), the algorithm provides a result with high confidence, but it can never be 100% certain.

## Code Walkthrough

- **is_probable_prime(n, t=6)**: This function performs the Miller-Rabin test `t` times with randomly chosen bases. It returns `True` if the number is probably prime and `False` if it is composite.
- **main()**: Tests a list of numbers for primality and prints whether each number is probably prime or composite.

## Usage

To run the script, simply execute it in a Python environment:

```bash
python miller_rabin.py
```

The script will test a set of predefined numbers and output whether each number is probably prime or composite.

### Example Output:
```
101 is probably prime.
16383 is composite.
1777 is probably prime.
9973 is probably prime.
10007 is probably prime.
```

## Improvements and Suggestions

While the implementation is functional, here are some ideas for improving the code:
1. **Optimization of Random Base Selection**: Instead of selecting a random base between 2 and `n-2`, we could use deterministic bases for small numbers or apply other optimizations like the Baillie-PSW primality test.
2. **Input from User**: Allow the user to input numbers to test for primality instead of using a predefined list.
3. **Testing Larger Numbers**: Expand the list of numbers or allow input from larger datasets, especially to test the algorithm on larger primes.
4. **Performance Considerations**: Consider the performance impact when testing very large numbers. Using efficient modular exponentiation and random number generation can make the algorithm faster.

## Conclusion

The Miller-Rabin test provides an efficient way to test for primality, especially for large numbers where other methods like trial division are too slow. This implementation is useful for cryptographic applications and number theory research.

