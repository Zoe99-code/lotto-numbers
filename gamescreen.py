from tkinter import *
from random import sample
from tkinter import messagebox

root = Tk()
root.geometry("600x600")
root.title("Lotto Numbers Generation")
root.config(bg="lime")
root.resizable(0, 0)
list1 = []
list2 = []
list3 = []


def run(num):
    if len(list1) == 5:
        click_button.config(state=NORMAL)
    elif len(list1) < 5:
        click_button.config(state=DISABLED)
    if len(list1) < 6 and num not in list1:
        list1.append(num)
        set1.config(text=list1)
    elif len(list1) == 6 and len(list2) < 6 and num not in list2:
        list2.append(num)
        set2.config(text=list2)
    elif len(list2) == 6 and len(list1) == 6 and len(list3) < 6 and num not in list3:
        list3.append(num)
        set3.config(text=list3)
    if len(list3) == 6:
        button1.config(state=DISABLED)
        button2.config(state=DISABLED)
        button3.config(state=DISABLED)
        button4.config(state=DISABLED)
        button5.config(state=DISABLED)
        button6.config(state=DISABLED)
        button7.config(state=DISABLED)
        button8.config(state=DISABLED)
        button9.config(state=DISABLED)
        button10.config(state=DISABLED)
        button11.config(state=DISABLED)
        button12.config(state=DISABLED)
        button13.config(state=DISABLED)
        button14.config(state=DISABLED)
        button15.config(state=DISABLED)
        button16.config(state=DISABLED)
        button17.config(state=DISABLED)
        button18.config(state=DISABLED)
        button19.config(state=DISABLED)
        button20.config(state=DISABLED)
        button21.config(state=DISABLED)
        button22.config(state=DISABLED)
        button23.config(state=DISABLED)
        button24.config(state=DISABLED)
        button25.config(state=DISABLED)
        button26.config(state=DISABLED)
        button27.config(state=DISABLED)
        button28.config(state=DISABLED)
        button29.config(state=DISABLED)
        button30.config(state=DISABLED)
        button31.config(state=DISABLED)
        button32.config(state=DISABLED)
        button33.config(state=DISABLED)
        button34.config(state=DISABLED)
        button35.config(state=DISABLED)
        button36.config(state=DISABLED)
        button37.config(state=DISABLED)
        button38.config(state=DISABLED)
        button39.config(state=DISABLED)
        button40.config(state=DISABLED)
        button41.config(state=DISABLED)
        button42.config(state=DISABLED)
        button44.config(state=DISABLED)
        button43.config(state=DISABLED)
        button45.config(state=DISABLED)
        button46.config(state=DISABLED)
        button47.config(state=DISABLED)
        button48.config(state=DISABLED)
        button49.config(state=DISABLED)


button1 = Button(root, text=1, command=lambda: run(1))
button1.place(x=20, y=10)
button2 = Button(root, text=2, command=lambda: run(2))
button2.place(x=60, y=10)
button3 = Button(root, text=3, command=lambda: run(3))
button3.place(x=100, y=10)
button4 = Button(root, text=4, command=lambda: run(4))
button4.place(x=140, y=10)
button5 = Button(root, text=5, command=lambda: run(5))
button5.place(x=180, y=10)
button6 = Button(root, text=6, command=lambda: run(6))
button6.place(x=220, y=10)
button7 = Button(root, text=7, command=lambda: run(7))
button7.place(x=260, y=10)
button8 = Button(root, text=8, command=lambda: run(8))
button8.place(x=300, y=10)
button9 = Button(root, text=9, command=lambda: run(9))
button9.place(x=340, y=10)
button10 = Button(root, text=10, width=1, command=lambda: run(10))
button10.place(x=20, y=50)
button11 = Button(root, text=11, width=1, command=lambda: run(11))
button11.place(x=60, y=50)
button12 = Button(root, text=12, width=1, command=lambda: run(12))
button12.place(x=100, y=50)
button13 = Button(root, text=13, width=1, command=lambda: run(13))
button13.place(x=140, y=50)
button14 = Button(root, text=14, width=1, command=lambda: run(14))
button14.place(x=180, y=50)
button15 = Button(root, text=15, width=1, command=lambda: run(15))
button15.place(x=220, y=50)
button16 = Button(root, text=16, width=1, command=lambda: run(16))
button16.place(x=260, y=50)
button17 = Button(root, text=17, width=1, command=lambda: run(17))
button17.place(x=300, y=50)
button18 = Button(root, text=18, width=1, command=lambda: run(18))
button18.place(x=340, y=50)
button19 = Button(root, text=19, width=1, command=lambda: run(19))
button19.place(x=20, y=90)
button20 = Button(root, text=20, width=1, command=lambda: run(20))
button20.place(x=60, y=90)
button21 = Button(root, text=21, width=1, command=lambda: run(21))
button21.place(x=100, y=90)
button22 = Button(root, text=22, width=1, command=lambda: run(22))
button22.place(x=140, y=90)
button23 = Button(root, text=23, width=1, command=lambda: run(23))
button23.place(x=180, y=90)
button24 = Button(root, text=24, width=1, command=lambda: run(24))
button24.place(x=220, y=90)
button25 = Button(root, text=25, width=1, command=lambda: run(25))
button25.place(x=260, y=90)
button26 = Button(root, text=26, width=1, command=lambda: run(26))
button26.place(x=300, y=90)
button27 = Button(root, text=27, width=1, command=lambda: run(27))
button27.place(x=340, y=90)
button28 = Button(root, text=28, width=1, command=lambda: run(28))
button28.place(x=20, y=130)
button29 = Button(root, text=29, width=1, command=lambda: run(29))
button29.place(x=60, y=130)
button30 = Button(root, text=30, width=1, command=lambda: run(30))
button30.place(x=100, y=130)
button31 = Button(root, text=31, width=1, command=lambda: run(31))
button31.place(x=140, y=130)
button32 = Button(root, text=32, width=1, command=lambda: run(32))
button32.place(x=180, y=130)
button33 = Button(root, text=33, width=1, command=lambda: run(33))
button33.place(x=220, y=130)
button34 = Button(root, text=34, width=1, command=lambda: run(34))
button34.place(x=260, y=130)
button35 = Button(root, text=35, width=1, command=lambda: run(35))
button35.place(x=300, y=130)
button36 = Button(root, text=36, width=1, command=lambda: run(36))
button36.place(x=340, y=130)
button37 = Button(root, text=37, width=1, command=lambda: run(37))
button37.place(x=20, y=170)
button38 = Button(root, text=38, width=1, command=lambda: run(38))
button38.place(x=60, y=170)
button39 = Button(root, text=39, width=1, command=lambda: run(39))
button39.place(x=100, y=170)
button40 = Button(root, text=40, width=1, command=lambda: run(40))
button40.place(x=140, y=170)
button41 = Button(root, text=41, width=1, command=lambda: run(41))
button41.place(x=180, y=170)
button42 = Button(root, text=42, width=1, command=lambda: run(42))
button42.place(x=220, y=170)
button43 = Button(root, text=43, width=1, command=lambda: run(43))
button43.place(x=260, y=170)
button44 = Button(root, text=44, width=1, command=lambda: run(44))
button44.place(x=300, y=170)
button45 = Button(root, text=45, width=1, command=lambda: run(45))
button45.place(x=340, y=170)
button46 = Button(root, text=46, width=1, command=lambda: run(46))
button46.place(x=20, y=210)
button47 = Button(root, text=47, width=1, command=lambda: run(47))
button47.place(x=60, y=210)
button48 = Button(root, text=48, width=1, command=lambda: run(48))
button48.place(x=100, y=210)
button49 = Button(root, text=49, width=1, command=lambda: run(49))
button49.place(x=140, y=210)
total = Label(root, text="")
total.place(x=10, y=530)

set1 = Label(root, text='', bg='grey12', fg="white", width=15, justify='center')
set1.place(x=0, y=260)
set2 = Label(root, text='', bg='grey12', fg="white", width=15, justify='center')
set2.place(x=0, y=310)
set3 = Label(root, text='', bg='grey12', fg="white", width=15, justify='center')
set3.place(x=0, y=360)


def random():
    random_list = sample(range(1, 49), 6)
    random_list.sort()
    label3.configure(text=random_list)

    counter = 0
    for numbers in list1:
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


click_button = Button(root, text="Play", borderwidth=10, command=random)
click_button.place(x=180, y=210)

click_button.config(command=random)

label2 = Label(root, bg="grey12", fg="white", text="Lotto Numbers!")
label2.place(x=270, y=250)

label3 = Label(root, bg="grey12", fg="white")
label3.place(x=270, y=300)

root.mainloop()
