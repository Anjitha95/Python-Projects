from tkinter import *
from tkinter import messagebox
import random
from word import words
from string import ascii_uppercase


def guess(c):
    global numberOfGuess
    if numberOfGuess < 11:
        text = list(word_with_space)
        guessed = list(lb1word.get())
        if word_with_space.count(c) >0:
            for i in range(len(text)):
                if text[i] == c:
                    guessed[i] = c
                lb1word.set("".join(guessed))
                if lb1word.get() == word_with_space:
                    messagebox.showinfo("Hangman", 'You have Guess It!!')
                    new_word()
        else:
            numberOfGuess += 1
            imageLabel.config(image=photos[numberOfGuess])
            if numberOfGuess == 11:
                messagebox.showwarning("Hangman", 'Game Over!! The Word was: '+ the_word)


def new_word():
    global word_with_space
    global numberOfGuess
    global the_word
    numberOfGuess =0
    imageLabel.config(image= photos[0])
    the_word = random.choice(words)
    print(the_word.upper())
    word_with_space = " ".join(the_word.upper())
    lb1word.set(" ".join("_"* len(the_word)))


if __name__ == '__main__':

    window = Tk()

    window.title('Hangman')

    window.resizable(0, 0)

    photos = [PhotoImage(file =r'C:\Users\anjit\Desktop\All folder\python projects\hangman\images\hang0.png'),
              PhotoImage(file=r'C:\Users\anjit\Desktop\All folder\python projects\hangman\images\hang1.png'),
              PhotoImage(file=r'C:\Users\anjit\Desktop\All folder\python projects\hangman\images\hang2.png'),
              PhotoImage(file=r'C:\Users\anjit\Desktop\All folder\python projects\hangman\images\hang3.png'),
              PhotoImage(file=r'C:\Users\anjit\Desktop\All folder\python projects\hangman\images\hang4.png'),
              PhotoImage(file=r'C:\Users\anjit\Desktop\All folder\python projects\hangman\images\hang5.png'),
              PhotoImage(file=r'C:\Users\anjit\Desktop\All folder\python projects\hangman\images\hang6.png'),
              PhotoImage(file=r'C:\Users\anjit\Desktop\All folder\python projects\hangman\images\hang7.png'),
              PhotoImage(file=r'C:\Users\anjit\Desktop\All folder\python projects\hangman\images\hang8.png'),
              PhotoImage(file=r'C:\Users\anjit\Desktop\All folder\python projects\hangman\images\hang9.png'),
              PhotoImage(file=r'C:\Users\anjit\Desktop\All folder\python projects\hangman\images\hang10.png'),
              PhotoImage(file=r'C:\Users\anjit\Desktop\All folder\python projects\hangman\images\hang11.png')
              ]

    imageLabel = Label(window)
    imageLabel.grid(row =0, column=0, columnspan=3, padx=10, pady=40)
    imageLabel.config(image= photos[0])

    lb1word = StringVar()
    Label(window, textvariable=lb1word, font=('Arial', 24, 'bold')).grid(row =0, column=3, columnspan=6, padx=10)
    n = 0
    for c in ascii_uppercase:
        Button(window, text=c, command=lambda c=c: guess(c), font=('Arial', 18, 'bold'), width=4).grid(row= 1+ n// 9,
                                                                                         column=n % 9)
        n += 1
    Button(window, text= "New\nGame", command=lambda: new_word(), font=('Arial', 10, 'bold')).grid(row=3, column=8, sticky='NSWE')
    new_word()
    window.mainloop()
