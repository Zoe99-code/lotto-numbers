from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x600")
root.title("Claim Prize")
root.config(bg="lime")
root.resizable(0, 0)


value_inside = StringVar(root)

value_inside.set("Select Bank")
bankoptions = ['ABSA', 'Capitec', 'FNB', 'Nedbank']

    class InvalidAccountName:
        pass

    title = Label(root, text='Claim your prize!')
    title.place(x=12, y=20)

    def bank(value_inside):
        if value_inside == 'Select Bank':
            pass
        else:
            accountNameEntry.config(state='normal')
            bankNrEntry.config(state='normal')

    bankselect = OptionMenu(root, value_inside, *bankoptions, command=bank)
    bankselect.place(x=30, y=100)
    accountNameLabel = Label(root, text="Account name")
    accountNameLabel.place(x=30, y=150)
    accountNameEntry = Entry(root, state='readonly')
    accountNameEntry.place(x=150, y=150)
    bankNrLabel = Label(root, text="Account Number")
    bankNrLabel.place(x=30, y=200)
    bankNrEntry = Entry(root, state='readonly')
    bankNrEntry.place(x=150, y=200)

    def claim():
        if accountNameEntry.get() == '' or bankNrEntry.get() == '':
            messagebox.showerror("Fields unfilled", "Please enter both account name and bank account number")
        else:
            try:
                banknr = int(bankNrEntry.get())
                if str.isalpha(accountNameEntry.get()) is False:
                    raise InvalidAccountName
                else:
                    messagebox.showinfo("test", score)
            except ValueError:
                messagebox.showerror("Invalid Bank Number", "Please enter valid bank number (digits only)")
            except InvalidAccountName:
                messagebox.showerror("Invalid Account Name", "Please enter valid account name (characters only")

claimBtn = Button(root, text="Claim", command=claim)
claimBtn.place(x=200, y=270)

root.mainloop()