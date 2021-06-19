from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("600x600")
root.title("Email")
root.config(bg="lime")
root.resizable(0, 0)


details = Label(root, bg="grey12", fg="white", text="ENTER BANKING DETAILS", justify="center")
details.place(x=150, y=10)
full_name = Label(root, bg="grey12", fg="white", text="Enter Full Name: ")
full_name.place(x=0, y=50)
full_name = Entry(root)
full_name.place(x=170, y=50)

d_o_b = Label(root, bg="grey12", fg="white", text="Enter Date Of Birth: ")
d_o_b.place(x=0, y=150)
d_o_b = Entry(root)
d_o_b.place(x=170, y=150)

identity_number = Label(root, bg="grey12", fg="white", text="Enter ID Number: ")
identity_number.place(x=0, y=200)
identity_number = Entry(root)
identity_number.place(x=170, y=200)
contact_number = Label(root, bg="grey12", fg="white", text="Enter Contact Number: ")
contact_number.place(x=0, y=250)
contact_number = Entry(root)
contact_number.place(x=170, y=250)
city = Label(root, bg="grey12", fg="white", text="Citizen: ")
city.place(x=0, y=300)
city = Entry(root)
city.place(x=170, y=300)
bank = Label(root, bg="grey12", fg="white", text="Select Bank: ")
bank.place(x=0, y=350)

var = StringVar()
category_list = ttk.Combobox(root, textvariable=var, width=18, value=["ABSA", "FNB", "Nedbank", "Standard Bank"])
category_list.place(x=170, y=350)

account = Label(root, bg="grey12", fg="white", text="Enter Account Number: ")
account.place(x=0, y=400)

account = Entry(root)
account.place(x=170, y=400)

branch = Label(root, bg="grey12", fg="white", text="Branch Code: ")
branch.place(x=0, y=450)
branch = Entry(root)
branch.place(x=170, y=450)

proceed_button = Button(root, text="Proceed", bg="royalblue", font=('Georgia', 10, 'bold'), borderwidth=10, command="", justify="center")
proceed_button.place(x=180, y=500)


def clear():
    full_name.delete(0, END)
    identity_number.delete(0, END)
    contact_number.delete(0, END)
    city.delete(0, END)
    d_o_b.delete(0, END)
    account.delete(0, END)
    branch.delete(0, END)


root.mainloop()
