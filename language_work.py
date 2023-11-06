from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk,ImageDraw,ImageFont
import mysql.connector
from tkinter import messagebox
import googletrans
import tkinter as tk
from googletrans import Translator
from tkinter import messagebox

x=1
a=1
def seen():
    root=Toplevel()
    root.geometry("1800x1800")
    root.config(bg="skyblue")
    root.title("neha")
    style = Style()
    style.configure('p.TButton',relief=RIDGE,boarderwidth=2,font=("verdana",12,"bold"),bg="khaki",activebackground="black",cursor="hand2")
    style.configure('s.TButton', font =('descriptive', 10),bd=0)

       
    def translate():
        lang_1=text_entry1.get("1.0","end-1c")
        cl=right_combo_box.get()

        if lang_1=='':
            messagebox.showerror('Language Translator','Enter the text to translate!')
        else:
            text_entry2.delete(1.0,'end')
            translator = Translator()
            output = translator.translate(lang_1,dest=cl)
            
            text_entry2.insert('end',output.text)
            
    def clear():
        text_entry1.delete(1.0,'end')
        text_entry2.delete(1.0,'end')
    lang_lbl=Label(root,text="LANGUAGE ",font=("Comic Sans MS",20,"bold"),background="skyblue")
    lang_lbl.place(x=800,y=10)
    trans_lbl=Label(root,text="TRANSLATOR",font=("Comic Sans MS",20,"bold"),background="skyblue")
    trans_lbl.place(x=840,y=50)
    frame_left=Frame(root,width=600,height=370,relief=RIDGE,borderwidth=5)
    frame_left.place(x=100,y=100)
    left_label=Label(frame_left,background="black",relief=RIDGE)
    left_label.place(x=0,y=0,width=590,height=355)
    text_entry1=Text(left_label,width=450,height=255,borderwidth=5,relief=RIDGE,font=("verdana",15),bg="khaki")
    text_entry1.place(x=0,y=0)
    left_btn=Button(root,command=translate,text="Translate",style='p.TButton')
    left_btn.place(x=350,y=480,width=100,height=40)
    
    language=googletrans.LANGUAGES
    languageV=list(language.values())
    lang1=language.keys()
    
    left_combo_box=Combobox(root,values=languageV,font=("times new roman",18),state='readonly',justify=CENTER)
    left_combo_box.place(x=100,y=50,width=600,height=40)
    left_combo_box.current(0)

    left_scrool_bar=Scrollbar(left_label)
    left_scrool_bar.pack(side="right",fill="y")
    
    frame_right=Frame(root,width=600,height=370,relief=RIDGE,borderwidth=5)
    frame_right.place(x=850,y=300)
    right_label=Label(frame_right,background="black")
    right_label.place(x=0,y=0,width=590,height=355)
    text_entry2=Text(right_label,width=500,height=150,borderwidth=5,relief=RIDGE,font=("verdana",15),bg="khaki")
    text_entry2.place(x=0,y=0)
    right_btn=Button(root,text="Clear",style='p.TButton',command=clear)
    right_btn.place(x=1100,y=680,width=100,height=40)
    
    language=googletrans.LANGUAGES
    languageU=list(language.values())
    lang2=language.keys()
    right_combo_box=Combobox(root,values=languageU,font=("times new roman",18),state='readonly',justify=CENTER)
    
    right_combo_box.place(x=850,y=250,width=600,height=40)
    right_combo_box.current(0)
        
    right_scrool_bar=Scrollbar(right_label)
    right_scrool_bar.pack(side="right",fill="y")

    
        



