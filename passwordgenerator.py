from tkinter import *
import random
from tkinter import messagebox
import string


def generate():
    max_len = 8
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digits = random.choice(string.digits)
    special = random.choice(string.punctuation)
    comp = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    temp = lower + upper + digits + special

    if len(temp) < max_len:
        for i in range(max_len - 4):
            temp = temp + random.choice(comp)
            
    messagebox.showinfo('Password', temp)


if __name__ == '__main__':

    window = Tk()

    window.title('Password Generator')

    window.resizable(0, 0)

    window.geometry("300x200")

    lb1 = Label(window, text='Password Generator', font=('Arial', 12, 'bold'))
    lb1.pack(pady= 30)

    btn = Button(window, text='Generate password', font=('Arial', 12, 'bold'), command= lambda : generate())
    btn.pack()

    window.mainloop()