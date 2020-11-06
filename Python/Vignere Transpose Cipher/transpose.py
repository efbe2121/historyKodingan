def splitText(text,n):
    return [text[i:i+n] for i in range(0, len(text), n)]

def makeRow(key,keySorted):
    keySorted = sorted(key)
    key = splitText(key,1)
    for i in range(len(key)):
        for j in range(len(key)):
            if keySorted[j] == key[i]:
                key[i] = j + 1
                keySorted[j] = ''
    return key

def returnIndex(textA,xXx):
    return textA.index(xXx)

def transpos(kolom,key,textA,textB):
    for i in range(kolom):
        for j in range(len(key)):
            try:
                textA[i][j] = textB[i][key[j]-1]
            except:
                textA[i][j] = '*'
    return textA

def reverse(kolom,key,textA):
    index = 0
    tmp = [ [ None for i in range(len(key)) ] for j in range(kolom) ]
    for i in range (len(key)):
        for j in range (kolom):
            tmp[j][i] = textA[index]
            index += 1
    return tmp

def dekrip(kolom,key,textA):
    tmp = ''
    textA = reverse(kolom,key,textA)
    for i in range (kolom):
        for j in range (len(key)):
            tmp += textA[i][returnIndex(key,j+1)]
    return tmp.replace('*','')

def printCipher2(kolom,key,textA):
    tmp = ''
    for i in range (len(key)):
        for j in range (kolom):
            tmp+=textA[j][i]
    return tmp