from tkinter import *


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


def extraxt_from_text(text):
    l = []
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l


def calculate():
    text = textin.get()
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l = extraxt_from_text(text)
                r = operations[word.upper()](l[0], l[1])
                list.delete(0, END)
                list.insert(END, r)
            except:
                list.delete(0, END)
                list.insert(
                    END, 'something went wrong please enter correct something again')
            finally:
                break
        elif word.upper() not in operations.keys():
            list.delete(0, END)
            list.insert(END, 'something went wrong please enter again')


operations = {'ADD': add, 'ADDITION': add, 'SUM': add, 'PLUS': add, "+": add,
              'SUB': sub, 'DIFFERENCE': sub, 'MINUS': sub, 'SUBTRACT': sub,
              'PRODUCT': mul, 'MULTIPLICATION': mul, '*': mul,
              'MULTIPLY': mul, 'DIVISION': div, 'DIV': div, 'DIVIDE': div, 'MOD': mod, '/': div,
              '%': mod,              'REMANDER': mod, 'MODULUS': mod}

win = Tk()
win.geometry('500x300')
win.title('Smart cal')
win.configure(bg='red')

l1 = Label(win, text='I am a smart calculator', width=20, padx=3)
l1.place(x=150, y=10)
l2 = Label(win, text='My name is genius', padx=3)
l2.place(x=180, y=40)
l3 = Label(win, text='What can i help you', padx=3)
l3.place(x=176, y=130)

textin = StringVar()
e1 = Entry(win, width=30, textvariable=textin)
e1.place(x=100, y=160)

b1 = Button(win, text='Just this', command=calculate)
b1.place(x=210, y=200)

list = Listbox(win, width=20, height=3)
list.place(x=150, y=230)

win.mainloop()
