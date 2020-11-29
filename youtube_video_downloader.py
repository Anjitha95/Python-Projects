from pytube import YouTube
from tkinter import *

radio_option = ""
youtube_link = ""


# For getting the value from the radio box
def sel():
    global radio_option
    radio_option = var.get()
    if radio_option == 1:
        label_message.config(text='You have selected Audio option. Click the button to Download the Audio!!!',
                             fg='white', font=('Arial', 10, 'bold'))
    else:
        label_message.config(text='You have selected Video option. Click the button to Download the Video!!!',
                             fg='white', font=('Arial', 10, 'bold'))
    print(radio_option)


def download_btn():
    global radio_option, youtube_link
    youtube_link = str(link_field.get())
    print(youtube_link)
    yt_obj = YouTube(youtube_link)
    if radio_option == 2:
        yt_obj.streams.get_highest_resolution().download(r'C:\Users\anjit\downloads')
        label_message.config(text='Video downloaded at: Downloads',
                             fg='white', font=('Arial', 10, 'bold'))
    elif radio_option == 1:
        yt_obj.streams.get_audio_only().download(r'C:\Users\anjit\downloads')
        label_message.config(text='Audio downloaded at: Downloads',
                             fg='white', font=('Arial', 10, 'bold'))

    else:
        label_message.config(text='Some Error has Occured!!',
                             fg='white', font=('Arial', 10, 'bold'))


if __name__ == '__main__':
    window = Tk()

    window.title('YouMate')

    window.configure(background='black')

    window.resizable(0, 0)

    window.geometry("600x400")

    title = Label(window, text='Youtube Video Downloader', anchor='center', font=('Arial', 18, 'bold'),
                  bg='red', width=400, fg='white', height=3)
    title.pack()

    label_link = Label(window, text='Link of video to download', anchor='center', font=('Arial', 14, 'bold'),
                       bg='black', width=400, fg='white', height=3)
    label_link.pack()

    link = StringVar()
    link_field = Entry(window, textvariable=link, font=('Arial', 14, 'bold'), width=40)
    link_field.pack()

    var = IntVar()
    R1 = Radiobutton(window, text="Audio", bg='black', variable=var, font=('Arial', 11, 'bold'), fg='white', value=1,
                     command=lambda: sel())
    R1.pack(padx=150, pady=10)

    R2 = Radiobutton(window, text="Video", bg='black', variable=var, font=('Arial', 11, 'bold'), fg='white', value=2,
                     command=lambda: sel())
    R2.pack(padx=150, pady=10)

    btn_submit = Button(window, text='Download', font=('Arial', 14), border=1, bg='red', fg='white', bd=0,
                        command=lambda: download_btn())
    btn_submit.pack()

    label_message = Label(window, text='Download Status', anchor=W, font=('Arial', 10, 'bold'),
                          bg='black', width=400, fg='white', height=3)
    label_message.pack(anchor=W)

    window.mainloop()
