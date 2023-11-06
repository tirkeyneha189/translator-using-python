from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk
from language_login import show

t=Tk()


def go1():
    show()
t.title("LANGUAGE TRANSLATOR!")

t.geometry("1800x1800")
t.config(bg="skyblue")
style = Style()
style.configure('W.TButton', font =('calibri', 20, 'bold',),foreground = 'GREEN',background="RED")
p=Label(t)
#BG=IMAGE=====
img=Image.open("world.jpg")
img=img.resize((1000,1000))
img=ImageTk.PhotoImage(img)
p.config(image=img)
p.image=img
p.place(x=0,y=0)
b=Button(t,text="Click on me!!",style = 'W.TButton',command=go1)
b.place(x=500,y=700)
b1=Button(t,text=" No Thanks !",style = 'W.TButton',command=t.destroy)
b1.pack()
b1.place(x=1200,y=700)
l1=Label(t,text="LANGUAGE ",font=("Comic Sans MS",20,"bold"))
l1.place(x=600,y=10)
l2=Label(t,text="TRANSLATOR",font=("Comic Sans MS",20,"bold"))
l2.place(x=640,y=50)
l3=Label(t,text="Hii!!I'm Language Translator !!",font=("Bodoni MT Black",20,"bold"),foreground = 'RED',background="skyblue")
l3.place(x=1030,y=50)
l4=Label(t,text="I Help You Connect With People !!",font=("Bodoni MT Black",20,"bold"),foreground = 'RED',background="SKYBLUE")
l4.place(x=1030,y=80)

l5=Label(t,text="language translator refers to any",font=("Algerian",15,"bold"),foreground = 'coral',background="skyBLUE")
l5.place(x=1030,y=140)
l6=Label(t,text="application that support human ",font=("Algerian",15,"bold"),foreground = 'coral',background="skyblue")
l6.place(x=1030,y=170)
l7=Label(t,text="translators throughout the ",font=("Algerian",15,"bold"),foreground = 'coral',background="SKYBLUE")
l7.place(x=1030,y=200)
l8=Label(t,text="process of transferring text",font=("Algerian",15,"bold"),foreground = 'coral',background="skyBLUE")
l8.place(x=1030,y=230)
l15=Label(t,text="from any",font=("Algerian",15,"bold"),foreground = 'white',background="skyBLUE")
l15.place(x=1030,y=260)
l9=Label(t,text="language to",font=("Algerian",15,"bold"),foreground = 'navyblue',background="skyblue")
l9.place(x=1150,y=260)
l10=Label(t,text="another.this",font=("Algerian",15,"bold"),foreground = 'white',background="SKYBLUE")
l10.place(x=1310,y=260)
l11=Label(t,text="translator ",font=("Algerian",15,"bold"),foreground = 'white',background="skyBLUE")
l11.place(x=1030,y=290)
l12=Label(t,text="will be",font=("Algerian",15,"bold"),foreground = 'navyblue',background="skyblue")
l12.place(x=1180,y=290)
l13=Label(t,text="helpful for people",font=("Algerian",15,"bold"),foreground = 'white',background="SKYBLUE")
l13.place(x=1270,y=290)
l14=Label(t,text="to have a ",font=("Algerian",15,"bold"),foreground = 'white',background="skyBLUE")
l14.place(x=1030,y=320)
l16=Label(t,text="understand ",font=("Algerian",15,"bold"),foreground = 'navyblue',background="skyBLUE")
l16.place(x=1160,y=320)
l17=Label(t,text="in many different",font=("Algerian",15,"bold"),foreground = 'white',background="skyBLUE")
l17.place(x=1300,y=320)
l18=Label(t,text="language  ",font=("Algerian",15,"bold"),foreground = 'white',background="skyBLUE")
l18.place(x=1030,y=350)
l19=Label(t,text="which will benefit",font=("Algerian",15,"bold"),foreground = 'navyblue',background="skyBLUE")
l19.place(x=1150,y=350)
l20=Label(t,text="in people life.",font=("Algerian",15,"bold"),foreground = 'white',background="skyBLUE")
l20.place(x=1370,y=350)
l21=Label(t,text="a person will be able to connct with",font=("Algerian",15,"bold"),foreground = 'green',background="skyblue")
l21.place(x=1030,y=380)
l22=Label(t,text="people on a more effective level throught",font=("Algerian",15,"bold"),foreground = 'green',background="skyBLUE")
l22.place(x=1030,y=410)
l23=Label(t,text="the power of this language translator.",font=("Algerian",15,"bold"),foreground = 'green',background="skyBLUE")
l23.place(x=1030,y=440)
l24=Label(t,text="translator is very useful in our life.",font=("Algerian",15,"bold"),foreground = 'green',background="skyBLUE")
l24.place(x=1030,y=480)
t.mainloop()









