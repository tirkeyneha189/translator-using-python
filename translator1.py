from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk,ImageDraw,ImageFont
import mysql.connector
from tkinter import messagebox
from register import signup#NAVIGATE REGISTER ==
import tkinter as tk
from tkinter import filedialog
from language_work import seen
x=1
a=1
def trans():
    seen()

def show():
    t1=Toplevel()
    t1.geometry("1800x1800")
    t1.config(bg="navyblue")
    style = Style()
    style.configure('t.TButton', font =('descriptive', 10),foreground = 'black',background="black",bg="red")
    style.configure('s.TButton', font =('descriptive', 10),bd=0)
    style.configure('n.TButton', font =('times new roman', 18,"bold"))
    style.configure('v.TButton', font =('times new roman', 15),foreground="#00759E",activebackground = '#00759E')
    
    #===IMAGE SLLIDER====
    
    def slider():
        global x
        bg=Label(t1)
        img=Image.open("N"+str(x)+".png")
        x=x+1
        if x==10:
            x=1
        img=img.resize((1000,1000))
        img=ImageTk.PhotoImage(img)
        bg.config(image=img)
        bg.image=img
        bg.place(x=650,y=0)
        t1.after(1000,slider)
        #====new page open===
        def show3():
            signup()
            
        #===Bg image==
        t1.left=ImageTk.PhotoImage(file="Neha.jpg")
        
        left=Label(t1,image=t1.left).place(x=5,y=0)
        lb=Label(t1,text="LANGUAGE ",font=("Comic Sans MS",20,"bold"),foreground="white",background="#0072BB")
        lb.place(x=500,y=0)
        lc=Label(t1,text="TRANSLATOR",font=("Comic Sans MS",20,"bold"),foreground="white",background="#0072BB")
        lc.place(x=540,y=40)
        
        t1.right=ImageTk.PhotoImage(file="Neha2.jpg")
        right=Label(t1,image=t1.right).place(x=5,y=210,height=250)
        lf=Label(t1,text="Don't have an accounnt? ",font=("times new roman",12,"bold"),foreground="red",background="white")
        lf.place(x=180,y=435)
        
        
        #Register Frame
        frame1=Frame(t1)
        frame1.place(x=360,y=210,width=290,height=250)
        lf=Label(frame1,text="LOGIN HERE",font=("times new roman",18,"bold"),foreground = 'navyblue')
        lf.place(x=50,y=0)
        #===LABEL ON FRAME====
        user=Label(frame1,text="Username",font=("times new roman",15,"bold"),foreground = 'black')
        user.place(x=10,y=25)
        
        
        userbox=Entry(frame1,font=("times new roman",15),text="username")
        userbox.place(x=10,y=50)
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),foreground = 'black')
        password.place(x=10,y=80)
        passbox=Entry(frame1,font=("times new roman",15),text="password",show="*")
        passbox.place(x=10,y=105)
        #t1=Entry(frame1,text="hello")
        #t1.place(x=10,y=120)
        t1.btn=ImageTk.PhotoImage(file="login1.jpg")
        def log():
            p1=userbox.get()
            p2=passbox.get()
            print(p1)
            print(p2)
            conn=mysql.connector.connect(host="127.0.0.1",user="root",passwd="")
            db=conn.cursor()
            db.execute("use project")
            db.execute("select * from user_info where uname="+"'"+p1+"'"+" and pass="+"'"+p2+"'"+" ")
            res=db.fetchall()
            count=0
            for row in res:
                print(row)
                fname=row[0]
                lname=row[1]
                mobile=row[2]
                email=row[3]
                print("email=",email)
                pic=row[7]
                profile=Toplevel()
                profile.geometry("700x500")
                profile.title("profile")
                profile.config(bg="skyblue")
                profile.resizable(False,False)
                frame1=Frame(profile)
                frame1.place(x=30,y=50,width=290,height=400)
                lf=Label(frame1,text="PROFILE",font=("times new roman",18,"bold"),foreground = 'navyblue')
                lf.place(x=70,y=0)
                l1=Label(frame1,text="Your Name:"+fname +lname,font=("Copperplate Gothic Bold",10,"bold"),foreground='black')
                l1.place(x=30,y=190)
                l2=Label(frame1,text="Your Username:"+fname,font=("times new roman",10,"bold"),foreground='red')
                l2.place(x=43,y=210)
                l_el=Label(frame1,text="Your Email:"+email,font=("times new roman",10,"bold"),foreground='black')
                l_el.place(x=43,y=230)
                l_no=Label(frame1,text="Your Mobile Nomber:"+mobile,font=("times new roman",10,"bold"),foreground='black')
                l_no.place(x=43,y=250)

                
                img1=Image.open(pic)
                img1=img1.resize((120,90))
                img1=ImageTk.PhotoImage(img1)
                p=Label(frame1)
                p.config(image=img1)
                p.image=img1
                p.place(x=50,y=40)
                
                def upload():
                    file=filedialog.askopenfilename()
                    
                    if(file):
                        print(file)
                        
                    conn1=mysql.connector.connect(host="127.0.0.1",user="root",passwd="")
                    db1=conn.cursor()
                    db1.execute("use project")
                    db1.execute("update user_info set pic="+"'"+file+"'"+" where mobile="+"'"+mobile+"'"+"")
                    conn1.commit()
                    messagebox.showinfo("My Message Box","PROFILE PICTURE UPDATED!!!")
                    
                uploadimage=Button(frame1,text="upload photo",command=upload)
                
                uploadimage.place(x=50,y=150,width=150,height=40)
                def reset():
                    new_page=Toplevel()
                    new_page.geometry("500x500")
                    new_page .config(bg="#c2315c")
                    new_page.resizable(False,False)
                    
                    style = Style()
                    k=Label(new_page) 
                    img=Image.open("lockbg.png")
                    img=img.resize((400,400))
                    img=ImageTk.PhotoImage(img)
                    k.config(image=img)
                    k.image=img
                    k.place(x=50,y=50)
                    '''
                    upper_lbl=Label(k,background="white")
                    upper_lbl.place(x=240,y=200,width=350,height=400)
                    '''
                    title_for=Label(k,text="RESET PASSWORD",font=("Elephant",15,"bold"),background="#99c0e6")
                    title_for.place(x=80,y=10)
                                
                    new_password=Label(k,text=" Enter Old Password ",font=("Courier New",12,"bold"),foreground="#767171",background="#99c0e6")
                    new_password.place(x=90,y=130)
                    new_password_box=Entry(k,font=("times new roman",15))
                    new_password_box.place(x=80,y=160,width=250)

                    confirm_password=Label(k,text=" Enter New Password ",font=("Courier New",12,"bold"),foreground="#767171",background="#99c0e6")
                    confirm_password.place(x=90,y=190)
                    confirm_password_box=Entry(k,font=("times new roman",15))
                    confirm_password_box.place(x=80,y=230,width=250)
                    
                    confirmn_password=Label(k,text=" Enter Confirm Password ",font=("Courier New",12,"bold"),foreground="#767171",background="#99c0e6")
                    confirmn_password.place(x=90,y=260)
                    confirmn_password_box=Entry(k,font=("times new roman",15))
                    confirmn_password_box.place(x=80,y=290,width=250)
                    
                    
                    def upd():
                        s1=new_password_box.get()
                        s2= confirm_password_box.get()
                        print("old pass=",s2)
                        print("new pass=",s1)
                        conn11=mysql.connector.connect(host="127.0.0.1",user="root",passwd="")
                        db11=conn11.cursor()
                        db11.execute("use project")
                        db11.execute("update user_info set pass="+"'"+s2+"'"+" where pass="+"'"+s1+"'"+"")
                        conn11.commit()
                        messagebox.showinfo("My Message Box","PROFILE PASSWORD UPDATED!!!")
                            
                        
                        
                    style.configure('O.TButton', font =('descriptive', 10),foreground = 'black',background="black",bg="red")
                    btn_save=Button(new_page,text="SAVE",style = 'O.TButton',command=upd)
                    btn_save.place(x=130,y=380,width=250,height=35)
                    
                    
                    
                                    
                changepassword=Button(frame1,text="Change password",command=reset)
                changepassword.place(x=50,y=300,width=150,height=40)
            
                frame2=Frame(profile)
                frame2.place(x=340,y=15,width=350,height=470)
                lg=Label(frame2,text="Edit Profile",font=("times new roman",15,"bold","underline"),foreground = 'navyblue')
                lg.place(x=30,y=0)
                ln=Label(frame2,text="FISRT NAME")
                ln.place(x=30,y=40)
                tn=Entry(frame2)
                tn.place(x=120,y=40)
                tn.insert(0,fname)

                ln1=Label(frame2,text="LAST NAME")
                ln1.place(x=30,y=80)
                tn1=Entry(frame2)
                tn1.insert(0,lname)
                tn1.place(x=120,y=80)

                ln2=Label(frame2,text="MOBILE NO")
                ln2.place(x=30,y=120)
                tn2=Entry(frame2)
                tn2.insert(0,mobile)
                tn2.place(x=120,y=120)

                l52=Label(frame2,text="EMAIL")
                l52.place(x=35,y=160)
                tn3=Entry(frame2)
                tn3.insert(0,email)
                tn3.place(x=120,y=160)
                '''
                ln4=Label(frame2,text="")
                ln4.place(x=30,y=160)
                tn4=Entry(frame2)
                tn4.place(x=120,y=160)
                frame3=Frame(frame2)
                frame3.place(x=20,y=250,width=300,height=150)
                '''
                        
                def slider():
                    global a
                    y=Label(frame3)
                    img=Image.open("T"+str(a)+".jpg")
                    a=a+1
                    if a==4:
                        a=1
                    img=img.resize((300,150))
                    img=ImageTk.PhotoImage(img)
                    y.config(image=img)
                    y.image=img
                    y.place(x=0,y=0)
                    frame3.after(1000,slider)
                slider()
                
                
                
                
                
                btnimage=Button(frame2,text="Update Profile",style='v.TButton')
                btnimage.place(x=15,y=200,width=320,height=50)
                
                btn_trans=Button(frame2,text="Continue",style = 'n.TButton',command=trans)
                btn_trans.place(x=15,y=405,width=320,height=45)
                
                count=count+1
            if count==0:
                messagebox.showinfo("My Message Box"," Invalid LOGIN !!!")
            

        btnimage=Button(frame1,image=t1.btn,command=log)
        btnimage.place(x=10,y=150,width=265,height=70)
        txtbox2=Button(t1,text="Sign Up",style = 'n.TButton',command=signup)
        txtbox2.place(x=190,y=402)
        def forget():
            new_t=Toplevel()
            new_t.geometry("500x480")
            new_t.config(bg="navyblue")
            new_t.title("forget")
            new_t.resizable(False,False)
            style = Style()
            style.configure('q.TButton', font =('times new roman', 10,"bold"),foreground="Black",activeforeground = '#00759E',bd=0)
            o=Label(new_t) 
            img=Image.open("lockb.jpeg")
            img=img.resize((500,480))
            img=ImageTk.PhotoImage(img)
            o.config(image=img)
            o.image=img
            o.place(x=0,y=0)
            
            
            
            
            title_forget=Label(o,text=" FORGET PASSWORD ",font=("Courier New",13,"bold"),foreground="black")
            title_forget.place(x=260,y=65)
            
            
            mobile_no=Label(o,text="Enter Register Mobile ",font=("Courier New",9,"bold"),foreground="black",background="white")
            mobile_no.place(x=270,y=200)
            mobile_no_box=Entry(o,font=("times new roman",9),text="Mobile")
            mobile_no_box.place(x=260,y=220,width=170)
            
            new_password=Label(o,text=" Enter New Password ",font=("Courier New",9,"bold"),foreground="BLACK",background="white")
            new_password.place(x=270,y=250)
            new_password_box=Entry(o,font=("times new roman",9))
            new_password_box.place(x=260,y=270,width=170)
            
            def change():
                if mobile_no_box.get() =='' or new_password_box.get() =='':
                    messagebox.showerror('Error','All entry fields must be entered')
                    return
                
                else:
                    s1=mobile_no_box.get()
                    s2=new_password_box.get()
                    print("new password=",s2)
                    print("mobile=",s1)
                    conn11=mysql.connector.connect(host="127.0.0.1",user="root",passwd="")
                    db11=conn11.cursor()
                    db11.execute("use project")
                    db11.execute("update user_info set pass="+"'"+s2+"'"+" where mobile="+"'"+s1+"'"+"")
                    conn11.commit()
                    messagebox.showinfo("My Message Box","YOUR PASSWORD SUCCESSFULLY RESET !!")
                    def login_new():
                        new_t.destroy()
                        retnew_t.destroy()
            
            
            submit=Button(o,text="RESET PASSWORD",style = 'q.TButton',command=change)
            submit.place(x=275,y=305) 

            
  
        
        forget_password=Button(frame1,text="Forget password",command=forget)
        forget_password.place(x=10,y=219,width=265,height=30)
        
        
            
    slider()#CALL SLIDER FUNCTION===
    t1.mainloop()
   
    

    







    
    
