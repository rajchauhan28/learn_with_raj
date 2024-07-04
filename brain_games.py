import tkinter
def calc():
	a = int(e1.get())
	b = int(e2.get())
	c = int(e3.get())
	lst = [a, b]
	for i in range(5):
		a, b = b, a+b+c
		lst.append(b)
	lb = tkinter.Label(t, text=str(lst)).pack()
t=tkinter.Tk()
e1=tkinter.Entry(t)
e1.pack()
e2=tkinter.Entry(t)
e2.pack()
e3=tkinter.Entry(t)
e3.pack()
btn=tkinter.Button(t, text = 'click', command = calc).pack()
t.mainloop()
