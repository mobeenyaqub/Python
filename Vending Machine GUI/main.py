from tkinter import *


class VendingMachine:
    def __init__(self):
        self.window = Tk()
        self.window.title("Vending Machine")
        self.window.minsize(width=500, height=300)
        self.window.config(pady=10, padx=10)
        self.total = 0

    def button_clicked(self, price=0, checkout=False):
        label = Label()
        if checkout:
            label.config(text=f"Total: {self.total}", font=("Arial", 30, "bold"))
            self.total = 0
        else:
            label.config(text=f"Price: {price}", font=("Arial", 24, "italic"))

        label.grid(row=1, column=3, pady=30, columnspan=2, sticky="ew")
        self.total += price

    def mainloop(self):
        self.window.mainloop()

    def buttons(self):
        cmd = self.button_clicked
        self.button = [
            Button(text="Lay's", command=lambda: cmd(80)),
            Button(text="Pringles", command=lambda: cmd(350)),
            Button(text="Doritos", command=lambda: cmd(800)),
            Button(text="KitKat", command=lambda: cmd(200)),
            Button(text="Snickers", command=lambda: cmd(180)),
            Button(text="Mars", command=lambda: cmd(160)),
            Button(text="Galaxy", command=lambda: cmd(350)),
            Button(text="Bounty", command=lambda: cmd(200)),
            Button(text="Reese's", command=lambda: cmd(250)),
            Button(text="Twix", command=lambda: cmd(180)),
            Button(text="Pepsi", command=lambda: cmd(120)),
            Button(text="7UP", command=lambda: cmd(120)),
        ]
        c = 1
        for i in range(len(self.button) // 2):
            self.button[i].grid(column=c, row=2, padx=5, pady=5)
            self.button[i].config(pady=10, padx=15)
            c += 1

        c = 1
        for i in range(len(self.button) // 2, len(self.button)):
            self.button[i].grid(column=c, row=3, padx=5, pady=5)
            self.button[i].config(pady=10, padx=15)
            c += 1

        checkout = Button(text="Checkout", command=lambda: cmd(0, True), font=("Arial", 20, "bold"))
        checkout.grid(columnspan=2, row=4, column=3, pady=20)


vm = VendingMachine()
vm.button_clicked()
vm.buttons()
vm.mainloop()
