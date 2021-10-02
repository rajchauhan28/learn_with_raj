from tkinter import *
root=Tk()
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=X)
scrollbar.pack(side=RIGHT,fill=Y)
list=Listbox (root,yscrollcommand=scrollbar.set)
for line in range(50):
    list.insert(END,f"Python{str(line)}")
    list.pack(side=LEFT,fill=BOTH)
    scrollbar.config(command=list.yview())

root.mainloop()