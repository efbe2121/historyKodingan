import cipher.caesar as caesar
import cipher.affine as affine

print("1. Caesar Cipher      2. Affine Cipher")
choose = int(input("1/2? "))

if choose == 1:
    print("1. Decypt     2. Encrypt")
    choose = int(input("1/2? "))

    if choose == 1:
        text = input("Ciphertext: ")
        key = int(input("Key: "))
        # Decrypt Caesar
        print(caesar.decrypt(text, key))

    elif choose == 2:
        text = input("Plaintext: ")
        key = int(input("Key: "))
        # Encrypt Caesar
        print(caesar.encrypt(text, key))


elif choose == 2:
    print("1. Decypt     2. Encrypt")
    choose = int(input("1/2? "))

    if choose == 1:
        text = input("Ciphertext: ")
        A = int(input("A: "))
        B = int(input("B: "))
        # Decrypt Affine
        print(affine.decrypt(text, A, B))
        
    elif choose == 2:
        text = input("Plaintext: ")
        A = int(input("A: "))
        B = int(input("B: "))
        # Decrypt Affine
        print(affine.encrypt(text, A, B))

del(choose)
