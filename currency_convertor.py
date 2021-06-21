from tkinter import *
from tkinter import messagebox
import tkinter as ttk
import requests

root = Tk()
root.geometry("600x600")
root.title("Currency Convertor")
root.config(bg="lime")
root.resizable(0, 0)

results = StringVar()
values1 = StringVar()
values2 = StringVar()

information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/USD')
information_json = information.json()

conversion_rates = information_json['conversion_rates']

currency = []
for i in conversion_rates.keys():
    currency.append(i)

currency2 = []
for i in conversion_rates.keys():
    currency2.append(i)

currency_cb = ttk.Combobox(root)
currency_cb['values'] = currency
currency_cb['state'] = 'readonly'
currency_cb.set('Select Currency')
currency_cb.place(x=10, y=280)

currency_cb2 = ttk.Combobox(root)
currency_cb2['values'] = currency2
currency_cb2['state'] = 'readonly'
currency_cb2.set('Select Currency')
currency_cb2.place(x=253, y=280)

Label(root, text='Enter Amount:').place(x=65, y=330)
ent1 = Entry(root)
ent1.place(x=200, y=330)
ent1.focus()
Label(root, text='Converted Amount:').place(x=65, y=380)
Label(root, text='', textvariable=results).place(x=200, y=380)


def convert(from_currency, to_currency, amount):
    if from_currency != 'USD':
        amount = amount / conversion_rates[from_currency]

    amount = round(amount * conversion_rates[to_currency], 4)
    return amount


def perform():
    try:
        amount = float(ent1.get())
        from_curr = currency_cb.get()
        to_curr = currency_cb2.get()

        converted_amount = convert(from_curr, to_curr, amount)

        results.set(converted_amount)
    except ValueError:
        if ent1 != int and ent1 != float:
            messagebox.showerror('Invalid Entry', 'Only Digits Allowed.')

    except requests.exceptions.ConnectionError:
        messagebox.showerror('Internet Connection Is Slow.', 'Retry Again Later.')
    except KeyError:
        messagebox.showerror('Error', 'Select Currency.')


def kill():
    return root.destroy()


def clear():
    currency_cb.set('Select Currency')
    currency_cb2.set('Select Currency')
    ent1.delete(0, END)
    ent1.focus()
    results.set('')


Button(root, text="Convert", borderwidth=5, command=perform).place(x=180, y=430)
Button(root, text="Exit", borderwidth=5, command=kill).place(x=281, y=480)
Button(root, text="Clear", borderwidth=5, command=clear).place(x=100, y=480)

root.mainloop()
