from tkinter import *

root = Tk()
root.geometry("600x600")
root.title("Claim Prize")
root.config(bg="lime")
root.resizable(0, 0)


class Score:
    def __init__(self):
        self.root = None
        self.root = root
        self.score = Label(root, bg="grey12", fg="white", text="Score")
        self.score.place(x=0, y=10)
        self.prize = Label(root, bg="grey12", fg="white", text="Prize")
        self.prize.place(x=150, y=10)
        self.number1 = Label(root, bg="grey12", fg="white", text="6 correct numbers")
        self.number1.place(x=0, y=50)
        self.winnings1 = Label(root, bg="grey12", fg="white", text='R10,000 000.00')
        self.winnings1.place(x=150, y=50)
        self.number2 = Label(root, bg="grey12", fg="white", text="5 correct numbers")
        self.number2.place(x=0, y=100)
        self.winnings2 = Label(root, bg="grey12", fg="white", text="R8,584.00")
        self.winnings2.place(x=150, y=100)
        self.number3 = Label(root, bg="grey12", fg="white", text="4 correct numbers")
        self.number3.place(x=0, y=150)
        self.winnings3 = Label(root, bg="grey12", fg="white", text="R2,384.00")
        self.winnings3.place(x=150, y=150)
        self.number4 = Label(root, bg="grey12", fg="white", text="3 correct numbers")
        self.number4.place(x=0, y=200)
        self.winnings4 = Label(root, bg="grey12", fg="white", text="R100.50")
        self.winnings4.place(x=150, y=200)
        self.number5 = Label(root, bg="grey12", fg="white", text="2 correct numbers")
        self.number5.place(x=0, y=250)
        self.winnings5 = Label(root, bg="grey12", fg="white", text="R20.00")
        self.winnings5.place(x=150, y=250)
        self.number6 = Label(root, bg="grey12", fg="white", text="1 correct number")
        self.number6.place(x=0, y=300)
        self.winnings6 = Label(root, bg="grey12", fg="white", text="R0.00")
        self.winnings6.place(x=150, y=300)
        self.number7 = Label(root, bg="grey12", fg="white", text="0 correct numbers")
        self.number7.place(x=0, y=350)
        self.winnings7 = Label(root, bg="grey12", fg="white", text="R0.00")
        self.winnings7.place(x=150, y=350)
        self.play_button = Button(root, text="Play Again", borderwidth=10, font=('Georgia', 10, 'bold'), bg="royalblue",
                                  command=self.play)
        self.play_button.place(x=0, y=400)
        self.continue_button = Button(root, text="Continue", borderwidth=10, font=('Georgia', 10, 'bold'),
                                      bg="royalblue",
                                      command=self.continue_button)
        self.continue_button.place(x=150, y=400)
        self.exit_button = Button(root, text="Exit", borderwidth=10, font=('Georgia', 10, 'bold'), bg="royalblue",
                                  command=self.exit_button)
        self.exit_button.place(x=300, y=400)

    def play(self):
        self.root.destroy()
        import gamescreen

    def continue_button(self):
        self.root.destroy()
        import email

    def exit_button(self):
        self.root.destroy()


score = Score()

root.mainloop()
