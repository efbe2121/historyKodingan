""""
This is an algorithm of 2 encryption combined
as one

vignere
transpose

"""

import vignere
import transpose
import math

"""
Here lies all of declaration
everything as one
"""
flag = True       #This is as flag for our looping section
key = ''          #This is our lovely key
keyNormal = ''    #This is spesific key for vignere method
keyReversed = ''  #This is spesific key for vignere method
keyTranspose = [] #This is spesific key for transpose method
keySorted = []    #This is spesific key for transpose method
lovelyText = ''   #This is our plain text
textSp = ''       #This is spesific text for transpose
cipherText = ''   #This is our encrypted text
kolom = ''        #Penentu kolom cipherText

"""
So our encryption algorithm is going to be
1. Encrypt text with key
2. Encrypt text with reversed key 
3. Decrypt text with key
4. Transpose the text
"""

def krispi():
    #First step
    keyNormal = vignere.normalizeKey(lovelyText,key)
    cipherText = vignere.encrypt(lovelyText,keyNormal)
    print ("""Here's first cipher text
    1st Vignere : %s"""%cipherText)

    #Second step
    keyReversed = key[::-1]
    keyReversed = vignere.normalizeKey(cipherText,keyReversed)
    cipherText = vignere.encrypt(cipherText,keyReversed)
    print ("""Here's next cipher text
    2nd Vignere Reversed key : %s"""%cipherText)

    #Third step
    cipherText = vignere.dekrip(cipherText,keyNormal)
    print ("""Here's next cipher text
    3rd Vignere : %s"""%cipherText)

    #Fourth Step
    kolom = int(math.ceil(len(lovelyText) / len(key)))
    keyTranspose = transpose.makeRow(key,keySorted)
    textSp = transpose.splitText(cipherText,len(keyTranspose))
    cipherText = [ [ None for i in range(len(keyTranspose)) ] for j in range(kolom) ]
    cipherText = transpose.transpos(kolom,keyTranspose,cipherText,textSp)
    cipherText = transpose.printCipher2(kolom,keyTranspose,cipherText)
    print ("""Here's next cipher text
    4th Transpose : %s"""%cipherText)
    #And after that we return the result
    return cipherText

"""
Now for our decryption algorithm is going to be
1. Decrypt text with transpose
2. Encrypt text with key 
3. Decrypt text with reversed key
4. Decrypt text with key
"""

def dedekrispi():
    #First step
    kolom = int(math.ceil(len(cipherText) / len(key)))
    keyTranspose = transpose.makeRow(key,keySorted)
    lovelyText = transpose.dekrip(kolom,keyTranspose,cipherText)
    print ("""Here's first plain text
    1st Transpose : %s"""%lovelyText)

    #Second step
    keyNormal = vignere.normalizeKey(lovelyText,key)
    lovelyText = vignere.encrypt(lovelyText,keyNormal)
    print ("""Here's next plain text
    2nd Vignere : %s"""%lovelyText)
    
    #Third step
    keyReversed = key[::-1]
    keyReversed = vignere.normalizeKey(lovelyText,keyReversed)
    lovelyText = vignere.dekrip(lovelyText,keyReversed)
    print ("""Here's next plain text
    3rd Vignere : %s"""%lovelyText)
    
    #Fourth step
    lovelyText = vignere.dekrip(lovelyText,keyNormal)
    print ("""Here's next plain text
    4th Vignere : %s"""%lovelyText)
    
    #Obviously we return the result
    return lovelyText




"""
This is the main loop
We need this one
"""

while (flag):
    choices = input ("""
    Hello! And welcome to our encryption program!
    What're you going to do?\n
    1.Encryption
    2.Decryption
    Answer: """)
    choices = int(choices)

    """
    Now we're doing some stuff
    please bear in mind that 
    sometimes i dont even understand 
    what am i doing
    """

    if choices == 1:

        key = input("Please input key: ")
        lovelyText = input("Please input your text: ")
        cipherText = krispi()
        print ("Here's your encrypted text: ",end=''), print (cipherText)

    else:

        key = input("Please input key: ")
        cipherText = input("Please input your encrypted text: ")
        lovelyText = dedekrispi()
        print ("Here's your plain text: ",end=''), print (lovelyText)

    chcs = input ("Are you done?\nSay 'y' if you're done and else if you need more time\nAnswer: ")
    if chcs.lower() == 'y':
        flag = False
    else:
        flag = True