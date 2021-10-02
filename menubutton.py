from tkinter import *
root=Tk()
root.geometry("400x400")
menubutton=Menubutton(root,text="file",relief=FLAT)

menubutton.grid()
menubutton.menu=Menu(menubutton)
menubutton["menu"]=menubutton.menu
menubutton.menu.add_checkbutton(label="open",variable=IntVar())
menubutton.menu.add_checkbutton(label="Close",variable=IntVar())
menubutton.menu.add_checkbutton(label="New",variable=IntVar())

menubutton.pack()
root.mainloop()