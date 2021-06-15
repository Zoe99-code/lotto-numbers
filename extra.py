from tkinter import *
from random import sample
from tkinter import messagebox

root = Tk()
root.geometry("600x500")
root.title("Lotto Numbers Generation")
root.config(bg="lime")
root.resizable(0, 0)

label1 = LabelFrame(root, text="Entry Numbers", bg="lime", pady=10)
label1.pack(fill="both")

entry1 = Entry(label1, width=5)
entry2 = Entry(label1, width=5)
entry3 = Entry(label1, width=5)
entry4 = Entry(label1, width=5)
entry5 = Entry(label1, width=5)
entry6 = Entry(label1, width=5)

entry1.grid(row=1, column=1, padx=25)
entry2.grid(row=1, column=2, padx=25)
entry3.grid(row=1, column=3, padx=25)
entry4.grid(row=1, column=4, padx=25)
entry5.grid(row=1, column=5, padx=25)
entry6.grid(row=1, column=6, padx=25)


def user_entries():
    int1 = int(entry1.get())
    int2 = int(entry2.get())
    int3 = int(entry3.get())
    int4 = int(entry4.get())
    int5 = int(entry5.get())
    int6 = int(entry6.get())

    List = [int1, int2, int3, int4, int5, int6]
    return List


def random_list():
    random_list = sample(range(1, 49), 6)
    random_list.sort()
    label3.configure(text=random_list)

    counter = 0
    for numbers in user_entries():
        if numbers in random_list:
            counter += 1
        if counter <= 1:
            messagebox.showinfo("Sorry", "Better Luck Again Next Time.")
            break

        elif counter == 2:
            messagebox.showinfo("Congratulations", "You won R20.")
            break

        elif counter == 3:
            messagebox.showinfo("Congratulations", "You won R100.")
            break

        elif counter == 4:
            messagebox.showinfo("Congratulations", "You won R2,384.00.")
            break

        elif counter == 5:
            messagebox.showinfo("Congratulations", "You won R2,384.00.")
            break

        elif counter == 6:
            messagebox.showinfo("CONGRATULATIONS!", "You won R10,000 000.00")
            break

play_btn = Button(root, text="Play", borderwidth=10, command=random_list)
play_btn.place(x=15, y=135)

play_btn.configure(command=random_list)

label2 = Label(root, text="Lotto Numbers!")
label2.place(x=10, y=85)

label3 = Label(root)
label3.place(x=130, y=85)

root.mainloop()
