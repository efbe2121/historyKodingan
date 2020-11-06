st = input("First sentence: ")
st2 = input("Second sentence: ")

count = 0
for i in range(len(st)):
    if st[i].lower() != st2[i].lower():
        count += 1
    else:
        count += 0
        
print (count)