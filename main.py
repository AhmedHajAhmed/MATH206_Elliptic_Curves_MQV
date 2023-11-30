

# Y^2 = X^3 + A*X + B

def add_points(P: tuple, Q: tuple, p: int, A):
    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and y1 == y2:
        # beta = (2 * x1 * x2 + A) / (2 * y1)
        beta = (2 * x1 * x2 + A) * pow(2 * y1, -1, p)   # multiplicative inverse value mod p
    else:
        # beta = (y2 - y1) / (x2 - x1)
        beta = (y2 - y1) * pow(x2 - x1, -1, p)          # multiplicative inverse value mod p

    x3 = (beta * beta - x1 - x2) % p
    y3 = (beta * (x1 - x3) - y1) % p

    return x3, y3


# Secp256k1 curve formula
a = 0
b = 7

# base point
G = (55066263022277343669578718895168534326250603453777594175500187360389116729240,
     32670510020758816978083085130507043184471273380659243275938904335757337482424)

# modulo
p = pow(2, 256) - pow(2, 32) - pow(2, 9) - pow(2, 8) - pow(2, 7) - pow(2, 6) - pow(2, 4) - pow(2, 0)

# order
n = 115792089237316195423570985008687907852837564279074904382605163141518161494337

# cofactor
h = 1

# print(p)

print(add_points(G, G, p, a))

