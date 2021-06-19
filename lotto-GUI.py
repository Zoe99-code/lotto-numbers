# Zoe Strachan, Group 2
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

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


def identity(age):
    if age >= 18:
        messagebox.showinfo("Welcome", "Select Yes To Start The Game.")
    elif age < 18:
        messagebox.showinfo("Error", "You Are Too Young To Proceed To The Game.")
    else:
        messagebox.showinfo("Invalid Identity Number", "You May Not Proceed.")


class Information:
    def __init__(self, master):
        self.master = master
        self.root = root
        self.fullname = Label(root, text='Full Name:', bg="grey12", fg='white')
        self.fullname.place(x=10, y=250)
        self.fullname_entry = Entry(root, width=20)
        self.fullname_entry.place(x=150, y=250)
        self.email = Label(root, text='Email Address:', bg="grey12", fg='white')
        self.email.place(x=10, y=300)
        self.email_entry = Entry(root, width=20)
        self.email_entry.place(x=150, y=300)
        self.address = Label(root, text='Address:', bg="grey12", fg='white')
        self.address.place(x=10, y=350)
        self.address_entry = Entry(root, width=20)
        self.address_entry.place(x=150, y=350)
        self.identity = Label(root, text='Identity Number:', bg="grey12", fg='white')
        self.identity.place(x=10, y=400)
        self.identity_entry = Entry(root, width=20)
        self.identity_entry.place(x=150, y=400)
        self.clear_button = Button(root, text='Clear', bg="royalblue", borderwidth=5, font=('Georgia', 10, 'bold'),
                                   command=self.reset)
        self.clear_button.place(x=100, y=460)
        self.play_button = Button(root, text='Confirm', bg="royalblue", borderwidth=5, font=('Georgia', 10, 'bold'),
                                  command=self.start)
        self.play_button.place(x=200, y=460)
        self.exit_button = Button(root, text='Exit', bg="royalblue", borderwidth=5, font=('Georgia', 10, 'bold'),
                                  command=self.close)
        self.exit_button.place(x=320, y=460)

    def start(self):
        self.fullname = ["Zoe Strachan"]
        self.address = ["75 Black Crescent"]
        self.identity = ["9908080293088"]
        self.email = ["lizzystrachan99@gmail.com"]

        found = False
        for x in range(len(self.fullname)):
            if self.fullname_entry.get() == self.fullname[x] and self.address_entry.get() == self.address[x] and \
                    self.identity_entry.get() == self.identity[x] and self.email_entry.get() == self.email[x]:
                found = True

        if found:
            root.destroy()
            import gamescreen

    def reset(self):
        self.fullname_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.identity_entry.delete(0, END)

    def close(self):
        self.root.destroy()


information = Information(root)

root.mainloop()
