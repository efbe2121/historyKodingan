from math import ceil, sqrt



def encrypt_sprial(array,baris,kolom):
    top = 0
    left = 0
    right = kolom-1
    bottom = baris-1
    indextext = 0
    arah = "kanan"
    while(top<=bottom and left <= right):
        if arah == "kanan":

            index = left

            while(index<=right):
                if(indextext<=len(plaintext)-1):
                    array[top][index] = plaintext[indextext]
                    indextext+=1
                index+=1
            top+=1
            arah = "bawah"

        elif arah == "bawah":

            index = top
            while(index<=bottom):
                if (indextext <= len(plaintext) - 1):
                    array[index][right] = plaintext[indextext]
                    indextext += 1
                index+=1
            right-=1
            arah = "kiri"

        elif arah == "kiri":
            index = right

            while(index >= left):
                if (indextext <= len(plaintext) - 1):
                    array[bottom][index] = plaintext[indextext]
                    indextext += 1
                index-=1
            bottom-=1
            arah = "atas"

        elif arah == "atas":
            index = bottom
            while(index>= top):
                if (indextext <= len(plaintext) - 1):
                    array[index][left] = plaintext[indextext]
                    indextext += 1
                index-=1
            left+=1
            arah = "kanan"

    print("Hasil Enkripsi: ", end="")
    for i in range(kolom):
        for j in range(baris):
            print(array[j][i], end="")
    print()

def decrypt_spriral(array, baris, kolom):
    indextext = 0
    for i in range(kolom):
        for j in range(baris):
            array[j][i] = chipertext[indextext]
            indextext+=1
    top = 0
    left = 0
    right = kolom - 1
    bottom = baris - 1
    indextext = 0
    arah = "kanan"
    print("hasil dekripsi: ", end ="")

    while (top <= bottom):  # and left <= right):
        if arah == "kanan":

            index = left

            while (index <= right):
                if(array[top][index]!="*"):
                    print(array[top][index], end="")
                index += 1
            top += 1
            arah = "bawah"

        elif arah == "bawah":

            index = top
            while (index <= bottom):
                if(array[index][right]!="*"):
                    print(array[index][right], end="")
                index += 1
            right -= 1
            arah = "kiri"

        elif arah == "kiri":
            index = right
            while (index >= left):
                if(array[bottom][index]!="*"):
                    print(array[bottom][index], end="")
                index -= 1
            bottom -= 1
            arah = "atas"

        elif arah == "atas":
            index = bottom
            while (index >= top):
                if(array[index][left]!="*"):
                    print(array[index][left], end="")
                index -= 1
            left += 1
            arah = "kanan"
    print()



status = True
while(status == True):
    pilihan=int(input("masukkan pilihan 1. encrypt  2. decrypt:   3. exit: "))
    if(pilihan == 1):
        plaintext = input("Masukkan text:")
        baris = ceil(sqrt(len(plaintext)))
        kolom = baris
        array = [["*" for i in range(baris)] for j in range(kolom)]
        encrypt_sprial(array,baris,kolom)
    elif(pilihan ==2):
        chipertext = input("masukkan ciphertext: ")
        baris = ceil(sqrt(len(chipertext)))
        kolom = baris
        array = [["*" for i in range(baris)] for j in range(kolom)]
        decrypt_spriral(array, baris, kolom)
    else:
        status = False







