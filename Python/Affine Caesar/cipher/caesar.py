def encrypt(P: str, K: int) -> str:
    """Encrypt using Caesar Cipher"""
    C = ''
    letter = 0

    print('Plaintext:', P)
    print('Key:', K)
    print('Algoritma: C = E(P, k) = (P + k) mod 26')
    print('\n==========encrypt plain text==========')

    # Core algorithm
    for p in P:
        letter = ord(p)

        if letter in range(65, 91):
            letter -= 65
            C += chr((letter + K) % 26 + 65)
            print(p, ': ('+str(letter), '+', str(K)+') mod 26 =', C[-1])
        elif letter in range(97, 123):
            letter -= 97
            C += chr((letter + K) % 26 + 97)
            print(p, ': ('+str(letter), '+', str(K)+') mod 26 =', C[-1])
        else:
            if letter != 10:
                print(p, ': sqip.')
            C += p

    return C

def decrypt(C: str, K: int) -> str:
    """Decrypt using Caesar Cipher"""
    P = ''
    letter = 0

    print('Ciphertext:', P)
    print('Key:', K)
    print('Algoritma: P = D(C, k) = (C - k) mod 26')
    print('\n==========decrypt plain text==========')

    # Core algorithm
    for c in C:
        letter = ord(c)

        if ord(c) in range(65, 91):
            letter -= 65
            P += chr((letter - K) % 26 + 65)
            print(c, ': (' + str(letter), '-', str(K) + ') mod 26 =', P[-1])
        elif ord(c) in range(97, 123):
            letter -= 97
            P += chr((letter - K) % 26 + 97)
            print(c, ': (' + str(letter), '+', str(K) + ') mod 26 =', P[-1])
        else:
            if letter != 10:
                print(c, ': sqip.')
            P += c

    return P
