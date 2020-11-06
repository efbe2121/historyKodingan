import math

def log(ha):
    return math.log(ha,4)

def factorial(n):
    tmp = 1
    for i in range(n):
        tmp = tmp * (i+1)
    return tmp

def nk(st):
    tmp = {}
    for i in range(len(st)):
        if st[i] in tmp:
            tmp[st[i]] += 1
        else:
            tmp[st[i]] = 1
    return tmp

def he(ddd):
    ddde = list(ddd.values())
    count = 1
    for i in range(len(ddde)):
        count*=factorial(ddde[i])
    return count

def kkk(l,n):
    return (1/l)*log(factorial(l)/n)

while(True):
    setri = input("Kalimat: ")
    haha = nk(setri)
    ehe = he(haha)
    kompleks = kkk(len(setri),ehe)
    print (ehe,len(setri),factorial(len(setri)))
    print (haha)
    print (round(kompleks,3))