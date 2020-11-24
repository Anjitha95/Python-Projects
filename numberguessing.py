"""A GUI Based Number Guessing Game using
 Tkinter Lib of python.The Game is very simple, here computer will choose a random number
 between 1-30 and the player will have to find out the number with only 6 chances."""


from tkinter import *
from random import randrange


# get the integer number
def submit_btn():
    guessed_number = int(text_field.get())
    print(type(guessed_number))
    process(guessed_number)


# method that validates the answer
def process(guessed_number):
    global guess_left, guess_no
    if guessed_number == guess_no:
        title_guess.config(text='Guesses Used:-' + str(guess_left))
        game_status.config(text='You have won!!', fg='green')
    elif guessed_number > guess_no:
        guess_left += 1
        title_guess.config(text='Guesses Used:-' + str(guess_left))
        game_status.config(text='Number you guessed is tooo HIGH', fg='red')
    else:
        guess_left += 1
        title_guess.config(text='Guesses Used:-' + str(guess_left))
        game_status.config(text='Number you guessed is tooo LOW', fg='red')
    if guess_left == 6:
        if guessed_number != guess_no:
            title_guess.config(text='Guesses Used:- 6')
            game_status.config(text='Maximum Guess Reached. You Lost!! The Number was:' + str(guess_no), fg='blue')
            btn_submit["state"] = DISABLED


# Resets all the labels to default values
def reset_btn():
    global guess_left, guess_no
    guess_left = 0
    guess_no = randrange(31)
    title_guess.config(text='Guesses Used:-')
    game_status.config(text='Status', fg='blue')
    btn_submit["state"] = NORMAL


guess_left = 0
guess_no = randrange(31)

# main function
if __name__ == '__main__':
    window = Tk()

    window.configure(background='#f5f5f5')

    window.title('Guess the number')

    window.resizable(0, 0)

    window.geometry("600x400")

    title = Label(window, text='Guess the number between 0 to 30', anchor='center', font=('Arial', 18, 'bold'),
                  bg='#f5f5f5')
    title.pack()

    break1 = Label(window, text='---------------------------------------------------------------------------',
                   font=('Arial', 18, 'bold'), bg='#f5f5f5')
    break1.pack()

    title_max = Label(window, text='Maximum Guess:- 6', font=('Arial', 14, 'bold'), bg='#f5f5f5')
    title_max.pack()

    title_guess = Label(window, text='Guesses Used:-', font=('Arial', 14, 'bold'), bg='#f5f5f5')
    title_guess.pack()

    break2 = Label(window, text='---------------------------------------------------------------------------',
                   font=('Arial', 18, 'bold'), bg='#f5f5f5')
    break2.pack()

    game_status = Label(window, text='Status', font=('Arial', 14, 'bold'), bg='#f5f5f5', fg='blue')
    game_status.pack()

    break3 = Label(window, text='---------------------------------------------------------------------------',
                   font=('Arial', 18, 'bold'), bg='#f5f5f5')
    break3.pack()

    number = StringVar()

    enter = Label(window, text="Enter the number you have guessed", font=('Arial', 14, 'bold'), bg='#f5f5f5')
    enter.pack()

    text_field = Entry(window, font=('Arial', 14, 'bold'), textvariable=number, fg='black')
    text_field.pack()

    btn_submit = Button(window, text='Submit', font=('Arial', 14), border=1, bg='#f5f5f5', command=lambda: submit_btn())
    btn_submit.pack(side=LEFT, padx=150)

    btn_reset = Button(window, text='Reset', font=('Arial', 14), border=1, bg='#f5f5f5', command=lambda: reset_btn())
    btn_reset.pack(side=LEFT)

    window.mainloop()
