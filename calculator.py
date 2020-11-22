""" This is a python program for calculator. In this program we make use of python tkinter
library to perform GUI operations. This is one of the beginner level program that one do after learning
the basics of python."""

from tkinter import *
from tkinter import StringVar


# The press(num) method is used to get the number from the GUI and formulating it to an expression
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


# The clear() function is used to clear the text editor of our calculator.
def clear():
    global expression
    expression = ""
    equation.set("")


# equalpress() method evaluates the expression we got from the press() method and returns the result.
def equalpress():
    global expression
    result = str(eval(expression))
    equation.set(result)
    expression = ""


expression = ""

# main function
if __name__ == '__main__':
    gui = Tk()

    # set the background color of the GUI
    gui.configure(background="black")

    # set the title
    gui.title("Calculator")

    # disable resize button
    gui.resizable(0, 0)

    # set the size of the calculator
    gui.geometry("320x450")

    # Divide into frames

    # frame 1: For text editor
    text_editor = Frame(gui, bg='#ffffff', height=100, width=320)
    text_editor.pack(side=TOP)

    # Frame 2: For button row 1
    btn_row1 = Frame(gui, bg='#ffffff')
    btn_row1.pack(expand=True, fill='both')

    # Frame 3: For button row 2
    btn_row2 = Frame(gui, bg='#ffffff')
    btn_row2.pack(expand=True, fill='both')

    # Frame 4: For button row 3
    btn_row3 = Frame(gui, bg='#ffffff')
    btn_row3.pack(expand=True, fill='both')

    # Frame 5: For button row 4
    btn_row4 = Frame(gui, bg='#ffffff')
    btn_row4.pack(expand=True, fill='both')

    # text editor
    equation = StringVar()
    expression_field = Entry(text_editor, font=('Arial', 30, 'bold'), textvariable=equation, fg='black', justify=RIGHT)
    expression_field.pack(expand=True, fill='both', ipady=40)

    # button row 1
    btn_seven = Button(btn_row1, text='7', font=('Arial', 22), border=0, command=lambda: press(7))
    btn_seven.pack(side=LEFT, expand=True, fill='both')

    btn_eight = Button(btn_row1, text='8', font=('Arial', 22), border=0, command=lambda: press(8))
    btn_eight.pack(side=LEFT, expand=True, fill='both')

    btn_nine = Button(btn_row1, text=' 9', font=('Arial', 22), border=0, command=lambda: press(9))
    btn_nine.pack(side=LEFT, expand=True, fill='both')

    btn_mul = Button(btn_row1, text='*', font=('Arial', 22), border=0, command=lambda: press('*'))
    btn_mul.pack(side=LEFT, expand=True, fill='both')

    # button row 2
    btn_six = Button(btn_row2, text='6', font=('Arial', 22), border=0, command=lambda: press(6))
    btn_six.pack(side=LEFT, expand=True, fill='both')

    btn_five = Button(btn_row2, text='5', font=('Arial', 22), border=0, command=lambda: press(5))
    btn_five.pack(side=LEFT, expand=True, fill='both')

    btn_four = Button(btn_row2, text='4', font=('Arial', 22), border=0, command=lambda: press(4))
    btn_four.pack(side=LEFT, expand=True, fill='both')

    btn_sub = Button(btn_row2, text='-', font=('Arial', 22), border=0, command=lambda: press('-'))
    btn_sub.pack(side=LEFT, expand=True, fill='both')

    # button row 3
    btn_three = Button(btn_row3, text='3', font=('Arial', 22), border=0, command=lambda: press(3))
    btn_three.pack(side=LEFT, expand=True, fill='both')

    btn_two = Button(btn_row3, text='2', font=('Arial', 22), border=0, command=lambda: press(2))
    btn_two.pack(side=LEFT, expand=True, fill='both')

    btn_one = Button(btn_row3, text=' 1', font=('Arial', 22), border=0, command=lambda: press(1))
    btn_one.pack(side=LEFT, expand=True, fill='both')

    btn_add = Button(btn_row3, text='+', font=('Arial', 22), border=0, command=lambda: press('+'))
    btn_add.pack(side=LEFT, expand=True, fill='both')

    # button row 4

    btn_c = Button(btn_row4, text='C', font=('Arial', 22), border=0, command=lambda: clear())
    btn_c.pack(side=LEFT, expand=True, fill='both')

    btn_zero = Button(btn_row4, text="0", font=('Arial', 22), border=0, command=lambda: press(0))
    btn_zero.pack(side=LEFT, expand=True, fill='both')

    btn_equals = Button(btn_row4, text='=', font=('Arial', 22), border=0, command=lambda: equalpress())
    btn_equals.pack(side=LEFT, expand=True, fill='both')

    btn_division = Button(btn_row4, text='/', font=('Arial', 22), border=0, command=lambda: press('/'))
    btn_division.pack(side=LEFT, expand=True, fill='both')

    gui.mainloop()
