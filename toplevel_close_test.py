from tkinter import *
root=Tk()
def create():
	popup=Toplevel(root)
	def submit():
		popup.destroy()
	Button(popup,text="Destroy TopLevel",command=submit).pack()
Button(root,text="Open TopLevel",command=create).pack()
root.mainloop()
