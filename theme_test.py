from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedStyle
root=Tk()
frame=ttk.Frame(root)
root.call('lappend', 'auto_path', r'C:\Python\Lib\site-packages\ttkthemes\themes\awthemes-9.5.0')
root.call('package', 'require', 'breeze')
style = ttk.Style(root)
style.theme_use('breeze')



a=ttk.Button(frame,text="Button1").pack()
s=ttk.Button(frame,text="Button2").pack()
frame.pack(fill=BOTH,expand=1)
root.mainloop()
