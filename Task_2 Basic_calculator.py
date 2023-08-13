from tkinter import *


expression = ""


def add_to_screen(symbol):
    global expression
    expression += str(symbol)
    screen.delete(1.0, 'end')
    screen.insert(1.0, expression)


def clear():
    global expression
    expression = ""
    screen.delete(1.0, 'end')

# evaluating the expression using eval()


def evaluate1():
    global expression
    try:
        result = str(eval(expression))
        expression = ""
        screen.delete(1.0, 'end')
        screen.insert(1.0, result)
    except:
        clear()
        screen.insert(1.0, "Error")


win = Tk()
win.geometry("300x275")
win.title("Basic Calculator")
win.resizable(False,False)

screen = Text(win, height=2, width=16, font=("aerial 24"))
screen.grid(columnspan=5)

# buttons

b1 = Button(win, text='1', command=lambda: add_to_screen(
    '1'), width=5, font=('ivay 12 bold'))
b1.grid(row=2, column=1)

b2 = Button(win, text='2', command=lambda: add_to_screen(
    '2'), width=5, font=('ivay 12 bold'))
b2.grid(row=2, column=2)


b3 = Button(win, text='3', command=lambda: add_to_screen(
    '3'), width=5, font=('ivay 12 bold'))
b3.grid(row=2, column=3)

b4 = Button(win, text='4', command=lambda: add_to_screen(
    '4'), width=5, font=('ivay 12 bold'))
b4.grid(row=3, column=1)
b5 = Button(win, text='5', command=lambda: add_to_screen(
    '5'), width=5, font=('ivay 12 bold'))
b5.grid(row=3, column=2)
b6 = Button(win, text='6', command=lambda: add_to_screen(
    '6'), width=5, font=('ivay 12 bold'))
b6.grid(row=3, column=3)
b7 = Button(win, text='7', command=lambda: add_to_screen(
    '7'), width=5, font=('ivay 12 bold'))
b7.grid(row=4, column=1)
b8 = Button(win, text='8', command=lambda: add_to_screen(
    '8'), width=5, font=('ivay 12 bold'))
b8.grid(row=4, column=2)
b9 = Button(win, text='9', command=lambda: add_to_screen(
    '9'), width=5, font=('ivay 12 bold'))
b9.grid(row=4, column=3)
b0 = Button(win, text='0', command=lambda: add_to_screen(
    '0'), width=5, font=('ivay 12 bold'))
b0.grid(row=5, column=2)

bplus = Button(win, text='+', command=lambda: add_to_screen('+'),
               width=5, font=('ivay 12 bold'))
bplus.grid(row=2, column=4)

bminus = Button(win, text='-', command=lambda: add_to_screen('-'),
                width=5, font=('ivay 12 bold'))
bminus.grid(row=3, column=4)

bdivision = Button(win, text='/', command=lambda: add_to_screen('/'),
                   width=5, font=('ivay 12 bold'))
bdivision.grid(row=4, column=4)

bmutl = Button(win, text='*', command=lambda: add_to_screen('*'),
               width=5, font=('ivay 12 bold'))
bmutl.grid(row=5, column=4)


# parentisis
b_open = Button(win, text='(', command=lambda: add_to_screen(
    '('), width=5, font=('ivay 12 bold'))
b_open.grid(row=5, column=1)

b_close = Button(win, text=')', command=lambda: add_to_screen(
    ')'), width=5, font=('ivay 12 bold'))
b_close.grid(row=5, column=3)

b_equal = Button(win, text='=', command=evaluate1,
                 width=12, font=('ivay 12 bold'))
b_equal.grid(row=6, column=3, columnspan=2)
b_clear = Button(win, text='clr', command=clear,
                 width=12, font=('ivay 12 bold'))
b_clear.grid(row=6, column=1, columnspan=2)


win.mainloop()
