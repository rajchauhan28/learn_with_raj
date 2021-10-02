from tkinter import*
root=Tk()

def hello():
    print("File ")


menubar=Menu(root)
menubar.add_command(label="File",command=hello)
menubar.add_command(label="Quit",command=root.quit)

root.config(menu=menubar)
root.mainloop()