import math


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


def pow_(x, y, mod):
    t = 1
    while y > 0:
        if y % 2 == 0:
            x = (x * x) % mod
            y = y/2
        else:
            t = (x * t) % mod
            y = y - 1
    return t


# Find phi: N = p*q
# phi = (p-1)*(q-1)
def totient(N):
    sqrt_N = int(math.sqrt(N))
    phi = N
    prime_1 = 2
    for i in range(3, sqrt_N+1):
        if (N % i == 0):
            phi = (i-1)*(N/i-1)
            prime_1 = i
    return int(phi), int(prime_1)


# Find e: gcd(phi,e)=1
def find_e(phi):
    e = 3
    while True:
        if not gcd(e, phi) == 1:
            e += 2
        else:
            return e


# Find d: (d*e)%phi = 1
# d*e = k*phi+1 , k is an integar
# d = (k*phi+1) / e
def find_d(e, phi):
    k = 1
    while True:
        d, rem = divmod(k*phi+1, e)
        if rem == 0:
            return d
        k += 1


def decrypt(c, d, n):
    return pow_(c, d, n)


def encrypt(m, e, n):
    return pow_(m, e, n)


x = '2449500764025883 9800003 201812'.split(' ')
N = int(x[0])
e = int(x[1])
message = list(x[2])
c = []
for char in message:
    c.append(encrypt(ord(char), e, N))
string = u','.join([str(integar) for integar in c])
print(string)
