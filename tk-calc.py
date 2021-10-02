from tkinter import Tk, Button, Label, Entry

'''Author: Raj Singh Chauhan
Purpose:
	Making a calculator that brings power of a cool calculator with a very easy logics
	just enter the expression by tapping on buttons and get a answer'''


def equal():
    ev = entry.get()
    l = len(ev)
    entry.delete(0, l)
    try:
        entry.insert(0, str(eval(ev)))
    except:
        entry.insert(0, 'error')


def clearer():
    e = entry.get()
    l = len(e)
    entry.delete(0, l)


def on_click(n):
    r = len(entry.get())

    entry.insert(r, n)


def exiter():
    root.destroy()


def backspace():
    entry.delete(len(entry.get()) - 1)


root = Tk()
entry = Entry(root, width=35)
btn1 = Button(root, text='1', height=4, width=7, command=lambda: on_click(1))
btn2 = Button(root, text='2', height=4, width=7, command=lambda: on_click(2))
btn3 = Button(root, text='3', height=4, width=7, command=lambda: on_click(3))
btn4 = Button(root, text='4', height=4, width=7, command=lambda: on_click(4))
btn5 = Button(root, text='5', height=4, width=7, command=lambda: on_click(5))
btn6 = Button(root, text='6', height=4, width=7, command=lambda: on_click(6))
btn7 = Button(root, text='7 ', height=4, width=7, command=lambda: on_click(7))
btn8 = Button(root, text='8', height=4, width=7, command=lambda: on_click(8))
btn9 = Button(root, text='9', height=4, width=7, command=lambda: on_click(9))
btn0 = Button(root, text='0', height=4, width=7, command=lambda: on_click(0))
plus = Button(root, text='+', height=4, width=7, command=lambda: on_click('+'))
minus = Button(root, text='-', height=4, width=7, command=lambda: on_click('-'))
mult = Button(root, text='*', height=4, width=7, command=lambda: on_click('*'))
divide = Button(root, text='/', height=4, width=7, command=lambda: on_click('/'))
evaluate = Button(root, text='=', height=4, width=7, command=equal)
back = Button(root, text='<--', height=4, width=7, command=backspace)
clear = Button(root, text='clear', height=4, width=7, command=clearer)
exit = Button(root, text='Exit', height=4, width=7, command=exiter)

entry.grid(row=0, column=0, columnspan=3)
btn1.grid(row=1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=1, column=2)
btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)
btn7.grid(row=3, column=0)
btn8.grid(row=3, column=1)
btn9.grid(row=3, column=2)
btn0.grid(row=4, column=0)
plus.grid(row=5, column=0)
minus.grid(row=5, column=1)
divide.grid(row=5, column=2)
mult.grid(row=6, column=0)
evaluate.grid(row=4, column=1)
back.grid(row=4, column=2)
clear.grid(row=6, column=1)
exit.grid(row=6, column=2)
root.mainloop()
