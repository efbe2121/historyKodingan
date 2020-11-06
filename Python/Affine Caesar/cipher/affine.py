def encrypt(P: str, A: int, B: int) -> str:
    """Encrypt using Affine Cipher"""
    C = ''
    letter = 0

    print('Plaintext:', P)
    print('A, B:', A, B)
    print('Algoritma: C = (AP + B) mod 26 | a,b in [0...25] dan fpb(a, 26) = 1')
    print('\n==========encrypt plain text==========')

    # Core algorithm
    for p in P:
        letter = ord(p)

        if letter in range(65, 91):
            letter -= 65
            C += chr((A*letter + B) % 26 + 65)
            print(p, ': ('+str(A)+'*'+str(letter), '+', str(B)+') mod 26 =', C[-1])
        elif letter in range(97, 123):
            letter -= 97
            C += chr((A*letter + B) % 26 + 97)
            print(p, ': ('+str(A)+'*'+str(letter), '+', str(B)+') mod 26 =', C[-1])
        else:
            if letter != 10:
                print(p, ': sqip.')
            C += p

    return C
###############################################################################
def egcd(a, b):
    """Extended Euclidean Algorithm for finding modular inverse
    Source: https://www.geeksforgeeks.org/implementation-affine-cipher/"""
    x,y, u,v = 0,1, 1,0
    while a!= 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x
def modinv(a, m):
    gcd, x = egcd(a, m)
    if gcd != 1:
        return None #modular inverse does not exist
    else:
        return x % m

def decrypt(C: str, A: int, B:int) -> str:
    """Decrypt using Affine Cipher"""
    P = ''
    letter = 0

    print('Ciphertext:', P)
    print('A, B:', A, B)
    print('Algoritma: P = (A^(-1) * (C - B)) mod 26 | A invers perkalian mod 26')
    print('\n==========decrypt cipher text==========')

    # Core algorithm
    A_inv = modinv(A, 26)
    print('Inverse A:', A_inv)

    for c in C:
        letter = ord(c)

        if letter in range(65, 91):
            letter -= 65
            P += chr(A_inv * (letter-B) % 26 + 65)
            print(c, ': ('+str(A_inv)+'*'+str(letter), '-', str(B)+') mod 26 =', P[-1])
        elif letter in range(97, 123):
            letter -= 97
            P += chr(A_inv * (letter-B) % 26 + 97)
            print(c, ': ('+str(A_inv)+'*'+str(letter), '-', str(B)+') mod 26 =', P[-1])
        else:
            if letter != 10:
                print(c, ': sqip.')
            P += c
    
    return P
