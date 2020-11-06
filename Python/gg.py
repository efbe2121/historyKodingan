#for python 3 or above use import tkinter instead Tkinter

from tkinter import all
import math

root = Tk()
#Declare besar windowsnya dulu

root.geometry("800x800")

fram = Frame(root)
#           BAGIAN UNTUK MEMPERMANIS TAMPILAN                   #
#################################################################
Label(fram,text="Point1: ").pack(side=LEFT)                     #
func=Entry(fram,width=3)                                        # -> Get user input
func2=Entry(fram,width=3)                                       # -> Get user input  
Label(fram,text="X:").pack(side=LEFT)                           #
func.pack(side=LEFT,fill=BOTH)                                  #
Label(fram,text="Y: ").pack(side=LEFT)                          #
func2.pack(side=LEFT,fill=BOTH)                                 #
#################################################################
Label(fram,text="Point2: ").pack(side=LEFT)                     #
func3=Entry(fram,width=3)                                       # -> Get user input
func4=Entry(fram,width=3)                                       # -> Get user input
Label(fram,text="X:").pack(side=LEFT)                           #   
func3.pack(side=LEFT,fill=BOTH)                                 #
Label(fram,text="Y: ").pack(side=LEFT)                          #   
func4.pack(side=LEFT,fill=BOTH)                                 #
#################################################################
Label(fram,text="Point3: ").pack(side=LEFT)                     #
func5=Entry(fram,width=3)                                       # -> Get user input
func6=Entry(fram,width=3)                                       # -> Get user input      
Label(fram,text="X:").pack(side=LEFT)                           #
func5.pack(side=LEFT,fill=BOTH)                                 #
Label(fram,text="Y: ").pack(side=LEFT)                          #
func6.pack(side=LEFT,fill=BOTH)                                 #
#################################################################
Label(fram,text="Point1 Sumbu Refleksi: ").pack(side=LEFT)      #
func7=Entry(fram,width=3)                                       # -> Get user input
func8=Entry(fram,width=3)                                       # -> Get user input
Label(fram,text="X:").pack(side=LEFT)                           #
func7.pack(side=LEFT,fill=BOTH)                                 #
Label(fram,text="Y: ").pack(side=LEFT)                          #
func8.pack(side=LEFT,fill=BOTH)                                 #
#################################################################
Label(fram,text="Point2 Sumbu Refleksi: ").pack(side=LEFT)      # 
func9=Entry(fram,width=3)                                       # -> Get user input
func0=Entry(fram,width=3)                                       # -> Get user input
Label(fram,text="X:").pack(side=LEFT)                           #
func9.pack(side=LEFT,fill=BOTH)                                 #
Label(fram,text="Y: ").pack(side=LEFT)                          #
func0.pack(side=LEFT,fill=BOTH)                                 #
#################################################################
Label(fram,text="   ").pack(side=LEFT)                          #
butt2 = Button(fram,text="Exit!")                               #
butt2.pack(side=RIGHT)                                          #   
Label(fram,text="   ").pack(side=LEFT)                          #
butt = Button(fram,text="Draw!")                                #
butt.pack(side=RIGHT)                                           #
fram.pack(side=TOP)                                             #
#################################################################
Label(root,text="OUTPUTnya : ",width=960,height=2,bg="grey",fg="black").pack(side=TOP)

c = Canvas(root)
c.pack(side=TOP, fill=BOTH, expand=1)

#Windows to ViewPort transformation
def Xv(x):
    x = 320 + (x*40)
    return x

def Yv(y):
    y = 320 - (y*40)
    return y
#Membuat garis Sumbu X dan Y

def sumbu():
    sb_x=c.create_line(0,320,640,320)
    sb_y=c.create_line(320,0,320,640)

#MAKE X point
def xPoint():
    i=-8
    sbx=0
    dx=640/16
    while sbx<=640:
        c.create_text(sbx,320,font="Times 10 bold",text=i)
        i += 1
        sbx += dx
    
#MAKE Y point
def yPoint():
    i=-8
    sby=0
    dy=640/16
    while sby<=640:
        c.create_text(320,sby,font="Times 10 bold",text=(-i))
        i += 1
        sby += dy

sumbu()
xPoint()
yPoint()

#MAKE THE TRIANGLE FIRST!
def triangle():
    p1x = func.get()
    p1x = int(p1x)
    p1y = func2.get()
    p1y = int(p1y)
    p2x = func3.get()
    p2x = int(p2x)
    p2y = func4.get()
    p2y = int(p2y)
    p3x = func5.get()
    p3x = int(p3x)
    p3y = func6.get()
    p3y = int(p3y)
    coord =[Xv(p1x),Yv(p1y),Xv(p2x),Yv(p2y),Xv(p3x),Yv(p3y),Xv(p1x),Yv(p1y)]
    c.create_line(*coord,fill="green")
    
def gambar():
    c.delete("all")
    sumbu()
    xPoint()
    yPoint()
    triangle()
    garissumbu()
    refleksi()

def garissumbu():
    sb1x=func7.get()
    sb1y=func8.get()
    sb2x=func9.get()
    sb2y=func0.get()
    sb1x = int(sb1x)
    sb1y = int(sb1y)
    sb2x = int(sb2x)
    sb2y = int(sb2y)
    c.create_line(Xv(sb1x),Yv(sb1y),Xv(sb2x),Yv(sb2y), fill = "red")

def refleksi():
    sb1x=func7.get()
    sb1y=func8.get()
    sb2x=func9.get()
    sb2y=func0.get()
    sb1x = int(sb1x)
    sb1y = int(sb1y)
    sb2x = int(sb2x)
    sb2y = int(sb2y)
    #Determine the equation first Ax + By + C = 0
    A = sb2y - sb1y
    B = -(sb2x - sb1x)
    C = -A * sb1x - B * sb1y
    M = math.sqrt(A*A + B*B)
    As = A/M
    Bs = B/M
    Cs = C/M
    #Get the equation A'x + B'y + C' = 0
    #Then get the value of my point
    p1x = func.get()
    p1x = int(p1x)
    p1y = func2.get()
    p1y = int(p1y)
    p2x = func3.get()
    p2x = int(p2x)
    p2y = func4.get()
    p2y = int(p2y)
    p3x = func5.get()
    p3x = int(p3x)
    p3y = func6.get()
    p3y = int(p3y)
    #Then the distance
    D1 = As * p1x + Bs * p1y + Cs
    D2 = As * p2x + Bs * p2y + Cs
    D3 = As * p3x + Bs * p3y + Cs
    #Then get the mirror point
    p1xr = p1x - 2 * As * D1
    p1yr = p1y - 2 * Bs * D1
    p2xr = p2x - 2 * As * D2
    p2yr = p2y - 2 * Bs * D2
    p3xr = p3x - 2 * As * D3
    p3yr = p3y - 2 * Bs * D3
    #Then draw the reflection
    coord =[Xv(p1xr),Yv(p1yr),Xv(p2xr),Yv(p2yr),Xv(p3xr),Yv(p3yr),Xv(p1xr),Yv(p1yr)]
    c.create_line(*coord,fill="blue")

butt.config(command=gambar)
butt2.config(command=root.destroy)
root.mainloop()
