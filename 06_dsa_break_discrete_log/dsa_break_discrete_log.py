#  Discrete Log Problem for DSA

# Samantha’s DSA public parameters are (p, q, g) = (103687, 1571, 21947), 
# and her public verification key is A = 31377. Employ whatever method you prefer to 
# solve the discrete log problem and find Samantha’s private signing key (but show in 
# detail what method you chose). Sign the document D = 510 with Samantha’s key, 
# using the random element k = 1105. 

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def baby_step_giant_step(p, g, A, q):
    m = int(q ** 0.5) + 1

    # Baby steps
    baby_steps = {pow(g, i, p): i for i in range(m)}

    # Precompute (g^(-m)) mod p
    gm_inv_m = pow(g, -m, p)

    # Giant steps
    for j in range(m):
        giant_step = (A * pow(gm_inv_m, j, p)) % p
        if giant_step in baby_steps:
            i = baby_steps[giant_step]
            return i + j * m

def sign_document(p, g, x, k, q, A, D):
    # Calculate r
    r = pow(g, k, p) % q

    # Calculate the hash of the document (assuming D is an integer, not a string)
    H_D = D  # You may replace this with your actual hash function

    # Calculate the modular inverse of k
    k_inv = mod_inverse(k, q)

    # Calculate s
    s = (k_inv * (H_D + x * r)) % q

    return r, s

# Given parameters
p = 103687
q = 1571
g = 21947
A = 31377
D = 510
k = 1105

# Solve the discrete logarithm problem
x_samantha = baby_step_giant_step(p, g, A, q)

# Sign the document D using Samantha's key
r_samantha, s_samantha = sign_document(p, g, x_samantha, k, q, A, D)

print("Samantha's Private Key (x):", x_samantha)
print("Samantha's Signature for D =", D, ":", r_samantha, s_samantha)

