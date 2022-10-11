from tkinter import ttk
from ttkthemes import ThemedStyle
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import pickle as p
import hashlib
import os

#Creating A Tk
root=Tk()
login_page=ttk.Frame(root)
root.call('lappend', 'auto_path', r'C:\Python\Lib\site-packages\ttkthemes\themes\awthemes-9.5.0')
root.call('package', 'require', 'awdark')
style=ttk.Style()
style.theme_use('awdark')
root.title("AutoCar Sales")

open_eye=ImageTk.PhotoImage(Image.open(r"icons\show_password.png").resize((30,30*(643//388)),resample=0))
close_eye=ImageTk.PhotoImage(Image.open(r"icons\hide_password.png").resize((30,30*(643//388)),resample=0))
#Setting window icon
root.iconbitmap("autocar_logo.ico")

#Setting dimensions of window and postioning it at the centre
login_page_width=500
login_page_height=300
screen_width=login_page.winfo_screenwidth()
screen_height=login_page.winfo_screenheight()
x=(screen_width/2) - (login_page_width/2)
y=(screen_height/2) - (login_page_height/2)

#Making the Window resizeable
root.geometry(f"{login_page_width}x{login_page_height}+{int(x)}+{int(y)}")
root.resizable(width=False,height=False)

#By default the password field hides the characters inputed by the user for added security
pass_view_status=False
#Storing the pasword inside a variable as StringVar
user_name=StringVar(login_page)
password=StringVar(login_page)
def view_pass(e):
    global pass_view_status
    if pass_view_status==False:
        pass_view_status=True
        password_field.config(show="")
        view_passwd_button.config(image=open_eye)
    else:
        pass_view_status = False
        password_field.config(show="*")
        view_passwd_button.config(image=close_eye)

    




def login():
    pass_flag=False #to check whether the password is valid
    user_flag=False #to check whether the username is present in database
    name=user_name.get()
    pwd=password.get()
    pwd = hashlib.md5(pwd.encode())
    pwd = pwd.hexdigest()
    fin=open('users.txt','rb')
    d=p.load(fin)
    if name in d:
        user_flag=True
        if d[name]==pwd:
            pass_flag=True
        else:
             pass_flag=False

    fin.close()
    if user_flag==True and pass_flag==True:
        messagebox.showinfo('..:::Login','Login Successful')
        root.destroy()
        os.system("Main_menu.py")
    elif user_flag==False:
        messagebox.showinfo("Access Denied","User does not exist")
    elif pass_flag==False:
        messagebox.showinfo("Access Denied","Invalid password")
        

                    
#Creating labels and buttons for login page
login_Label=ttk.Label(login_page,text="\tAutocar Sales\t",anchor=CENTER,font=("Times New Roman",20),width=30)
user_id_Label = ttk.Label(login_page,text="Username:",font=('DM Sans',18))
user_id_field= ttk.Entry(login_page,textvariable=user_name,font=('Calibri 18'))
password_Label = ttk.Label(login_page,text="Password:",font=('Arial',18))
password_field = ttk.Entry(login_page,textvariable=password,show="*",font=('Calibri 18'))
submit_button=ttk.Button(login_page,text="Login",command=login,takefocus=False)
view_passwd_button=Label(login_page,image=close_eye,bd = 0,takefocus=False)
view_passwd_button.bind("<Button-1>",view_pass)

#Placing labels and buttons ,progressbar
login_page.pack(fill=BOTH,expand=1)
login_Label.grid(columnspan=3)
user_id_Label.grid(row=1,column=0,pady=10,sticky="E")
user_id_field.grid(row=1,column=1,pady=20)
user_id_field.focus_set()
password_Label.grid(row=2,column=0,pady=10,sticky="E")
password_field.grid(row=2,column=1,pady=20)
view_passwd_button.grid(row=2,column=2,pady=20)
submit_button.grid(row=3,column=0,padx=30)

#Inserting sample useraname and password
user_id_field.insert(0,"Kevin")
password_field.insert(0,"ironman")

root.mainloop()







