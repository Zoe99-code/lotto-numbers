# Zoe Strachan, Group 2
# Import everything

import datetime
import tkinter
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk


# Clear Button
def reset():
    fullname_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)
    identity_entry.delete(0, END)


def close():
    root.destroy()


# defining ID entry
def start():
    date_time = datetime.datetime.now()
    for x in range(int(identity_entry.get())):
        result = int(identity_entry.get()[0:3]) - int(date_time.strftime("%y"))
        if result >= 18:
            messagebox.showerror("Error", "You are too young to play, please try again later...")
            break
        else:
            messagebox.askyesno("Congratulations", "Are you ready?")
            if "yes":
                root.destroy()
                import extra

root = Tk()
root.geometry("600x600")
root.title("Lotto Numbers Challenge")
root.config(bg="lime")
root.resizable(0, 0)



image = Image.open("lotto-image.jpeg")
test = ImageTk.PhotoImage(image)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=100, y=50)
# name entries
fullname = Label(root, text='Full Name:', bg='white')
fullname.place(x=10, y=250)
fullname_entry = Entry(root, bg='grey12', width=20, fg='white')
fullname_entry.place(x=150, y=250)
email = Label(root, text='Email Address:', bg='white')
email.place(x=10, y=300)
email_entry = Entry(root, bg='grey12', width=20, fg='white')
email_entry.place(x=150, y=300)
address = Label(root, text='Address:', bg='white')
address.place(x=10, y=350)
address_entry = Entry(root, bg='grey12', width=20, fg='white')
address_entry.place(x=150, y=350)
identity = Label(root, text='Identity Number:', bg='white')
identity.place(x=10, y=400)
identity_entry = Entry(root, bg='grey12', width=20, fg='white')
identity_entry.place(x=150, y=400)
# my buttons
clear_button = Button(root, text='Clear', bg='gray80', borderwidth=5, fg='gray12', font=('Georgia', 10, 'bold'),
                      command=reset)
clear_button.place(x=100, y=460)
play_button = Button(root, text='Play', bg='gray80', borderwidth=5, fg='gray12', font=('Georgia', 10, 'bold'),
                     command=start)
play_button.place(x=180, y=460)
exit_button = Button(root, text='Exit', bg='gray80', borderwidth=5, fg='gray12', font=('Georgia', 10, 'bold'),
                     command=close)
exit_button.place(x=260, y=460)

root.mainloop()
