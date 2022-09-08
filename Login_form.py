from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk  # pip install pillow
from tkinter import messagebox
import mysql.connector

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1540x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\users\Dell\oneDrive\Desktop\login_form\images\imgonline-com-ua-resize-L3aV9ZaDYM8EP.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        
        frame=Frame(self.root,bg="white")
        frame.place(x=510,y=170,width=340,height=450)
        
        img1=Image.open(r"C:\users\Dell\oneDrive\Desktop\login_form\images\download.jpg")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=635,y=175,width=100,height=100)

        

        get_str=Label(frame,text="Welcome",font=("times new roman",14,"bold"),fg="#24A19C",bg="white")
        get_str.place(x=135,y=100)

        get_str1=Label(frame,text="Donation Management System",font=("times new roman",14,"bold"),fg="#24A19C",bg="white")
        get_str1.place(x=50,y=120)


        #===============Label=====================
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="#24A19C",bg="white")
        username.place(x=75,y=155)
        
        #
        self.txtpass1_var=StringVar()
        self.txtuser1_var=StringVar()
        self.txtuser=ttk.Entry(frame,textvariable=self.txtuser1_var,font=("times new roman",15,"bold"))
        self.txtuser.place(x=45,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="#24A19C",bg="white")
        password.place(x=75,y=225)

        self.txtpass=tkinter.Entry(frame,show='*',textvariable=self.txtpass1_var,font=("times new roman",15,"bold"))
        self.txtpass.place(x=45,y=250,width=270)
        #self.var_pass=StringVar()
        self.var_check1=IntVar(value=0)
        
        #================ CheckBox ===================
        check1=Checkbutton(frame,command=self.showpassword1,text="Show Password",font=("times new roman",9,"bold"),bg="white",fg="#24A19C",variable=self.var_check1,onvalue=1,offvalue=0,activeforeground="white",activebackground="#24A19C")
        check1.place(x=40,y=270)

        #=============    icon image   -====================
        
        img2=Image.open(r"C:\users\Dell\oneDrive\Desktop\login_form\images\download.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=555,y=323,width=25,height=25)

                # for password
 
        img3=Image.open(r"C:\users\Dell\oneDrive\Desktop\login_form\images\password.png")
        img3=img3.resize((35,35),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=556,y=392,width=25,height=25)

                 #login Button
        loginbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#24A19C",activeforeground="white",activebackground="gray")
        loginbtn.place(x=110,y=312,width=120,height=35)

                 # Text
        newsignup_str=Label(frame,text="or",font=("times new roman",15,"bold"),fg="#24A19C",bg="white")
        newsignup_str.place(x=157,y=350)

                 #Register
        registerbtn=Button(frame,text="Sign Up",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="#24A19C",bg="white",activeforeground="white",activebackground="#24A19C")
        registerbtn.place(x=110,y=378,width=120,height=35)

                 #forgot password
        forgotbtn=Button(frame,command=self.forgot_password_window,text="Forgot Password?",font=("times new roman",9,"bold"),borderwidth=0,fg="#24A19C",bg="white",activeforeground="white",activebackground="#24A19C")
        forgotbtn.place(x=190,y=288,width=160)
                 
                 #admin 
        adminbtn=Button(frame,command=self.admin_window,text="Login To Admin",font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="#24A19C",activeforeground="white",activebackground="#24A19C")
        adminbtn.place(x=10,y=400,width=120,height=35)
    def register_window(self):
        self.new_window=Toplevel(self.root) 
        self.app=Login_window_s(self.new_window)
    def admin_window(self):
        self.new_window=Toplevel(self.root) 
        self.app=Admin_window(self.new_window)

    def showpassword1(self):
        if self.var_check1.get()==1:
            self.txtpass.config(show='')
        else:
            self.txtpass.config(show='*')

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","Please fill all the details")
        elif self.txtuser.get()=="suhail" and self.txtpass.get()=="1234":
            messagebox.showinfo("Success","Success")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="suhail",database="loginform")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.txtuser.get(),
                                                                                    self.txtpass.get()
                                                                       ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invaild Username & Password")
            else:
                open_main=messagebox.askyesno("Yes/No","Acess Only Admain")
                if open_main>0:
                    self.new_window1=Toplevel(self.root)
                    self.app=Donation(self.new_window1)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()
            self.txtuser1_var.set(""),
            self.txtpass1_var.set("")
    #============================Reset Password=====================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("error","Selecct Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("error","Please enter the answer",parent=self.root2)
        elif self.txt_newpassword.get()=="":
            messagebox.showerror("error","please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="suhail",database="loginform")
            my_cursor=conn.cursor()
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,vlaue)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.txt_newpassword.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Passoword has been reset. please login with new password",parent=self.root2)
                self.root2.destroy()






    #==================================frogot password==================
    def  forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("error","Please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="suhail",database="loginform")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)
            if row==None:
                messagebox.showerror("error","Please enter valid usename")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",15,"bold"),fg="#24A19C",bg="white")
                l.place(x=0,y=10,relwidth=1)


                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",13,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)
                #==================Combo box===============
                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",13,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your Friend Name","Your Pet Name")
                self.combo_security_Q.place(x=50,y=110,width=200)
                self.combo_security_Q.current(0)



                security_A=Label(self.root2,text="Security Answer:-",font=("times new roman",13,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",13,"bold"))
                self.txt_security.place(x=50,y=180,width=200)
                
                new_password=Label(self.root2,text="New Password:-",font=("times new roman",13,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpassword=ttk.Entry(self.root2,font=("times new roman",13,"bold"))
                self.txt_newpassword.place(x=50,y=250,width=200)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times new roman",12,"bold"),fg="white",bg="#24A19C")
                btn.place(x=50,y=290)
# ================================================ register================================================
class Login_window_s:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1540x800+0+0")

        #================ Variable ==============================
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        #checkvariable
        self.var_check=IntVar()

        #================ BackGround Image======================== 
        self.bg=ImageTk.PhotoImage(file=r"C:\users\Dell\oneDrive\Desktop\login_form\images\imgonline-com-ua-resize-vBjDwqUvmCY0clX.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        #================= Left BackGround Image===================
        self.bg1=ImageTk.PhotoImage(file=r"C:\users\Dell\oneDrive\Desktop\login_form\images\imgonline-com-ua-resize-I6KtXjqpFp.png")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=370,height=550)

        

        # ================ frame right=============================
        frame=Frame(self.root,bg="white")
        frame.place(x=420,y=100,width=800,height=550)

        # ============Label Inside matter==========================
        register_lbl=Label(frame,text="   ─────────────     SignUp Here     ──────────────────",font=("monotype corsiva",20,"bold"),fg="#FFAD60",bg="white")
        register_lbl.place(x=20,y=20)

        #===========Label and entry Field ============Row 1============
        fname=Label(frame,text="First Name:-",font=("times new roman",13,"bold"),bg="white",fg="#24A19C")
        fname.place(x=101,y=100)
        
        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",13,"bold"))
        self.fname_entry.place(x=105,y=130,width=200)
        
        lname=Label(frame,text="Last Name:-",font=("times new roman",13,"bold"),bg="white",fg="#24A19C")
        lname.place(x=420,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",13,"bold"))
        self.txt_lname.place(x=420,y=130,width=200)

        #===================Row 2==================

        contact_1=Label(frame,text="Contact No:-",font=("times new roman",13,"bold"),bg="white",fg="#24A19C")
        contact_1.place(x=101,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",13,"bold"))
        self.txt_contact.place(x=105,y=200,width=200)

        email=Label(frame,text="Email:-",font=("times new roman",13,"bold"),bg="white",fg="#24A19C")
        email.place(x=420,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",13,"bold"))
        self.txt_email.place(x=420,y=200,width=200)

        #==================Row 3===================

        security_Q=Label(frame,text="Select Security Question",font=("times new roman",13,"bold"),bg="white",fg="#24A19C")
        security_Q.place(x=101,y=240)
        #==================Combo box===============
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",13,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your Friend Name","Your Pet Name")
        self.combo_security_Q.place(x=105,y=270,width=200)
        self.combo_security_Q.current(0)



        security_A=Label(frame,text="Security Answer:-",font=("times new roman",13,"bold"),bg="white",fg="#24A19C")
        security_A.place(x=420,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",13,"bold"))
        self.txt_security.place(x=420,y=270,width=200)

        #=================Row 4====================

        pswd=Label(frame,text="Password:-",font=("times new roman",13,"bold"),bg="white",fg="#24A19C")
        pswd.place(x=101,y=310)

        self.txt_pswd=ttk.Entry(frame,show='*',textvariable=self.var_pass,font=("times new roman",13,"bold"))
        self.txt_pswd.place(x=105,y=340,width=200)

        confirm_pswd=Label(frame,text="Confirm Password:-",font=("times new roman",13,"bold"),bg="white",fg="#24A19C")
        confirm_pswd.place(x=420,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",13,"bold"))
        self.txt_confirm_pswd.place(x=420,y=340,width=200)

        #================Check Button====================

        checkbtn=Checkbutton(frame,variable=self.var_check,text="I have read and agree to the Terms & Conditions",font=("times new roman",13,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=101,y=390)
         
        self.var_check=IntVar(value=0)
        
        #================ CheckBox for showpassword  ===================
        check=Checkbutton(frame,command=self.showpassword,text="Show Password",font=("times new roman",9,"bold"),bg="white",fg="#24A19C",variable=self.var_check,onvalue=1,offvalue=0,activeforeground="white",activebackground="#24A19C")
        check.place(x=101,y=370)
        #====================Buttons=====================

        #img=Image.open(r"C:\users\Dell\oneDrive\Desktop\login_form\images\login.png")
        #img=img.resize((200,50),Image.ANTIALIAS)
        #self.photoimage=ImageTk.PhotoImage(img)
        #b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="white")
        #b1.place(x=10,y=420,width=300)

        #img1=Image.open(r"C:\users\Dell\oneDrive\Desktop\login_form\images\register.png")
        #img1=img1.resize((200,50),Image.ANTIALIAS)
        #self.photoimage1=ImageTk.PhotoImage(img1)
        #b1=Button(frame,command=self.register_data,image=self.photoimage1,borderwidth=0,cursor="hand2",font=("times new roman",15,"bold"),bg="white")
        #b1.place(x=330,y=420,width=300)
        
        loginbtn=Button(frame,text="Login",command=self.login1,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#24A19C",activeforeground="white",activebackground="#24A19C")
        loginbtn.place(x=101,y=420,width=120,height=35)

        registerbtn=Button(frame,command=self.register_data,text="Sign Up",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#24A19C",activeforeground="white",activebackground="#24A19C")
        registerbtn.place(x=420,y=420,width=120,height=35)

        


    def showpassword(self):
        if self.var_check.get()==1:
            self.txt_pswd.config(show='')
        else:
            self.txt_pswd.config(show='*')
        #================== Fuction Delecartion ==========
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All field are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our Terms and Conditions")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="suhail",database="loginform")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already exists,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                          
                                                                                          self.var_fname.get(),
                                                                                          self.var_lname.get(),
                                                                                          self.var_contact.get(),
                                                                                          self.var_email.get(),
                                                                                          self.var_securityQ.get(),
                                                                                          self.var_securityA.get(),
                                                                                          self.var_pass.get()
                                                                                      ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfull")
    def login1(self):
        #self.new_window=Toplevel(self.root)
        #self.app=Login_window(self.new_window)
        self.root.destroy()
#======================================== Admin Window ==============================================================



class Admin_window:
    def __init__(self,root):
        self.root1=root
        self.root1.title("Login")
        self.root1.geometry("1540x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\users\Dell\oneDrive\Desktop\login_form\images\imgonline-com-ua-resize-L3aV9ZaDYM8EP.png")
        lbl_bg=Label(self.root1,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        
        frame=Frame(self.root1,bg="white")
        frame.place(x=510,y=170,width=340,height=450)
        
        img11=Image.open(r"C:\users\Dell\oneDrive\Desktop\login_form\images\download.jpg")
        img11=img11.resize((100,100),Image.ANTIALIAS)
        self.photoimage11=ImageTk.PhotoImage(img11)
        lblimg11=Label(image=self.photoimage11,bg="black",borderwidth=0)
        lblimg11.place(x=635,y=175,width=100,height=100)

        

        get_str1=Label(frame,text="Welcome",font=("times new roman",14,"bold"),fg="#24A19C",bg="white")
        get_str1.place(x=135,y=100)

        get_str11=Label(frame,text="Donation Management System",font=("times new roman",14,"bold"),fg="#24A19C",bg="white")
        get_str11.place(x=50,y=120)


        #===============Label=====================
        username1=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="#24A19C",bg="white")
        username1.place(x=75,y=155)

        self.txtuser1=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser1.place(x=45,y=180,width=270)

        password1=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="#24A19C",bg="white")
        password1.place(x=75,y=225)

        self.txtpass1=tkinter.Entry(frame,show='*',font=("times new roman",15,"bold"))
        self.txtpass1.place(x=45,y=250,width=270)
        #self.var_pass=StringVar()
        self.var_check11=IntVar(value=0)
        
        #================ CheckBox ===================
        check11=Checkbutton(frame,command=self.showpassword11,text="Show Password",font=("times new roman",9,"bold"),bg="white",fg="#24A19C",variable=self.var_check11,onvalue=1,offvalue=0,activeforeground="white",activebackground="#24A19C")
        check11.place(x=40,y=270)

        #=============    icon image   -====================
        
        img12=Image.open(r"C:\users\Dell\oneDrive\Desktop\login_form\images\download.png")
        img12=img12.resize((25,25),Image.ANTIALIAS)
        self.photoimage12=ImageTk.PhotoImage(img12)
        lblimg12=Label(image=self.photoimage12,bg="black",borderwidth=0)
        lblimg12.place(x=555,y=323,width=25,height=25)

                # for password
 
        img13=Image.open(r"C:\users\Dell\oneDrive\Desktop\login_form\images\password.png")
        img13=img13.resize((35,35),Image.ANTIALIAS)
        self.photoimage13=ImageTk.PhotoImage(img13)
        lblimg13=Label(image=self.photoimage13,bg="black",borderwidth=0)
        lblimg13.place(x=556,y=392,width=25,height=25)

                 #login Button
        loginbtn1=Button(frame,text="Login",command=self.login11,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="#24A19C",activeforeground="white",activebackground="gray")
        loginbtn1.place(x=110,y=312,width=120,height=35)

                 # Text
        newsignup1_str=Label(frame,text="or",font=("times new roman",15,"bold"),fg="#24A19C",bg="white")
        newsignup1_str.place(x=157,y=350)

                 #Register
        registerbtn1=Button(frame,text="Sign Up",font=("times new roman",10,"bold"),borderwidth=0,fg="#24A19C",bg="white",activeforeground="white",activebackground="#24A19C")
        registerbtn1.place(x=110,y=378,width=120,height=35)

                 #forgot password
        forgotbtn1=Button(frame,text="Forgot Password?",font=("times new roman",9,"bold"),borderwidth=0,fg="#24A19C",bg="white",activeforeground="white",activebackground="#24A19C")
        forgotbtn1.place(x=190,y=288,width=160)

        adminbtn1=Button(frame,command=self.lo_window,text="Back to Login Page",font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="#24A19C",activeforeground="white",activebackground="#24A19C")
        adminbtn1.place(x=10,y=400,width=120,height=35)

    def lo_window(self):
        self.new_window=Toplevel(self.root1) 
        self.app=Login_window(self.new_window) 
     
    def showpassword11(self):
        if self.var_check11.get()==1:
            self.txtpass1.config(show='')
        else:
            self.txtpass1.config(show='*')

    def login11(self):
        if self.txtuser1.get()=="" or self.txtpass1.get()=="":
            messagebox.showerror("Error","Please fill all the details")
        elif self.txtuser.get()=="suhail" and self.txtpass.get()=="1234":
            messagebox.showinfo("Success","Success")
        else:
            messagebox.showinfo("Error","Please Check whelther Username and Password are incorrect")


# =================     Donation            ==============================================================================================
class Donation:
    def __init__(self,root):
        self.root=root
        self.root.title("Donation management System")
        self.root.geometry("1540x800+0+0")



        #================================Add Med Variable===========================
        self.Addmed_var=StringVar()
        self.RefMed_var=StringVar()

        #=================================Main Table Variable=======================
        self.Ref_var=StringVar()
        self.Cmp_var=StringVar()
        self.Typemed_var=StringVar()
        self.Medname_var=StringVar()
        self.lot_var=StringVar()
        self.issuedate_var=StringVar()
        self.expdate_var=StringVar()
        self.uses_var=StringVar()
        self.sideefect_var=StringVar()
        self.waring_var=StringVar()
        self.dosage_var=StringVar()
        self.price_var=StringVar()
        self.product_var=StringVar()



        lbltitle=Label(self.root,text=" Donation Management System",bd=15,relief=RIDGE
                             ,bg='white',fg="darkgreen",font=("times new roman",50,"bold"),padx=2,pady=4)

        lbltitle.pack(side=TOP,fill=X)


        #==================================DataFrame================================
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1360,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Donar Information",
                          fg="dark Green",font=("times new roman",12,"bold"))
        DataFrameLeft.place(x=0,y=5,width=900,height=350)

        
        
        #===================================ButtonFrame=======================================
        
        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1360,height=65)

        #========================================Main Button===================================
        btnAddData=Button(ButtonFrame,command=self.add_data,text="Medicine Add",font=("times new roman",12,"bold"),bg="darkgreen",fg="white")
        btnAddData.grid(row=0,column=0)

        btnUpdateMed=Button(ButtonFrame,command=self.Update_data,text="UPDATE",font=("times new roman",12,"bold"),width=14,bg="darkgreen",fg="white")
        btnUpdateMed.grid(row=0,column=1)

        btnDeleteMed=Button(ButtonFrame,command=self.delete_data,text="DELETE",font=("times new roman",12,"bold"),width=14,bg="darkgreen",fg="white")
        btnDeleteMed.grid(row=0,column=2)

        btnRestMed=Button(ButtonFrame,command=self.reset_data,text="RESET",font=("times new roman",12,"bold"),width=14,bg="darkgreen",fg="white")
        btnRestMed.grid(row=0,column=3)

        btnExitMed=Button(ButtonFrame,command=self.iExit,text="EXIT",font=("times new roman",12,"bold"),width=14,bg="darkgreen",fg="white")
        btnExitMed.grid(row=0,column=4)

        #==================Search by=================
        lblSerach=Label(ButtonFrame,font=("arial",12,"bold"),text="Search by",padx=2,bg="Red",fg="White")
        lblSerach.grid(row=0,column=5,sticky=W)

        # varaible
        self.search_var=StringVar()
        search_combo=ttk.Combobox(ButtonFrame,textvariable=self.search_var,width=12,font=("arial",13,"bold"),state="readonly")
        search_combo["values"]=("Ref_no","Medname","lotno")
        search_combo.grid(row=0,column=6)
        search_combo.current(0)
        
        self.searchTxt_var=StringVar()
        txtSearch=Entry(ButtonFrame,textvariable=self.searchTxt_var,bd=3,relief=RIDGE,width=12,font=("times new roman",12,"bold"))
        txtSearch.grid(row=0,column=7)

        Btnsearch=Button(ButtonFrame,command=self.serach_data,text="Search",font=("times new roman",12,"bold"),width=14,bg="darkgreen",fg="white")
        Btnsearch.grid(row=0,column=8)

        showAll=Button(ButtonFrame,command=self.fatch_data,text="Show All",font=("times new roman",12,"bold"),width=14,bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9)
 

        #====================================Label and Entry========================================

        lblrefno=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Reference No",padx=2)
        lblrefno.grid(row=0,column=0,sticky=W)
        

        conn=mysql.connector.connect(host='localhost',username='root',password='suhail',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute("select ref from pharma")
        row=my_cursor.fetchall()



        ref_combo=ttk.Combobox(DataFrameLeft,textvariable=self.Ref_var,width=14,font=("times new roman",13,"bold"),state="readonly")
        ref_combo["values"]=row
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)
        

        lblCmpName=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Company Name:",padx=2,pady=6)
        lblCmpName.grid(row=1,column=0,sticky=W)
        txtCmpName=Entry(DataFrameLeft,textvariable=self.Cmp_var,font=("times new roman",12,"bold"),bg="white",bd=2,relief=RIDGE,width=18)
        txtCmpName.grid(row=1,column=1)

        lblTypeofMedicine=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Type of Medicine:",padx=2,pady=6)
        lblTypeofMedicine.grid(row=2,column=0,sticky=W)

        comTypeofMedicine=ttk.Combobox(DataFrameLeft,textvariable=self.Typemed_var,width=16,font=("times new roman",11,"bold"),state="readonly")
        comTypeofMedicine["values"]=("Tablet","Liquid","Capusules","Topical medicines","Drops","Inhales","Injection")
        comTypeofMedicine.grid(row=2,column=1)
        comTypeofMedicine.current(0)

        #===============Add Medicine=========================
        lblMedicineName=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Medicine Name:",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)
           

        conn=mysql.connector.connect(host='localhost',username='root',password='suhail',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute("select Medname from pharma")
        row=my_cursor.fetchall()

        comMedicineName=ttk.Combobox(DataFrameLeft,textvariable=self.Medname_var,width=14,font=("times new roman",13,"bold"),state="readonly")
        comMedicineName["values"]=row
        comMedicineName.grid(row=3,column=1)
        comMedicineName.current(0)
        
        

        lblLotNo=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Lot No:",padx=2,pady=6)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,textvariable=self.lot_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=16)
        txtLotNo.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Issue Data:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,textvariable=self.issuedate_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=16)
        txtIssueDate.grid(row=5,column=1)

        lblIExDate=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Exp Data:",padx=2,pady=6)
        lblIExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataFrameLeft,textvariable=self.expdate_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=16)
        txtExDate.grid(row=6,column=1)

        #lblIExDate=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Exp Data:",padx=2,pady=6)
        #lblIExDate.grid(row=6,column=0,sticky=W)
        #txtExDate=Entry(DataFrameLeft,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=16)
        #txtExDate.grid(row=6,column=1)

        lblUses=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Uses:",padx=2,pady=4)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,textvariable=self.uses_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=16)
        txtUses.grid(row=7,column=1)
 
        lblSideEffect=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Side Effects:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,textvariable=self.sideefect_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=16)
        txtSideEffect.grid(row=8,column=1)

        lblPrecWarning=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="PrecWarning:",padx=2,pady=6)
        lblPrecWarning.grid(row=0,column=2,sticky=W)
        txtPrecWarning=Entry(DataFrameLeft,textvariable=self.waring_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=16)
        txtPrecWarning.grid(row=0,column=3)

        lblDosage=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Dosage:",padx=2,pady=6)
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,textvariable=self.dosage_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=16)
        txtDosage.grid(row=1,column=3)
        
        lblPrice=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Tablet Price:",padx=2,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,textvariable=self.price_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=16)
        txtPrice.grid(row=2,column=3)
        
        lblProductQt=Label(DataFrameLeft,font=("times new roman",12,"bold"),text="Product Qt:",padx=2,pady=6)
        lblProductQt.grid(row=3,column=2,sticky=W)
        txtProductQt=Entry(DataFrameLeft,textvariable=self.product_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=16)
        txtProductQt.grid(row=3,column=3,sticky=W)

        #lblDosage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effects:",padx=2,pady=6)
        #lblDosage.grid(row=8,column=0,sticky=W)
        #txtDosage=Entry(DataFrameLeft,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=12)
        #txtDosage.grid(row=8,column=1)
        
        #=================================images================================
        lblhome=Label(DataFrameLeft,font=("arial",12,"bold"),text="Stay Home stay safe",padx=15,pady=6,bg="White",fg="red",width=37)
        lblhome.place(x=410,y=140)

        #img2=Image.open("path ")
        #img2=img2.resize((150,135),Image.ANTIALIAS)
        #self.photoimg2=ImageTK.photoImage(img2)
        #b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        #b1.place(x=770,y=330)

        #img2=Image.open("path ")
        #img2=img2.resize((150,135),Image.ANTIALIAS)
        #self.photoimg2=ImageTK.photoImage(img2)
        #b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        #b1.place(x=770,y=330)

        #img2=Image.open("path ")
        #img2=img2.resize((150,135),Image.ANTIALIAS)
        #self.photoimg2=ImageTK.photoImage(img2)
        #b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        #b1.place(x=770,y=330)

        #=================================dataframeright===========================
        
        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Donar referal id",
                          fg="dark Green",font=("times new roman",12,"bold"))
        DataFrameRight.place(x=910,y=5,width=400,height=350)
        

        #img2=Image.open("path ")
        #img2=img2.resize((150,135),Image.ANTIALIAS)
        #self.photoimg2=ImageTK.photoImage(img2)
        #b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        #b1.place(x=770,y=330)
 
        #img2=Image.open("path ")
        #img2=img2.resize((150,135),Image.ANTIALIAS)
        #self.photoimg2=ImageTK.photoImage(img2)
        #b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        #b1.place(x=770,y=330)
        
        #img2=Image.open("path ")
        #img2=img2.resize((150,135),Image.ANTIALIAS)
        #self.photoimg2=ImageTK.photoImage(img2)
        #b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        #b1.place(x=770,y=330)
        
        lblrefno=Label(DataFrameRight,font=("times new roman",12,"bold"),text="Reference No:",padx=2,pady=6)
        lblrefno.place(x=0,y=80)
        txtrefno=Entry(DataFrameRight,textvariable=self.RefMed_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=16)
        txtrefno.place(x=125,y=80)

        lblMedicineName=Label(DataFrameRight,font=("times new roman",12,"bold"),text="MedicineName:",padx=2,pady=6)
        lblMedicineName.place(x=0,y=110)
        txtMedicineName=Entry(DataFrameRight,textvariable=self.Addmed_var,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=16)
        txtMedicineName.place(x=125,y=110)
         
        #====================================SideFrame==============================
        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="White",)
        side_frame.place(x=0,y=150,width=230,height=160)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,column=("Reg","Medname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("Reg",text="Reg")
        self.medicine_table.heading("Medname",text="Medname")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("Reg",width=100)
        self.medicine_table.column("Medname",width=100)
        
        self.medicine_table.bind("<ButtonRelease-1>",self.Medget_cursor)

        #==========================medicine add button================================
        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="Dark Green")
        down_frame.place(x=250,y=150,width=110,height=160)

        btnAddmed=Button(down_frame,command=self.AddMed,text="Add",font=("times new roman",12,"bold"),width=10,bg="lime",fg="white",pady=4)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,command=self.UpdateMed,text="Update",font=("times new roman",12,"bold"),width=10,bg="purple",fg="white",pady=4)
        btnUpdatemed.grid(row=1,column=0)


        btnDeletemed=Button(down_frame,command=self.DeleteMed,text="Delete",font=("times new roman",12,"bold"),width=10,bg="Red",fg="white",pady=4)
        btnDeletemed.grid(row=2,column=0)
        

        btnClearmed=Button(down_frame,command=self.ClearMed,text="Clear",font=("times new roman",12,"bold"),width=10,bg="orange",fg="white",pady=4)
        btnClearmed.grid(row=3,column=0)


        #================================Frame details===================================
        Framedeatils=Frame(self.root,bd=15,relief=RIDGE)
        Framedeatils.place(x=0,y=586,width=1500,height=150)


        #==================================Main table & scrollbar====================
        Table_frame=Frame(Framedeatils,bd=10,relief=RIDGE,padx=20)
        Table_frame.place(x=0,y=1,width=1390,height=120)

        scorll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scorll_x.pack(side=BOTTOM,fill=X)
        scorll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scorll_y.pack(side=RIGHT,fill=Y)
 
        self.pharmacy_table=ttk.Treeview(Table_frame,column=("Reg","companyname","type","tabletname","lotno","issuedate",
                                            "expdate","uses","sideeffect","warning","dosage","price","productqt")
                                            ,xscrollcommand=scorll_x.set,yscrollcommand=scorll_y.set)
        scorll_x.pack(side=BOTTOM,fill=X)
        scorll_y.pack(side=RIGHT,fill=Y)

        scorll_x.config(command=self.pharmacy_table.xview)
        scorll_y.config(command=self.pharmacy_table.yview)
 
        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("Reg",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type Of Medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Prec&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product Qts")
        self.pharmacy_table.pack(fill=BOTH,expand=1)

        self.pharmacy_table.column("Reg",width=100)
        self.pharmacy_table.column("companyname",width=100)
        self.pharmacy_table.column("type",width=100)
        self.pharmacy_table.column("tabletname",width=100)
        self.pharmacy_table.column("lotno",width=100)
        self.pharmacy_table.column("issuedate",width=100)
        self.pharmacy_table.column("expdate",width=100)
        self.pharmacy_table.column("uses",width=100)
        self.pharmacy_table.column("sideeffect",width=100)
        self.pharmacy_table.column("warning",width=100)
        self.pharmacy_table.column("dosage",width=100)
        self.pharmacy_table.column("price",width=100)
        self.pharmacy_table.column("productqt",width=100)
        self.pharmacy_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_dataMed()
        self.fatch_data()

    #==================================Add Medicine Funtionality Delclaration==================

    def AddMed(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='suhail',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",(
                
                                                                          self.RefMed_var.get(),
                                                                          self.Addmed_var.get(),
                                                                         ))
        conn.commit()
        self.fetch_dataMed()
        conn.close()
        messagebox.showinfo("Success","Medicine added")

    def fetch_dataMed(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='suhail',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharma")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #============================MedGetcusror================================
    def Medget_cursor(self,event=""):
        cursor_row=self.medicine_table.focus()
        content=self.medicine_table.item(cursor_row)
        row=content["values"]
        self.RefMed_var.set(row[0])
        self.Addmed_var.set(row[1])
    
    def UpdateMed(self):
        if self.RefMed_var.get()=="" or self.Addmed_var.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        else:
             conn=mysql.connector.connect(host='localhost',username='root',password='suhail',database='management')
             my_cursor=conn.cursor()
             my_cursor.execute("update pharma set MedName=%s where Ref=%s",(
                                                                                 self.Addmed_var.get(),
                                                                                 self.RefMed_var.get(),
                                                                                 ))            
             conn.commit()
             self.fetch_dataMed()
             conn.close()
             messagebox.showinfo("Success","Medicine has been Updated")
    def DeleteMed(self):
         conn=mysql.connector.connect(host='localhost',username='root',password='suhail',database='management')
         my_cursor=conn.cursor()
         
         sql="delete from pharma where Ref=%s"
         val=(self.RefMed_var.get(),)
         my_cursor.execute(sql,val)

         conn.commit()
         self.fetch_dataMed()
         conn.close()
         messagebox.showinfo("Success","Medicine has been Deleted")
    def ClearMed(self):
        self.RefMed_var.set("")
        self.Addmed_var.set("")
    
    #========================= Main table ===================================

    def add_data(self):
        if self.Ref_var.get()=="" or self.lot_var.get()=="":
            messagebox.showerror("Error","All Fields are required")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='suhail',database='management')
            my_cursor=conn.cursor()
            my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                         self.Ref_var.get(),
                                                                         self.Cmp_var.get(),
                                                                         self.Typemed_var.get(),
                                                                         self.Medname_var.get(),
                                                                         self.lot_var.get(),
                                                                         self.issuedate_var.get(),
                                                                         self.expdate_var.get(),
                                                                         self.uses_var.get(),
                                                                         self.sideefect_var.get(),
                                                                         self.waring_var.get(),
                                                                         self.dosage_var.get(),
                                                                         self.price_var.get(),
                                                                         self.product_var.get(),
                                                                         ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success","Data has be inserted")
    
    def fatch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='suhail',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    #========================================================
    def get_cursor(self,event=""):
        cursor_row=self.pharmacy_table.focus()
        content=self.pharmacy_table.item(cursor_row)
        row=content["values"]

        self.Ref_var.set(row[0]),
        self.Cmp_var.set(row[1]),
        self.Typemed_var.set(row[2]),
        self.Medname_var.set(row[3]),
        self.lot_var.set(row[4]),
        self.issuedate_var.set(row[5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideefect_var.set(row[8]),
        self.waring_var.set(row[9]),
        self.dosage_var.set(row[10]),
        self.price_var.set(row[11]),
        self.product_var.set(row[12])


    def Update_data(self):
        if self.Ref_var.get()=="":
            messagebox.showerror("Error","All Fields are Required")
        else:
            conn=mysql.connector.connect(host='localhost',username='root',password='suhail',database='management')
            my_cursor=conn.cursor()
            my_cursor.execute("update pharmacy set CmpName=%s,Typemed=%s,Medname=%s,Lotno=%s,issuedate=%s,expdata=%s,uses=%s,sideeffect=%s,waring=%s,dosage=%s,price=%s,product=%s where Ref_no=%s",(



                                                                                                                                                                                                          
                                                                                                                                                                                                          self.Cmp_var.get(),
                                                                                                                                                                                                          self.Typemed_var.get(),
                                                                                                                                                                                                          self.Medname_var.get(),
                                                                                                                                                                                                          self.lot_var.get(),
                                                                                                                                                                                                          self.issuedate_var.get(),
                                                                                                                                                                                                          self.expdate_var.get(),
                                                                                                                                                                                                          self.uses_var.get(),
                                                                                                                                                                                                          self.sideefect_var.get(),
                                                                                                                                                                                                          self.waring_var.get(),
                                                                                                                                                                                                          self.dosage_var.get(),
                                                                                                                                                                                                          self.price_var.get(),
                                                                                                                                                                                                          self.product_var.get(),
                                                                                                                                                                                                          self.Ref_var.get()
             
                                                                                                                                                                                                       ))            
            conn.commit()
            self.fatch_data() 
            conn.close()
            messagebox.showinfo("Updated","Data has been Updated")

    def delete_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='suhail',database='management')
        my_cursor=conn.cursor()
         
        sql="delete from pharmacy where Ref_no=%s"
        val=(self.Ref_var.get(),)
        my_cursor.execute(sql,val)

        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Success","Medicine has been Deleted")


    def reset_data(self):
        #self.Ref_var.set(row[0]),
        self.Cmp_var.set(""),
        #self.Typemed_var.set(row[2]),
        #self.Medname_var.set(row[3]),
        self.lot_var.set(""),
        self.issuedate_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.sideefect_var.set(""),
        self.waring_var.set(""),
        self.dosage_var.set(r""),
        self.price_var.set(r""),
        self.product_var.set(r"")

    def serach_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='suhail',database='management')
        my_cursor=conn.cursor()
        my_cursor.execute("select * from pharmacy where " +str(self.search_var.get())+" LIKE  '%"+str(self.searchTxt_var.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close() 


    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Donation Management System","Confirm if you want to exit")
        if iExit>0:
            main.destroy()
            return



if __name__ == "__main__":
    #root=Tk()
    #app=Login_window(root)
    main()

    
