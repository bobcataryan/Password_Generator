from tkinter import *
import random

root=Tk()
root.title("password guesser")
root.geometry("500x500")

input1=Entry(root)
label1=Label(root)
label2=Label(root)

array1=[["1","2","3","4","5","6","7","8","9","0"],["Red","Blue","Orange","Yellow","Green","Purple","Pink","Black","White"],["A",'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','Z']]
print(array1[2][9])



def createpassword() :
    response= input1.get()
    label1['text'] = "password guessed is " +response
    
    number=random.randint(0,9)
    number2=random.randint(0,8)
    number3=random.randint(0,25)
    
    charac1=array1[0][number]
    charac2=array1[1][number2]
    charac3=array1[2][number3]
    label2['text'] = "Generated password was " + charac1 + charac2 + charac3
    
   
    
btn=Button(root,text="check guess",command=createpassword)
input1.place(relx=0.5,rely=0.4,anchor=CENTER)
label1.place(relx=0.5,rely=0.5,anchor=CENTER)
btn.place(relx=0.5,rely=0.6,anchor=CENTER)
label2.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()