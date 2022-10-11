from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
import mysql.connector as ms
from datetime import date
from ttkthemes import ThemedStyle
import os
import time
import pdf_generator
from PIL import Image,ImageTk

#Establishing Python-Sql connection via mysql connector
mydb=ms.connect(host='localhost',user='root',passwd='student',db='projectdb')
#Creating cursor object
c=mydb.cursor()

root=Tk()
root.title("AutoCar Sales and Inventory")
root.iconbitmap('autocar_logo.ico')

#Settting dimensions of the window
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()

root.geometry("%dx%d+-10+0"%(screen_width,screen_height))
#Making the Window  non resizeable
root.resizable(False,False)

#Creating a noteboook
my_notebook=ttk.Notebook(root)
my_notebook.place(x=0,y=0,relwidth=1,relheight=1)

#Creating frames for the notebook
option1=ttk.Frame(my_notebook,width=screen_width,height=screen_height)
option2=ttk.Frame(my_notebook,width=screen_width,height=screen_height)
option3=ttk.Frame(my_notebook,width=screen_width,height=screen_height)
#Styling
# style1 = ThemedStyle()
# style1.set_theme("breeze")
style = ttk.Style(root)
root.call('lappend', 'auto_path', r'C:\Python\Lib\site-packages\ttkthemes\themes\awthemes-9.5.0')
root.call('package', 'require', 'awdark')
style.theme_use('awdark')
#Adding frames to my notebook
my_notebook.add(option1,text="Add Vehicle")
my_notebook.add(option2,text="Search")
my_notebook.add(option3,text="Invoice")
option1.focus_set()

def add_customer(b,m,v,co,res,p,tp):  
    popup_window=Toplevel(root)
    popup=ttk.Frame(popup_window)
    #popup_window.resizable(False,False)
    popup_width=300
    popup_height=408
    x=(screen_width/2)-(popup_width/2)
    y=(screen_height/2)-(popup_height/2)
    popup_window.geometry("%dx%d+%d+%d"%(popup_width,popup_height,int(x),int(y)))
    popup.place(x=0,y=0,relwidth=1,relheight=1)
    heading_customer = ttk.Label(popup,text = "CUSTOMER DETAILS")
    heading_customer.grid(row=0,column=1,rowspan = 2,columnspan=1,padx=10,pady=10,sticky="W")                  

    name_text = ttk.Label(popup,text = "NAME:")
    name_entry = ttk.Entry(popup)
    name_text.grid(row=2,column=0,padx=20,sticky="E")
    name_entry.grid(row=2,column=1,sticky="W",padx=10,pady=10,)

    phone_text = ttk.Label(popup,text = "PHONE NO:")
    phone_entry =ttk.Entry(popup)
    phone_text.grid(row=3,column=0,padx=20,sticky="E")
    phone_entry.grid(row=3,column=1,sticky="W",padx=10,pady=10,)

    email_text = ttk.Label(popup,text = "EMAIL:")
    email_entry =ttk.Entry(popup)
    email_text.grid(row=4,column=0,padx=20,sticky="E")
    email_entry.grid(row=4,column=1,sticky="W",padx=10,pady=10,)

    address_box=Frame(popup)
    address_text=ttk.Label(popup,text="ADDRESS:")
    address_entry=Text(address_box,width=20,height=3,bg='#191c1d',insertbackground='white')
    vbar=ttk.Scrollbar(address_box,command=address_entry.yview,orient="vertical")
    address_entry.configure(yscrollcommand=vbar.set) 
    address_entry.insert(INSERT,"")
    address_entry.configure(fg='white')
    address_text.grid(row=5,column=0)
    address_box.grid(row=5,column=1,sticky="W",padx=1,pady=1)
    address_entry.grid(row=0,column=0,sticky="NSEW")
    vbar.grid(row=0,column=1,sticky="NS") 

    heading_veicle_details = ttk.Label(popup,text = "VEHICLE DETAILS")
    heading_veicle_details.grid(row=6,column=1,rowspan = 1,columnspan=1,pady=10,sticky='we')   
     
    resval=IntVar(popup)
     
    car_brand_text = ttk.Label(popup,text = "Brand:")
    car_brand_text.grid(row=7,column=0,padx=20,sticky="E")
    car_brand_entry = ttk.Entry(popup)
    car_brand_entry.grid(row=7,column=1,sticky="W")
    car_brand_entry.insert(0,b)
    car_brand_entry.config(state="readonly")
    

    car_model_text=ttk.Label(popup,text = "Model:")
    car_model_text.grid(row=8,column=0,padx=20,sticky="E")
    car_model_entry=ttk.Entry(popup)
    car_model_entry.grid(row=8,column=1,sticky="W")
    car_model_entry.insert(0,m)
    car_model_entry.config(state="readonly")

    car_var_text=ttk.Label(popup,text="Variant:")
    car_var_text.grid(row=9,column=0,padx=20,sticky="E")
    car_var_entry=ttk.Entry(popup)
    car_var_entry.grid(row=9,column=1,sticky="W")
    car_var_entry.insert(0,v)
    car_var_entry.config(state="readonly")
    
    car_color_text= ttk.Label(popup,text = "Color:")
    car_color_text.grid(row=10,column=0,padx=20,sticky="E")                         
    car_color_entry =ttk.Entry(popup)
    car_color_entry.grid(row=10,column=1,sticky="W")
    car_color_entry.insert(0,co)
    car_color_entry.config(state="readonly")

    resale_value_text=ttk.Label(popup,text="Resale value:")
    resale_value_text.grid(row=11,column=0,sticky="E")
    resale_value_entry=ttk.Entry(popup,textvariable=resval)
    resale_value_entry.insert(0,res)
    resale_value_entry.grid(row=11,column=1,sticky="W")

    def submit():
        nm=name_entry.get().strip()
        ph=int(phone_entry.get().strip())
        em=email_entry.get().strip()
        ad=address_entry.get(1.0,END).strip()
        today=date.today()
        try:
            print("insert into customers(name,phone,email,addr,pur_date,plate,resval)values('%s','%s','%s','%s','%s','%s',%d)"%(nm,ph,em,ad,today,p,int(resval.get())))
            c.execute("insert into customers(name,phone,email,addr,pur_date,plate,resval) values('%s','%s','%s','%s','%s','%s',%d)"%(nm,ph,em,ad,today,p,int(resval.get())))
            c.execute("Update vehicles set AVAIL='sold' where plate='%s'"%(p))
            mydb.commit()
            c.execute("select INVNO from customers where plate='%s'"%p)
            invno=c.fetchone()
            messagebox.showinfo("Data Info",'Record Added Successfully!')
            invoice(nm,ph,em,ad,b,m,v,co,tp,p,resval.get(),today,invno)
            popup.destroy()
            my_notebook.select(2)
        except Exception as e:
            print(e)

    submit_button=ttk.Button(popup,text="SUBMIT",command=submit)
    submit_button.grid(row=12,column=1,sticky="W")
        
    
def add_vehicle():
    name=StringVar(option1)
    phone=StringVar(option1)
    email=StringVar(option1)
    name.set("")
    phone.set("")
    email.set("")
    global icon1
    icon1=Image.open(r'icons\owner_new.png')
    icon1=icon1.resize((30,30), resample = 0)
    icon1=ImageTk.PhotoImage(icon1)
    global icon2
    icon2=Image.open(r'icons\phone_new.png')
    icon2=icon2.resize((30,30), resample = 0)
    icon2=ImageTk.PhotoImage(icon2)
    global icon3
    icon3=Image.open(r'icons\mail_new.png')
    icon3=icon3.resize((50,30), resample = 0)
    icon3=ImageTk.PhotoImage(icon3)
    global icon4
    icon4=Image.open(r'icons\addr_new.png')
    icon4=icon4.resize((30,30), resample = 0)
    icon4=ImageTk.PhotoImage(icon4)

    heading_customer =ttk.Label(option1,text = "Previous Owner Details",font=("Times",20,"underline"))
    heading_customer.grid(row=0,column=1,rowspan = 2,columnspan=4,pady=10)

    name_text = ttk.Label(option1,text = "          Name:",image=icon1,compound=LEFT)
    name_entry = ttk.Entry(option1,textvariable=name,width=22)
    name_text.grid(row=2,column=0,padx=(200,0),pady=1)
    name_entry.grid(row=2,column=1)

    phone_text = ttk.Label(option1,text = "      Phone No.:",image=icon2,compound=LEFT)
    phone_entry = ttk.Entry(option1,textvariable=phone,width=22)
    phone_text.grid(row=2,column=2,pady=1,sticky="W")
    phone_entry.grid(row=2,column=3,sticky="W")

    email_text = ttk.Label(option1,text = "         E-mail:",image=icon3,compound=LEFT)
    email_entry = ttk.Entry(option1,textvariable=email,width=22)
    email_text.grid(row=3,column=0,padx=(200,0),pady=1)
    email_entry.grid(row=3,column=1)

    address_text = ttk.Label(option1,text = "       Address:",image=icon4,compound=LEFT)
    address_box=ttk.Frame(option1)
    address=Text(address_box,width=20,height=3,bg='#191c1d',insertbackground='white')
    vbar=ttk.Scrollbar(address_box,command=address.yview,orient="vertical")
    address.configure(yscrollcommand=vbar.set)
    address.grid(row=0,column=0,sticky='NSEW')
    vbar.grid(row=0,column=1,sticky="NS")
    address.insert(INSERT,"")
    address.configure(fg='white')
    address_text.grid(row=3,column=2,pady=1,sticky="W")
    address_box.grid(row=3,column=3,sticky="E",pady=20)
    
    heading_vehicle=ttk.Label(option1,text="Vehicle Details",font=("Times",20,"underline"))
    heading_vehicle.grid(row=4,column=1,columnspan=4,pady=10)
    
    #Values for dropdown boxes
    #'BRAND':{'MODEL':{'NAME':['VARIANT']}
    brands={
    
    'MARUTI SUZUKI':{'MODEL':{'ALTO':['LX','AX','LXI'],
    'ALT0 800':['LX','AX','LXI'],
    'SWIFT':['LXI','ZDI','LDI','VXI'],
    'SWIFT DEZIRE':['VX','VXI','LDI','VXI'],
    'WAGON R':['LXI','VXI','ZDX']}},
    'HONDA':
    {'MODEL':{'JAZZ':['1.2 ACTIVE|VTEC','1.2 BASE|VTEC'],
    'BRIO':['1.2 VX|VTEC','1.2 EX|VTEC','1.2 EM|VTEC'],
    'CITY':['VMT PETROL','VMT EXCLS','S MT PETROL'],
    'CIVIC':['1.8 VT','VX PETROL','ZX MT PETROL'],
    'AMAZE':['VMT PETROL','ZX MT PETROL','VMT EXCLS']}
    },
    'FORD':
    {'MODEL':{'FIGO':['1.4LX DURATORQ','1.4ZX DURATORQ','1.4LXI DURATORQ'],
    'CLASSIC':['1.4CLX DURATORQ','1.4ZX DURATORQ','1.4CLXI DURATORQ'],
    'ECOSPORT':['1.5 TITANIUM','1.5 ECOBOOST','1.5 TREND TI VCT'],
    'ENDEAVOUR':['2.5 4X2','2.5 4X2 AT','2.5 4X4'],
    'IKON':['FLAIR','ROCAM','SXI']}
    },
    'TATA':
    {'MODEL':{'TIAGO':['XM','XZ,X AT', '1.5 XZ'],
    'ALTROZ':['XE','XM','XT'],
    'NANO':['XT','CX','CX CNG'],
    'NEXON':['XMA 1.2','XMA 1.5','XE REVOTORQ'],
    'XENON XT':['DLE','EX 4X2','EX 4X4']}
    },
    'TOYOTA':
    {'MODEL':{'ETIOS':['CROSS 1.5','VD','VX'],
    'COROLLA':['LE','SE','H1.8 J'],
    'CAMRY':['W1 MT','W2 AT','W3 MT'],
    'INNNOVA':['2.0 GX 8','2.0 GX 7','2.0 VX 7'],
    'YARIS':['G CVT','J CVT','J MT']}
    }
    }
    
    
    years=['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
    states=['KL-KERALA','KA-KARNATAKA','TN-TAMIL NADU','GA-GOA','AP-ANDHRA PRADESH']



    #text variables for dropdown boxes
    brand=StringVar(option1)
    brand.set('')

    model=StringVar(option1)
    model.set('')

    yearb=StringVar(option1)

    variant=StringVar(option1)
    variant.set('')

    yearp=StringVar(option1)

    state=StringVar(option1)
    state.set('')

    price=StringVar(option1)

    color=StringVar(option1)
    color.set('')

    plate=StringVar(option1)
    plate.set('')

    trip=StringVar(option1)

    resval=StringVar(option1)

    def set_model():
        try:            #print(list(brands[brand.get()]['MODEL'].keys())) # to get list of models #print(brands[brand.get()]['MODEL'].keys())
            model.set("")
            set_variant()
            model_list['values']=list(brands[brand.get()]['MODEL'].keys())
        except:
            pass

    brand_text = ttk.Label(option1,text = "  Brand:")
    brand_text.grid(row=5,column=0,padx=(200,0),pady=1,sticky="E")
    brand_list = ttk.Combobox(option1,textvariable=brand,values=list(brands.keys()),state='readonly',postcommand=set_model)
    brand_list.grid(row=5,column=1,pady=(0,10))
    
    def set_variant():
        try:             #values=brands[brand.get()]['MODEL'][model.get()] #print(brands[brand.get()]['MODEL'][model.get()])
            variant.set('')
            variant_list['values']=brands[brand.get()]['MODEL'][model.get()]
        except:
            pass
        
    model_text = ttk.Label(option1,text = "         Model:")
    model_text.grid(row=5,column=2,pady=1,sticky="W")           
    
    model_list = ttk.Combobox(option1,textvariable=model,state='readonly',postcommand=set_model)
    model_list.grid(row=5,column=3,pady=(0,10))
   
    year_build_text=ttk.Label(option1,text="              Year of Build:")
    year_build_list=ttk.Combobox(option1,textvariable=yearb,state='readonly',values=years)
    year_build_text.grid(row=6,column=0,padx=(200,0),pady=1,sticky="E")
    year_build_list.grid(row=6,column=1,pady=(0,10))

    variant_text=ttk.Label(option1,text="          Variant:")
    variant_list=ttk.Combobox(option1,textvariable=variant,state='readonly',postcommand=set_variant)
    #print((brands[brand.get()][model.get()]))
    variant_text.grid(row=6,column=2,pady=1,sticky="W")
    variant_list.grid(row=6,column=3,pady=(0,10))

    year_pur_text=ttk.Label(option1,text="          Year of Purchase:")
    year_pur_entry=ttk.Entry(option1,textvariable=yearp,width=22)
    year_pur_text.grid(row=7,column=0,padx=(200,0),pady=1,sticky="E")
    year_pur_entry.grid(row=7,column=1,pady=(0,10)) 

    state_text=ttk.Label(option1,text = "          Regd State:")
    state_list=ttk.Combobox(option1,textvariable=state,state='readonly',values=states)
    state_text.grid(row=7,column=2,pady=1,sticky="W")
    state_list.grid(row=7,column=3,pady=(0,10))    

    price_text = ttk.Label(option1,text = "         Price:")
    price_entry = ttk.Entry(option1,textvariable=price,width=22)
    price_text.grid(row=8,column=0,padx=(200,0),pady=1,sticky="E")
    price_entry.grid(row=8,column=1,pady=(0,10))

    color_text = ttk.Label(option1,text = "         Color:")
    color_entry = ttk.Entry(option1,textvariable=color,width=22)
    color_text.grid(row=8,column=2,pady=1,sticky="W")
    color_entry.grid(row=8,column=3,pady=(0,10))

    license_plate_text = ttk.Label(option1,text ="     License Plate:")
    license_plate_entry = ttk.Entry(option1,textvariable=plate,width=22)
    license_plate_text.grid(row=9,column=0,padx=(200,0),pady=1,sticky="E")
    license_plate_entry.grid(row=9,column=1,pady=(0,10))

    km_driven_text = ttk.Label(option1,text = "         Km Driven:")
    km_driven_entry=Entry(option1)
    km_driven_entry = ttk.Entry(option1,textvariable=trip,width=22)
    km_driven_text.grid(row=9,column=2,pady=1,sticky="W")
    km_driven_entry.grid(row=9,column=3,pady=(0,10))

    resale_value_text=ttk.Label(option1,text="          Resale Value:")
    resale_value_entry=ttk.Entry(option1,textvariable=resval,width=22)
    resale_value_text.grid(row=10,column=0,padx=(200,0),pady=1,sticky="E")
    resale_value_entry.grid(row=10,column=1,pady=(0,10))


    #Validating entry Fields
    def validate_name(event):
        if len(name.get().strip())<=25:
           for i in name.get().strip():
                if i.isdigit():
                    messagebox.showerror('Invalid Name',"Enter Only Alphabets in Name Field")
                    name_entry.focus_set()
                    break
                elif i.isspace()==False and i.isalpha()==False:
                    messagebox.showerror('Invalid Name',"Enter Only Alphabets in Name Field")
                    name_entry.focus_set()
                    break
        else:
            messagebox.showerror('Error',"Entered Name is too long")
            name_entry.focus_set()

    def validate_phone(event):
        try:
            
            if len(phone.get().strip())!=10 and phone.get()!="":
                int(phone.get().strip())
                phone.set((phone.get().strip()))
                messagebox.showerror('Error',"Enter valid Phone Number(of 10 digits)")
                phone_entry.focus_set()
        except:
            messagebox.showerror('Invalid Phone no',"Enter only digits ")
            phone.set("")
            phone_entry.focus_set()
            

    def validate_email(event):
        if '@' not in email.get() and email.get().strip()!="":
            messagebox.showerror('Invalid Email',"Please enter a valid Email")
            email_entry.focus_set()
        elif len(email.get())>35:
            messagebox.showerror('Error',"Entered Email is too long")
            email_entry.focus_set()

    def validate_address(event):
        if address.get(1.0,END).strip()!="" and len(address.get(1.0,END))>80:
            messagebox.showerror('Error',"Entered Address is too long")
            address.focus_set()

    def validate_year_of_purchase(event):
        try:
            
            if (yearb.get()!="" and (yearp.get()!="") and int(yearp.get())<int(yearb.get())):
                int(yearp.get().strip())
                yearp.set(yearp.get().strip())
                messagebox.showerror('Logical Error','Year Of Purchase cannot be before Year Of Build')
                year_pur_entry.focus_set()
            elif yearb.get()=="":
                messagebox.showerror('Error','Select year of build first')
                yearp.set("")
                year_build_list.focus_set()
        except:
            messagebox.showerror('Invalid Year of Purchase','Enter digits for Year')
            yearp.set(yearp.get().strip())
            year_pur_entry.focus_set() 
    def validate_price(event):
        try:
            if price.get().strip()!="":
                int(price.get().strip())
            if  len(str(price.get()))>8:
                price.set(price.get().strip())
                messagebox.showerror('Error',"Entered Price too long")
                price_entry.focus_set()
        except:
            messagebox.showerror('Invalid Price',"Enter only digits\nInfo:DO NOT separate digits with commas")
            price.set("")
            
    def validate_license_plate(event):
        if len(str(plate.get().strip()))!=12 and plate.get()!="":
            messagebox.showerror('Invalid','Enter a valid License Plate No')
            plate.set("")
            license_plate_entry.focus_set()
    def validate_color(event):
        if len(color.get())>20:
            messagebox.showerror('Error',"Entered Color name too long")
            color.set("")
    def validate_km_driven(event):
        try:
            if trip.get().strip()!="":
                int(trip.get().strip())
            if  len(str(trip.get().strip()))>7:
                int(trip.get().strip())
                trip.set(trip.get().strip())
                messagebox.showerror('Error',"Entered Trip in(Kms) Too long")
                km_driven_entry.focus_set()
        except:
            messagebox.showerror('Invalid Km driven',"Enter only in digits\nInfo:DO NOT separate digits with commas")
            trip.set("")
            km_driven_entry.focus_set()
    def validate_resale_value(event):
        try:
            if resval.get().strip()!="":
                int(resval.get().strip())
            resval.set(resval.get().strip())
            if len(str(resval.get()))>7:
                messagebox.showerror('Error',"Entered Resale Value Too long")
                resval.set("")
        except:
            messagebox.showerror('Invalid Resale Value',"Enter only in digits\nInfo:DO NOT separate digits with commas")
            resval.set("")
            


    name_entry.focus_set()        
    name_entry.bind("<FocusOut>",validate_name)
    phone_entry.bind("<FocusOut>",validate_phone)
    email_entry.bind("<FocusOut>",validate_email)
    address.bind("<FocusOut>",validate_address)
    year_pur_entry.bind("<FocusOut>",validate_year_of_purchase)
    price_entry.bind("<FocusOut>",validate_price)
    license_plate_entry.bind("<FocusOut>",validate_license_plate)
    color_entry.bind("<FocusOut>",validate_color)
    km_driven_entry.bind("<FocusOut>",validate_km_driven)
    resale_value_entry.bind("<FocusOut>",validate_resale_value)

    def Submit():
        if name.get().strip() == "":
            name_text['foreground']="red"
            name_text.config(text="         *Name:")
            flag = False
        else:
            name_text['foreground']="white"
            name_text.config(text="          Name:")
            flag=True

        if phone.get().strip()=="":
            phone_text['foreground']="red"
            phone_text.config(text="     *Phone No :")   
            flag = False
        else:
            phone_text['foreground']="white"
            phone_text.config(text="      Phone No :")   
            flag = True
        if email.get().strip() == "":
            email_text['foreground']="red"
            email_text.config(text="     *Email :")   
            flag = False
        else:
            email_text['foreground']="white"
            email_text.config(text="      Email :")   
            flag = False

        if address.get(1.0,END).strip() == "":
            address_text['foreground']="red"
            address_text.config(text="      *Address :")   
            flag = False
        else:
            address_text['foreground']="white"
            address_text.config(text="     Address:")   
            flag = True

        
    
        if brand.get().strip() == "":
            brand_text['foreground']="red"
            brand_text.config(text="     *Brand:")   
            flag = False
        else:
            brand_text['foreground']="white"
            brand_text.config(text="  Brand:")   
            flag = True

        if model.get().strip() == "":
            model_text['foreground']="red"
            model_text.config(text="        *Model:")   
            flag = False
        else:
            model_text['foreground']="white"
            model_text.config(text="         Model:")   
            flag = True

        if yearb.get().strip()=="":
            year_build_text['foreground']="red"
            year_build_text.config(text="             *Year of Build:")   
            flag = False
        else:
            year_build_text['foreground']="white"
            year_build_text.config(text="              Year of Build:")   
            flag = True


        if variant.get().strip() == "":
            variant_text['foreground']="red"
            variant_text.config(text="          *Variant:")   
            flag = False
        else:
            variant_text['foreground']="white"
            variant_text.config(text="           Variant:")   
            flag = True

        if yearp.get().strip()=="":
            year_pur_text['foreground']="red"
            year_pur_text.config(text="         *Year of Purchase:")   
            flag = False
        else:
            year_pur_text['foreground']="white"
            year_pur_text.config(text="          Year of Purchase:")   
            flag = True

        if state.get().strip() == "":
            state_text['foreground']="red"
            state_text.config(text="            *Regd State:")   
            flag = False
        else:
            state_text['foreground']="white"
            state_text.config(text="             Regd State:")   
            flag = True

        if price.get().strip()=="":
            price_text['foreground']="red"
            price_text.config(text="        *Price:")   
            flag = False
        else:
            price_text['foreground']="white"
            price_text.config(text="         Price:")   
            flag = True
        
        if plate.get().strip()=="":
            license_plate_text['foreground']="red"
            license_plate_text.config(text="    *License Plate:")   
            flag = False
        else:
            license_plate_text['foreground']="white"
            license_plate_text.config(text="     License Plate:")   
            flag = True
        if trip.get().strip()=="":
            km_driven_text['foreground']="red"
            km_driven_text.config(text="         Km Driven:")   
            flag = False
        else:
            km_driven_text['foreground']="white"
            km_driven_text.config(text="         Km Driven:")   
            flag = True
        
        if flag == True:
            if resval.get().strip()=="":
                resval.set("0")
            c.execute("INSERT INTO VEHICLES VALUES('%s','%s',%s,'%s',%s,'%s',%s,'%s','%s',%s,%s,'%s',%s,'%s','%s','%s')"%(brand.get(),model.get(),int(yearb.get().strip()),variant.get(),int(yearp.get().strip()),state.get(),int(price.get().strip()),color.get().upper(),plate.get(),int(trip.get().strip()),int(resval.get().strip()),name.get().upper().strip(),int(phone.get().strip()),email.get().strip(),address.get(1.0,END).strip(),'for sale'))
            mydb.commit()
            name.set('')
            phone.set('')
            email.set('')
            address.delete(1.0,END)
            brand.set('')
            model.set('')
            variant.set('')
            yearb.set('')
            yearp.set('')
            state.set('')
            price.set('')
            color.set('')
            plate.set('')
            trip.set('')
            resval.set('')
            messagebox.showinfo('Add Vehicle',"Data Added Successfully")
        else:
            messagebox.showerror('*Mandatory Field','Fill all Mandatory Fields')
    submit_button = ttk.Button(option1,text="SUBMIT",command=Submit)
    submit_button.grid(row=11,column=1,padx=(280,0),pady=1,sticky="W")
   

   
                  
 #Caliing individual functions           
def search():
    table=StringVar(option2)   #table is a clue for searching the table name
    sby=StringVar(option2)     #sby is for storing the value of dropdown box
    key=StringVar(option2)     #key is for getting the "word" to be searched for in  the "sby" column of the MySQL_table "table"

    search_table_label=ttk.Label(option2,text="Search Records For:")
    search_by_label=ttk.Label(option2,text="Search by")
    search_dropbox=ttk.Combobox(option2,textvariable=sby,width="30")
    
    
    
    def list_values():
        sby.set("")
        if table.get()=="customers":
            search_dropbox['values']=['Name','Phone no','Email','All Customers']
            cust_table()
        elif table.get()=="vehicles":
            search_dropbox['values']=['Brand','Resale Value','Trip','All for sale']
            car_table()
    
    radiobutton_1=ttk.Radiobutton(option2,text="Customer details",variable=table,value="customers",command=lambda:list_values())
    radiobutton_2=ttk.Radiobutton(option2,text="Vehicles",variable=table,value="vehicles",command=lambda:list_values())
    
    
    search_table_label.grid(row=0,column=0)
    radiobutton_1.grid(row=0,column=1,sticky="W")
    radiobutton_2.grid(row=0,column=2,padx=0,sticky="NW")

    search_by_label.grid(row=1,column=0)
    search_dropbox.grid(row=1,column=1,sticky="W")

    
    search_entry=ttk.Entry(option2,width="32",textvariable=key)
    search_entry.grid(row=1,column=2,sticky="W")
    
    global searchicon
    searchicon=Image.open(r'icons\search_icon.png')
    searchicon=searchicon.resize((20,30), resample = 0)
    searchicon=ImageTk.PhotoImage(searchicon)
    search_button=ttk.Button(option2,text="Search",image=searchicon,compound=LEFT,command=lambda:display(True,sby.get(),key.get().strip(),table.get()))
    search_button.grid(row=1,column=3,sticky="W")

 
    global clearicon
    clearicon=Image.open(r'icons\clear_icon.png')
    clearicon=clearicon.resize((20,20), resample = 0)
    clearicon=ImageTk.PhotoImage(clearicon)    
    clear_button=ttk.Button(option2,text="Clear",image=clearicon,compound=LEFT,command=lambda:display(False,"","",table.get()))
    clear_button.grid(row=1,column=4,sticky='W')
    
    

    search_frame=ttk.LabelFrame(option2,text="Data Retrieved",width=700,height=200)
    search_frame.grid(row=2,column=1,columnspan=4,pady=20)
    search_frame.propagate(False)

    add_customer_button=ttk.Button(option2,text="Add Customer",command=lambda:select_record())


    treev =ttk.Treeview(search_frame, selectmode ='browse',height="5")
    

    scroll_bar_y = ttk.Scrollbar(search_frame,orient="vertical")
    scroll_bar_x=ttk.Scrollbar(search_frame,orient="horizontal")
    
    
    treev.configure(yscrollcommand=scroll_bar_y.set,xscrollcommand=scroll_bar_x.set)

    
    scroll_bar_y.config(command=treev.yview)
    scroll_bar_x.config(command=treev.xview)

    
    
    #Creates the table layout for customer details

    def cust_table():
        add_customer_button.grid_forget()
         # Defining number of columns 
        treev["columns"] = ("1", "2", "3", "4", "5","6","7","8","9","10") 
          
        #Defining heading 
        treev['show'] = 'headings'
          
        #Assigning the width of the columns and where to align the text inside the columns
        treev.column("#1", width = 120, anchor ='sw') 
        treev.column("#2", width = 100, anchor ='sw') 
        treev.column("#3", width = 150, anchor ='sw') 
        treev.column("#4", width = 150, anchor ='sw') 
        treev.column("#5", width = 100, anchor ='sw')
        treev.column("#6", width = 100, anchor ='sw') 
        treev.column("#7", width = 200, anchor ='sw')
        treev.column("#8", width = 100, anchor ='sw')
        treev.column("#9", width = 100, anchor ='sw')
        treev.column("#10",width = 100, anchor='sw')
          
        # Assigning the heading names to the respective columns 
        treev.heading("1", text ="NAME") 
        treev.heading("2", text ="PHONE") 
        treev.heading("3", text ="EMAIL") 
        treev.heading("4", text ="ADDRESS") 
        treev.heading("5", text ="PUR_DATE")
        treev.heading("6", text="PLATE NO") 
        treev.heading("7", text ="RESALE_VAL")
        treev.heading("8", text="BRAND")
        treev.heading("8", text="MODEL")
        treev.heading("9", text="VARIANT")
        treev.heading("10", text="COLOR")
    
        scroll_bar_y.pack(side=RIGHT,fill=Y)
        scroll_bar_x.pack(side=BOTTOM,fill=X)
        treev.pack(side=TOP)
    
    
    #Creates the table layout for vehicle details
    def car_table():
        # Defining number of columns 
        treev["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11") 
          
        #Defining heading 
        treev['show'] = 'headings'
          
        #Assigning the width of the columns and where to align the text inside the columns
        treev.column("#1", width = 120, anchor ='sw') 
        treev.column("#2", width = 120, anchor ='sw') 
        treev.column("#3", width = 120, anchor ='sw') 
        treev.column("#4", width = 120, anchor ='sw') 
        treev.column("#5", width = 120, anchor ='sw') 
        treev.column("#6", width = 120, anchor ='sw') 
        treev.column("#7", width = 120, anchor ='sw')
        treev.column("#8", width = 120, anchor ='sw') 
        treev.column("#9", width = 120, anchor ='sw') 
        treev.column("#10", width = 120, anchor ='sw')
        treev.column("#11", width = 120, anchor ='sw')  
          
        treev.heading("1", text ="BRAND") 
        treev.heading("2", text ="MODEL") 
        treev.heading("3", text ="VARIANT") 
        treev.heading("4", text ="BUILT_YR") 
        treev.heading("5", text ="PUR_YR") 
        treev.heading("6", text ="REGD STATE") 
        treev.heading("7", text ="RESALE_VAL") 
        treev.heading("8", text ="COLOR") 
        treev.heading("9", text ="PLATE_NO")
        treev.heading("10", text ="TRIP")  
        treev.heading("11", text ="PREV_OWNER_NAME")
        
        scroll_bar_y.pack(side=RIGHT,fill=Y)
        scroll_bar_x.pack(side=BOTTOM,fill=X)
        treev.pack(side=TOP)
        add_customer_button.grid(row=3,column=1,sticky="W")  

    def display(show,field,keyw,table):
        #sby is field
        #key is keyw
        if show==True and table=="vehicles":
            if field=="All for sale" :
                key.set("")
                c.execute("select BRAND,MODEL,VAR,YEARB,YEARP,STATE,RESVAL,COLOR,PLATE,TRIP,NAME from vehicles where AVAIL='for sale'")
                records=c.fetchall()
                if len(records)==0:
                    messagebox.showinfo('Records',"No records exist")

            elif field=="Brand" and keyw!="":
                c.execute("select BRAND,MODEL,VAR,YEARB,YEARP,STATE,RESVAL,COLOR,PLATE,TRIP,NAME from vehicles where BRAND='%s' and AVAIL='for sale'"%(keyw.upper()))
                records=c.fetchall()
                if len(records)==0:
                    messagebox.showinfo('Records',"No records exist")
            elif field=="Resale Value":
                l=keyw.split(",")
                try:
                    st=l[0]
                    end=l[1]
                    int(st)
                    int(end)
                    c.execute("select BRAND,MODEL,VAR,YEARB,YEARP,STATE,RESVAL,COLOR,PLATE,TRIP,NAME from vehicles where RESVAL BETWEEN %s and %s and AVAIL='for sale'"%(st,end))
                    records=c.fetchall()
                    if len(records)==0:
                        messagebox.showinfo('Records',"No records exist")   
                except:
                    messagebox.showerror('Invalid Values',"Enter Integer values for FROM and TO limits\n Eg:500,1000 \n where 500 is lower limit and 1000 is the upper limit ")
                
                
            elif field=="Trip":
                l=keyw.split(",")
                try:
                    st=l[0]
                    end=l[1]
                    int(st)
                    int(end)
                    c.execute("select BRAND,MODEL,VAR,YEARB,YEARP,STATE,RESVAL,COLOR,PLATE,TRIP,NAME from vehicles where TRIP BETWEEN %s and %s and AVAIL='for sale'"%(st,end))
                    records=c.fetchall()   
                    if len(records)==0:
                        messagebox.showinfo('Records',"No records exist")
                except:
                    messagebox.showerror('Invalid Values',"Enter Integer values for FROM and TO limits\n Eg:500,1000 \n where 500 is lower limit and 1000 is the upper limit ")
                
            elif field=="" or keyw=="":
                messagebox.showerror('Error',"Fill in all fields")
            #Delete if any records are present in the treeview
            for i in treev.get_children(): 
                treev.delete(i)
            try:
                for row in records:

                    brand=row[0]
                    model =row[1]
                    var=row[2]
                    yearb=row[3]
                    yearp=row[4]
                    state=row[5]
                    resval=row[6]
                    color=row[7]
                    plate=row[8]
                    trip=row[9]
                    prev_name=row[10]
                    treev.insert("", 'end', text ="L1", values =(brand,model,var,yearb,yearp,state,resval,color,plate,trip,prev_name,))
                radiobutton_1.config(state="disabled")
                radiobutton_2.config(state="disabled")
            except:
                pass
        
        elif show==True and table=='customers':
            if field=="All Customers":
                 c.execute("select * from CUSTOMERS")
                 key.set("")
                 records=c.fetchall()
                 if len(records)==0:
                    messagebox.showinfo('Records',"No records exist")
            elif field=="Name" and keyw!="":
                c.execute("select * from CUSTOMERS where NAME='%s'"%(keyw.upper()))
                records=c.fetchall()
                if len(records)==0:
                    messagebox.showinfo('Records',"No records exist")
            elif field=="Phone no" and keyw!="":
                c.execute("select * from customers where PHONE=%s"%(keyw))
                records=c.fetchall()
                if len(records)==0:
                    messagebox.showinfo('Records',"No records exist")
            elif field=="Email" and keyw!="":
                c.execute("select * from customers where EMAIL='%s'"%(keyw.strip()))
                records=c.fetchall()
                if len(records)==0:
                    messagebox.showinfo('Records',"No records exist")


            elif field=="" or keyw=="":
                 messagebox.showerror('Error',"Fill in all fields")
             
            #Delete if any records are present in the treeview
            for i in treev.get_children(): 
                    treev.delete(i)

            try:
                for row in records:

                    Name =row[0]
                    Phone =row[1]
                    Email =row[2]
                    Addr =row[3]
                    Pur_date=row[4]
                    plate=row[5]                        
                    c.execute("select BRAND,MODEL,VAR,COLOR from vehicles where plate='%s'"%(plate))       
                    res=c.fetchone()
                    brand=res[0]
                    model=res[1]
                    var=res[2]
                    color=res[3]
                    treev.insert("", 'end', text ="L1", values =(Name,Phone,Email,Addr,Pur_date,plate,brand,model,var,color))
                radiobutton_1.config(state="disabled")
                radiobutton_2.config(state="disabled")
            except:
                pass



        else:
            #Delete if any records are present in the treeview  when clear button is clicked
            for i in treev.get_children(): 
                treev.delete(i)
            sby.set("")
            key.set("")
            radiobutton_1.config(state="normal")
            radiobutton_2.config(state="normal")
    


    def from_and_to(event):
        if sby.get()=="Trip" or sby.get()=="Resale Value":
            search_entry.delete(0,END)
            search_entry.insert(0,"FROM,TO")
        else:
            search_entry.delete(0,END)


    def select_record():
        selected=treev.focus()
        values=treev.item(selected,'values')
        try:
            b=values[0]
            m=values[1]
            v=values[2]
            res=values[6]
            co=values[7]
            p=values[8]
            tp=values[9]
            add_customer(b,m,v,co,res,p,tp)
        except IndexError:
            messagebox.showinfo('Add_Customer','Choose a Vehicle from the table')
    
    search_dropbox.bind("<<ComboboxSelected>>",from_and_to)


def invsearch(invno):
    #invno is a str here
    #Checks whether invno is an integer by using except block and 
    #sets the corresponding boolean vslue to flag
    try:
        int(invno)  
        c.execute("select * from customers where INVNO='%s'"%(invno))
        row=c.fetchone()
        flag=True
    except ValueError:
        messagebox.showerror('Error..::',"Enter a Valid Invoice No!")
        flag=False
    if flag==True and row!=None:    
        try:
            
                    nm =row[0]
                    ph =row[1]
                    em =row[2]
                    addr =row[3]
                    pur_date=row[4]
                    plate=row[5]
                    price=row[6]
                    invno=row[7]                        
                    c.execute("select BRAND,MODEL,VAR,COLOR,TRIP from vehicles where plate='%s'"%(plate))       
                    res=c.fetchone()
                    brand=res[0]
                    model=res[1]
                    variant=res[2]
                    color=res[3]
                    trip=res[4]
                    invoice(nm,ph,em,addr,brand,model,variant,color,trip,plate,price,pur_date,invno)
        except Exception as e:
            print(e)
    elif flag==True and row==None:
        messagebox.showinfo('Data Info',"No records exist for\nInvoice no:%d"%(int(invno)))

#Function for generating invoice inside Text Widget

#def invoice(nm="Kevin",ph=1234567890,em="ironman@gmail",addr="parel\nqwe\nasd\n",brand="Maruti Suzuki",model="Swift Dezire",variant="LXI",color="WHITE",trip="25",plate="KL",resval=0,today="",invno=0):
def invoice(nm="",ph=0,em="",addr="",brand="",model="",variant="",color="",trip=0,plate="",resval=0,today="",invno=0):
     from PIL import Image,ImageTk
     global pdficon
     pdficon=Image.open(r'icons\pdf_icon.png')
     pdficon=pdficon.resize((30,30), resample = 0)
     pdficon=ImageTk.PhotoImage(pdficon)

     search=ttk.Label(option3,text="Invoice No.:")
     sentry=ttk.Entry(option3)
     sbttn=ttk.Button(option3,text="Search",image=searchicon,compound=LEFT,command=lambda:invsearch(sentry.get()))
     
     spdf=ttk.Button(option3,text="Save as PDF",image=pdficon,compound=LEFT,command=lambda:pdf_generator.create_pdf(info,invno))
     search.grid(row=0,column=0)
     sentry.grid(row=0,column=1,sticky='W')
     sbttn.grid(row=0,column=2,sticky='W')
     spdf.grid(row=0,column=3)

     sum_frame=ttk.Frame(option3)
     sum_frame.propagate(1)
     sum_text_box=Text(sum_frame,width=115)

     sum_text_box.config(state='normal')
     sum_text_box.delete(1.0,END)

     global header_img
     header_img=ImageTk.PhotoImage(Image.open("header.png").resize((1285,90), resample = 0))
     sum_text_box.image_create(END,image=header_img)
     sum_text_box.config(font="Times 16",foreground='black',background='white')
     sum_text_box.insert(INSERT,"\nInvoice No:%d\n"%(invno))
     sum_text_box.insert(INSERT,"Date:%s"%(today))
     sum_text_box.insert(INSERT,"\n")
     
     sum_text_box.insert(INSERT,"Customer Name:%-25s"%(nm))
     sum_text_box.insert(INSERT," "*25)
     sum_text_box.insert(INSERT,"Phone no:%d\n"%(ph))
     sum_text_box.insert(INSERT,"  "*39)
     sum_text_box.insert(INSERT," "*4)
     sum_text_box.insert(INSERT,"Email:%-35s\n"%(em))
     sum_text_box.insert(INSERT,"Billing Address:%-80s\n"%(addr))
     sum_text_box.insert(INSERT,"    "*6)
     sum_text_box.insert(INSERT,"           Particulars\n")
     sum_text_box.insert(INSERT,"_"*115)
     sum_text_box.insert(INSERT,"\n")
     sum_text_box.insert(INSERT,"Brand:%-13s"%(brand))
     sum_text_box.insert(INSERT,"    "*4)
     sum_text_box.insert(INSERT,"Purchase Value:%d\n\n"%(resval))
     sum_text_box.insert(INSERT,"Model:%-12s\n\n"%(model))
     sum_text_box.insert(INSERT,"Variant:%-16s\n\n"%(variant))
     sum_text_box.insert(INSERT,"Color:%-20s\n\n"%(color))
     sum_text_box.insert(INSERT,"Trip(Km driven):%-7s\n\n"%trip)
     sum_text_box.insert(INSERT,"License Plate no:%-12s\n\n"%(plate))
     info=sum_text_box.get(2.0,END).split('\n')
     sum_text_box.config(state='disabled')

     vbar=Scrollbar(sum_frame,command=sum_text_box.yview,orient="vertical")
     hbar=Scrollbar(sum_frame,command=sum_text_box.xview,orient="horizontal")
     sum_text_box.configure(yscrollcommand=vbar.set)
     sum_text_box.configure(xscrollcommand=hbar.set)
     sum_text_box.grid(row=0,column=0,sticky="EW")
     vbar.grid(row=0,column=1,sticky="NS")
     hbar.grid(row=1,column=0,sticky="NEWS")
     sum_frame.grid(row=1,column=0,columnspan=4,padx=20,pady=20)
add_vehicle()
search()    
invoice()
root.mainloop()
#use 134 star characters for filling the screen
#**************************************************************************************************************************************
