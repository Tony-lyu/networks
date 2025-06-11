def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

p = 23
q = 17
e = 3
M = 4
C = 2

n = p * q
phi_n = (p - 1) * (q - 1)

d = modinv(e, phi_n)

encrypted_M = pow(M, e, n)

decrypted_C = pow(C, d, n)

print(f"Value of d: {d}")
print(f"Encrypted M: {encrypted_M}")
print(f"Decrypted C: {decrypted_C}")
