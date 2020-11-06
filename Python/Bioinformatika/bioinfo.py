code = input("Code: ")

def translation(co):
    start = ""
    for i in range (len(co)):
        if co[i] == "G":
            start += "C"
        elif co[i] == "C":
            start += "G"
        elif co[i] == "A":
            start += "T"
        elif co[i] == "T":
            start += "A"
    return start

def transcribe(co):
    start = ""
    for i in range (len(co)):
        if co[i] == "T":
            start += "U"
        else:
            start += co[i]
    return start

def printed(co):
    tmp = ""
    for i in range(len(co)):
        if i%3 == 0:
            tmp+= " "
        tmp+= co[i]
    return tmp

intermediate = translation(code)    
transcribed = transcribe(intermediate)

print("""
Start           : %s
Intermediate    : %s
Transcribed     : %s
"""%(printed(code),printed(intermediate),printed(transcribed)))

