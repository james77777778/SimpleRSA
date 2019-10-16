

def gcd(a, b):
    if b > a:
        if b % a == 0:
            return a
        else:
            return gcd(b % a, a)
    else:
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)


def find_d(phi_n, e):
    k = 1
    mod0 = False
    while not mod0:
        d, rem = divmod(k*phi_n+1, e)
        if rem == 0:
            return d
        k += 1


def find_e(phi_n):
    e = 3
    while True:
        if not gcd(e, phi_n) == 1:
            e += 2
        else:
            return e


def generate_keys(p1, p2):
    n = p1*p2
    phi_n = (p1-1)*(p2-1)
    e = find_e(phi_n)
    d = int(find_d(phi_n, e))
    return ((e, n), (d, n))


def endecrypt(key, m):
    return pow(m, key[0], key[1])


public_key, private_key = generate_keys(11, 17)
