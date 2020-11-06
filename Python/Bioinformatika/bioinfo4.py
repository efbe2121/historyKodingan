import math

l = 0.318
s = int(input("Blossom Score: "))
m = int(input("Quary Length: "))
n = int(input("Hit Length: "))
k = 0.14

expe = (l*s)
print (expe)
result = k*m*n*math.exp(-expe)
print("Result: %s"%round(result,5))