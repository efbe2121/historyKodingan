#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Sastrawi is a library of Indonesian stopwords remover.
Can be installed from

pip install Sastrawi or pip3 install Sastrawi

PrettyTables is a library to help me print tables
in short, it creates pretty table :D

pip install prettytable or pip3 install prettytable
"""
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import numpy as np
import pandas as pd
import string #This is used to split the text, so we could get the words
import itertools #This is used to limit the dictionary
import re #This is regex
from prettytable import PrettyTable
mn=PrettyTable() #This is our table that carries our data till the end


# In[2]:


class NB:
    """
    THIS IS CLASS FOR NAIVE BAYES 
    FUNCTIONS WITH LAPLACE SMOOTHING
    
    getCountClickbait to get count of all words in Clickbait class
    getCountNonClickbait is same as above but for Non Clickbait class
    
    getCountwordCB to get count of particular unique word in Clickbait class
    getCountwordNCb is same as above but for Non Clickbait class
    
    estimateWord to get the conditional probabilities of each word
    in each class
    """
    def __init__(self,cb,ncb):
        self.cb = cb
        self.ncb = ncb
    
    def getCountClickbait(self):
        count = 0
        tmp = list(self.cb.values())
        for i in range(len(tmp)):
            count+=tmp[i][0]
        return count
    
    def getCountNonClickbait(self):
        count = 0
        tmp = list(self.ncb.values())
        for i in range(len(tmp)):
            count+=tmp[i][0]
        return count
    
    def getCountwordCb(self,word):
        if word in self.cb:
            return self.cb[word][0]
        else:
            return 0
    
    def getCountwordNCb(self,word):
        if word in self.ncb:
            return self.ncb[word][0]
        else:
            return 0
    
    #We will apply Laplace Smoothing (Add-1)
    #So that the probability will never be 0
    def estimateWord(self,word,cls,countWord):
        count = 0
        if cls.lower() == "cb":
            count = self.getCountClickbait()+countWord
            return (self.getCountwordCb(word)+1)/(count)
        elif cls.lower() == "ncb":
            count = self.getCountNonClickbait()
            return (self.getCountwordNCb(word)+1)/(count)
    
    def predict(self,title,cls):
        title = re.split(r'[^\w]',title)
        dicc = {}
        for i in range(len(title)):
            if title[i]!='' and title[i]!=' ':
                if title[i].lower() in dicc:
                    dicc[title[i].lower()]+=1
                else:
                    dicc[title[i].lower()]=1
        
        #NOW LET THE PREDICTION BEGIN
        tmp = list(dicc)
        predik = 1
        """
        predik = priorCB * eachword probabilites times by how many times 
                            it occurs
        """
        if cls == "cb":
            for i in range(len(tmp)):
                if tmp[i] in self.cb:
                    predik = predik * (self.cb[tmp[i]][1] ** dicc[tmp[i]])
                else:
                    estimation = (0+1)/(self.getCountClickbait()+1000)
                    predik = predik * (estimation ** dicc[tmp[i]])
        if cls == "ncb":
            for i in range(len(tmp)):
                if tmp[i] in self.ncb:
                    predik = predik * (self.ncb[tmp[i]][1] ** dicc[tmp[i]])
                else:
                    estimation = (0+1)/(self.getCountNonClickbait()+1000)
                    predik = predik * (estimation**dicc[tmp[i]])
        return predik


# In[3]:


#Ok first of all lets put the file here
okezone_data = pd.read_csv("annotated_okezone.csv")
fimela_data = pd.read_csv("annotated_fimela.csv")

okezone_data


# In[4]:


# Jadi ada data seperti diatas
# Ada 1500 title dimana masing masingnya memiliki kelas tersendiri
# Dari data tersebut akan di ekstrak unique wordsnya
# dimana unique words tersebut akan dibatasi menjadi 1000 kata saja


# In[5]:


"""
So this part is where we get the vocabularies or Unique words

I declare 2 dictionaries
Frequent Word as Clickbait
and 
Frequent Word as nonClickbait

With this 2 dictionaries we can calculate
their probabilities based on how many times
it shows up

Also we can get the P(Cj) here where
P(Cb) = total clickbait title
P(NCb) = total non-clickbait title

"""
f = StopWordRemoverFactory()
sW = f.create_stop_word_remover()

PCb = 0
PNCb = 0
frequentWord_CB = {}
frequentWord_NCB = {}
for i in range (len(okezone_data["title"])):
    tmp = sW.remove(okezone_data["title"][i])
    tmp = re.split(r'[^\w]',tmp)
    if okezone_data['label_score'][i] == 1:
        PCb += 1
        for j in range (len(tmp)):
            if tmp[j] != '' and tmp[j] != ' ':
                if tmp[j].lower() in frequentWord_CB:
                    frequentWord_CB[tmp[j].lower()][0]+=1
                else:
                    frequentWord_CB[tmp[j].lower()]=[1]
    else:
        PNCb += 1
        for j in range (len(tmp)):
            if tmp[j] != '' and tmp[j] != ' ':
                if tmp[j].lower() in frequentWord_NCB:
                    frequentWord_NCB[tmp[j].lower()][0]+=1
                else:
                    frequentWord_NCB[tmp[j].lower()]=[1]
                    
# Di bagian ini terdapat 2 hal yang terjadi
# 1. Penghilangan stopwords
# 2. Ekstrak kata dari kalimat yang telah dihilangkan stopwordsnya

# PCb dan PNCb disini akan menjadi priors untuk kelas kedepannya
# PCb untuk Clickbait
# PNCb untuk Non-Clickbait

# ada 2 perulangan dimana terdapat 2 pointer yaitu
# bagian Title dan per kata di titlenya

# karena dari fungsi regex terdapat '' apabila kalimatnya 
# berlebih spasi, maka perlu dibersihkan terlebih dahulu

# tentu saja kita menggunakan lowercase dengan tujuan agar 
# meningkatkan akurasinya

# if elsenya hanya untuk menentukan apakah title tersebut masuk ke
# Click bait atau tidak, dan menambahkannya ke dictionary yang telah
# di deklarasikan di awal untuk menyimpan datanya

# Kenapa valuenya memakai list? karena ingin memberi ruang lebih untuk
# conditional probability kedepannya


# In[6]:


#Now we sort the frequent words
frequentWord_CB = dict(sorted(frequentWord_CB.items(),key = lambda x: x[1],reverse=True))
frequentWord_NCB = dict(sorted(frequentWord_NCB.items(),key = lambda x: x[1],reverse=True))

#Now we limit the frequent words to get Most Frequent Words
frequentWord_CB = dict(itertools.islice(frequentWord_CB.items(),1000))
frequentWord_NCB = dict(itertools.islice(frequentWord_NCB.items(),1000))

mn.field_names = ["Word","Count"]
for key, value in frequentWord_CB.items():
    mn.add_row([key,value])
print (mn)
print ("\n\nAnd this is non-Clickbait")
mn.clear()
mn.field_names = ["Word","Count"]
for key, value in frequentWord_NCB.items():
    mn.add_row([key,value])
print (mn)

# Di bagian ini program akan mengurutkan data yang
# ada di dictionary berdasarkan kemunculan
# masing masing kata. Semakin sering muncul
# maka akan menjadi paling atas.

# Karena data yang terbentuk cukup banyak, 
# data dibatasi menjadi 1000 data saja dimana
# saya menggunakan itertools untuk 'memotong'
# dictionarynya agar tersisa 1000 data saja

# Dapat dilihat di bawah hasil dari dictionarynya


# In[7]:


naiveBayes = NB(frequentWord_CB,frequentWord_NCB)
"""
So P(Cj) in this case will be
P(Cb) and P(NCb)

Added add-1 laplace smoothing so it wont return 0 at any point
P(W|Cj) = count(W|Cj) + 1 / (count(C) + |V|)

Count(C) will be naiveBayes.getCountClickbait or naiveBayes.getCountNonClickbait
count(W|Cj) will be naiveBayes.getCountWordCb or naiveBayes.getCountwordNCb
WordsTotal will be |V| or total of Unique word

why WordsTotal = 1000? Because we limit the most frequent unique words to 1000
"""
WordsTotal = 1000
# P(Cj) has been declared above, so we're going to
# estimate each word P(w|cj)
PriorCB = PCb/(PCb+PNCb)
PriorNCB = PNCb/(PCb+PNCb)


# In[8]:


"""
Now we're going to estimate each word conditional probabilities
By using the function we've declared
P(W|C) = count(W|C) + 1 / (count(C) + |V|)
And we stored each word probabilities inside the dictionary itself
"""
tmp = list(frequentWord_CB.items())   # This is to get the word itself
tmp2 = list(frequentWord_NCB.items()) # This is to get the word itself

#Looping to get the estimation
#of each words where the words 
#have their own conditional probabilities

for i in range (1000):
    word = tmp[i][0]
    prob = naiveBayes.estimateWord(word,"CB",1000)
    frequentWord_CB[word].append(prob)
    word = tmp2[i][0]
    prob = naiveBayes.estimateWord(word,"NCB",1000)
    frequentWord_NCB[word].append(prob)
    
#Delete some variables to free up some memories 
#because we dont need them anymore
del word,prob,tmp,tmp2

mn.clear()
mn.field_names = ["Word","Count","Probability"]
for key,value in frequentWord_CB.items():
    mn.add_row([key,frequentWord_CB[key][0],frequentWord_CB[key][1]])
print (mn)
print ("\n\nAnd this is non-Clickbait")
mn.clear()
mn.field_names = ["Word","Count","Probability"]
for key,value in frequentWord_NCB.items():
    mn.add_row([key,frequentWord_NCB[key][0],frequentWord_NCB[key][1]])
print (mn)

# Dua bagian diatas merupakan proses mencari Prior untuk masing masing kelas
# dan Words total merupakan total unique words yang telah di set 
# Setelah itu kita menghitung estimasi perkata dari tiap kelas
# dan di masukkan kedalam dictionary awal.

# Hasilnya dapat dilihat dibawah ini


# In[9]:


#THIS IS THE BEGINNING OF TESTING PHASE


# In[10]:


fimela={}
for i in range(len(fimela_data)):
    pepecebe = (naiveBayes.predict(fimela_data["title"][i],"cb"))*PriorCB
    pepencebe = (naiveBayes.predict(fimela_data["title"][i],"ncb"))*PriorNCB
    label = 1 if pepecebe > pepencebe else 0
    fimela[fimela_data["title"][i]] = label


# In[11]:


#Accuracy?
count = 0
tmp = list(fimela.values())
for i in range(len(fimela_data)):
    if tmp[i] == fimela_data["label_score"][i]:
        count += 1
acc = count/len(fimela_data)*100
acc = round(acc,4)

print ("\nTerpantau akurasi nya: %s Persen" % acc)

zc = list(fimela.keys())
zx = list(fimela_data["label_score"])
mn.clear()
mn.field_names = ["Title","Prediction","Original"]
for i in range(len(fimela_data)):
    t = zc[i][:50]+"..."
    mn.add_row([t,tmp[i],zx[i]])
print (mn)

del zc,t

# INI ADALAH AWAL MULAI DARI TESTING PHASE

# 2 Bagian diatas merupakan bagian proses penghitungan probability
# untuk kemungkinan kelas dari test data 'fimela'. Setelah menemukan probability
# masing masingnya dengan rumus
# P(Wi|Class) = count(Wi|Class)+1 / (Count(Class) + |V|)
# Dimana :
# |V| adalah total unique words
# Count(Wi|Class) adalah kemunculan suatu kata dalam kelas tersebut
# Count(Class) adalah total kemunculan semua kata dalam kelas tersebut
# Kenapa +1 ? +1 adalah bagian dari Laplace Smoothing
# Dimana berfungsi untuk mencegah terjadinya atau munculnya probabilitas 0

# Lalu berapakah akurasi dari program ini dalam menentukan kelas?

# Berikut adalah hasil prediksinya secara visualnya
# 1 = Clickbait
# 0 = non-Clickbait


# In[12]:


"""
This is an evaluation
of Fimela_data.csv
where we've done 
the prediction

Now we're going to find
the Confusion Matrix itself

There're 4 things

True Positive  = Predicted and Real is 1
False Positive = Predicted 1 but Real 0
True Negative  = Predicted and Real is 0
False Negative = Predicted 0 but Real 1

"""
class evaluation:
    def __init__(self,real,predict):
        self.r = real
        self.p = predict
        self.TP,self.FP,self.TN,self.FN = 0,0,0,0
        
        for i in range (len(self.r)):
            if self.r[i] == 1 and self.r[i] == self.p[i]:
                self.TP += 1
            elif self.r[i] == 0 and self.r[i] == self.p[i]:
                self.TN += 1
            elif self.r[i] == 0 and self.p[i] == 1:
                self.FP += 1
            else:
                self.FN += 1
                
    def getTP(self):
        return self.TP
    
    def getTN(self):
        return self.TN
    
    def getFP(self):
        return self.FP
    
    def getFN(self):
        return self.FN


# In[13]:


print ("""INI ADALAH AWAL MULA DARI EVALUATION PHASE
Pada tahapan ini kita mengevaluasi berdasarkan confusion matrix
dan mengamati presisi,recall,f1, dan akurasi dari hasil prediksi
yang telah kita peroleh

Berikut adalah hasil dari confusion matrix yang telah dibuat untuk kelas Clickbait""")

evl = evaluation(zx,tmp)
A = evl.getTP()
B = evl.getTN()
C = evl.getFP()
D = evl.getFN()
E = A/(A+C)
F = A/(A+D)
G = (A+B)/(A+B+C+D)
H = (2*E*F)/(E+F)
#Make the confusion matrix
mn.clear()
mn.field_names = [" ","True","False"]
mn.add_row(["Positive",A,C])
mn.add_row(["Negative",D,B])
print (mn)
print ("""Precision Acquired:\t %s
Recall Acquired:\t %s
Accuracy Acquired:\t %s
F1 Acquired:\t\t %s
""" % (E,F,G,H))

A2 = B
B2 = A
C2 = D
D2 = C
E2 = A2/(A2+C2)
F2 = A2/(A2+D2)
G2 = (A2+B2)/(A2+B2+C2+D2)
H2 = (2*E2*F2)/(E2+F2)
Makro = (G+G2)/2

print ("""Berikut adalah confusion matrix untuk kelas non clickbait
Dimana 
True Positive  = Predicted and Real is 0
False Positive = Predicted 0 but Real 1
True Negative  = Predicted and Real is 1
False Negative = Predicted 1 but Real 0
""")
mn.clear()
mn.field_names = [" ","True","False"]
mn.add_row(["Positive",A2,C2])
mn.add_row(["Negative",D2,B2])
print (mn)

print ("""Precision Acquired:\t %s
Recall Acquired:\t %s
Accuracy Acquired:\t %s
F1 Acquired:\t\t %s

Sehingga akurasi untuk MACRO-AVERAGING adalah
Accuracy : %s""" % (E2,F2,G2,H2,Makro))


# In[14]:


#FOR MICRO-AVERAGING
A3 = A+A2
B3 = B+B2
C3 = C+C2
D3 = D+D2
E3 = A3/(A3+C3)
F3 = A3/(A3+D3)
G3 = (A3+B3)/(A3+B3+C3+D3)
H3 = (2*E3*F3)/(E3+F3)
mn.clear()
mn.field_names = [" ","True","False"]
mn.add_row(["Positive",A3,C3])
mn.add_row(["Negative",D3,B3])
print ("""Bagian ini adalah bagian Micro-Averaging
Di micro-averaging, ke 4 kriteria yaitu
True Positive
False Positive
True Negative
False Negative
akan ditambahkan dari sebuah confusion matrix yang 
merupakan hasil penjumlahan dari ke 2 confusion matrix
yang berasal dari 2 kelas sebelumnya yaitu
Clickbait dan Non-Clickbait

After the processing: 
Precision Acquired:\t %s
Recall Acquired:\t %s
Accuracy Acquired:\t %s
F1 Acquired:\t\t %s
""" % (E3,F3,G3,H3))
print(mn)


# In[15]:


# Yohankristian 
# 18/424200/PA/18305

# Analisis dari hasil program :
# Dapat dilihat bahwa dari ke 3 fase yang telah dilaksanakan
# diperoleh beberapa hasil 

# Dalam fase pertama yaitu tahap learning, dimana kata" dari
# title yang terdapat pada .csv di ekstrak dan dihitung kemunculannya
# serta dikelompokkan berdasarkan kelas nya masing masing

# Pada fase ke 2 diperoleh akurasi 61.429% walau StopWords telah di hilangkan
# dan kumpulan kata telah dibersihkan. Karena hanya terbatas 1000 
# unique words saja, dan beberapa kata yang tidak seimbang di salah satu kelas
# dapat membuat akurasinya menjadi seperti itu.

# Pada fase ke 3 yaitu tahap evaluasi, kita dapat melihat perbandingan dari
# True Positive, True Negative, False Positive, False Negative dimana
# False Positivenya cenderung masih banyak.

# True Positive  = Predicted and Real is 1
# False Positive = Predicted 1 but Real 0
# True Negative  = Predicted and Real is 0
# False Negative = Predicted 0 but Real 1

# Diperoleh presisi, recall, akurasi, dan F1 yang bagus untuk kelas clickbait
# sedangkan untuk kelas non-clickbait dapat dilihat bahwa presisi, recall, dan f1
# kurang baik. hal ini lagi lagi disebabkan karena keterbatasan dalam hal training
# data dimana data yang telah ditraining tersebut timpang sebelah.

# Oleh karena itu, hasil hasil yang telah didapatkan tersebut masih dapat 
# ditingkatkan lagi dengan cara menambah data-data dalam training agar 
# dapat meningkatkan presisi, recall, akurasi, dan f1 agar mencapai tingkat
# dimana prediksi dapat tepat sasaran

