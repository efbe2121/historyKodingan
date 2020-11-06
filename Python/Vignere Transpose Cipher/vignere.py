import string
#ALPHABET
alfa = "abcdefghijklmnopqrstuvwxyz"

def toAlp(text):
    for i in range (len(alfa)):
        if text.lower() == alfa[i]:
            return i
    

#KEY TO TEXT
def normalizeKey(textA, KEY):
    i, j = 0, 0
    keyNormalized = ''
    while (i < len(textA)):
        if textA[i] != ' ':
            if j > len(KEY) - 1:
                j = 0
            keyNormalized += KEY[j]
            j += 1
        else:
            keyNormalized += ' '
        i += 1
    return keyNormalized

#ENCRYPTION FUNCTION
def encrypt(textA, textB):
    c = ''
    for i in range(len(textA)):
        if textA[i] != ' ':
            c += alfa[((toAlp(textA[i]) + toAlp(textB[i])) % 26)]
        else:
            c += ' '
    return c

#DECRYPTION FUNCTION
def dekrip(textA, textB):
    d = ''
    for i in range(len(textA)):
        if textA[i] != ' ':
            d += alfa[((toAlp(textA[i]) - toAlp(textB[i])) + 26) % 26]
        else:
            d += ' '
    return d