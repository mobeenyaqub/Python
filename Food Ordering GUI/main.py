from tkinter import ttk
from tkinter import *


class VendingMachine:
    def __init__(self):
        self.window = Tk()
        self.window.title("Vending Machine")
        self.window.minsize(width=500, height=300)
        self.window.config(pady=10, padx=10)

        self.label = Label(text="Enter name below", font=("Arial", 16, "italic"))
        self.label.grid(row=1, column=2, sticky="ew", columnspan=2)

        self.name = Entry(bg="white", width=40, borderwidth=2)
        self.name.grid(row=2, column=2, pady=20, columnspan=2)

        self.comboboxes = []

        self.items = ["Lay's", 'Pringles', 'Doritos', '7UP', 'KitKat', 'Snickers',
                      'Mars', 'Galaxy', "Bounty", "Reese's", 'Twix', 'Pepsi']
        self.qty = []
        self.prices = [80, 350, 800, 120, 200, 180, 160, 350, 200, 250, 180, 120]
        self.total = 0

    def button_clicked(self):
        self.name = self.name.get()
        for i in range(len(self.comboboxes)):
            qty = int(self.comboboxes[i].get())
            if qty <= 10:
                self.total += qty * self.prices[i]
                self.qty.append(qty)
            else:
                self.qty.append(0)

        self.window.destroy()

        self.bill_generator()

    def bill_generator(self):
        bill = Tk()
        bill.title("Total Bill")
        bill.minsize(width=50, height=50)
        bill.config(padx=10, pady=10)

        label = Label(text=f"{self.name}'s Bill", font=("Arial", 16, "bold", "italic"), padx=10, pady=20)

        label.grid(row=1, columnspan=2, column=1)
        labels = [
            Label(),
            Label(),
            Label(),
            Label(),
            Label(),
            Label(),
            Label(),
            Label(),
            Label(),
            Label(),
            Label(),
            Label()
        ]

        heading = Label(text="Product ❌ Qty = Price", font=("Arial", 16, "underline", "italic"))
        heading.grid(row=2, column=1, pady=10)

        r = 3
        c = 1

        for i in range(len(labels)):
            if self.qty[i] > 0:
                labels[i].config(text=f"{self.items[i]} ❌ {self.qty[i]}   =   Rs. {self.prices[i] * self.qty[i]}",
                                 font=("Arial", 12))
                labels[i].grid(row=r, column=c, pady=5)
                r += 1

        label = Label(text=f"Grand Total: Rs. {self.total}", font=("Arial", 18, "bold", "italic"), pady=20)
        label.grid(row=15, column=1)

        if self.total > 0:
            money_label = Label(text="Enter Money:", font=("Arial", 12, "italic"))
            money_label.grid(row=16, column=1)
            enter_money = Entry()
            enter_money.grid(row=17, column=1)

            process_order = Button(text="Process Order", font=("Arial", 12, "bold"), command=lambda: self.order_processing(int(enter_money.get())))
            process_order.grid(row=18, column=1, columnspan=2, pady=10)

        bill.mainloop()

    def order_processing(self, money):
        label = Button(font=("Arial", 14, "bold", "italic"), borderwidth=0)
        if money == self.total:
            label.config(text="Enjoy your snack!")
        elif money < self.total:
            label.config(text="Insufficient funds!")
        else:
            label.config(text=f"Your change: Rs.{money - self.total}\nEnjoy your snack!")

        label.grid(row=18, column=1, sticky="ew")

    def mainloop(self):
        self.window.mainloop()

    def buttons(self):
        labels = [
            Label(),
            Label(),
            Label(),
            Label(),
            Label(),
            Label(),
            Label(),
            Label(),
            Label(),
            Label(),
            Label(),
            Label()
        ]

        self.comboboxes = [
            ttk.Combobox(self.window, values=[i for i in range(11)]),
            ttk.Combobox(self.window, values=[i for i in range(11)]),
            ttk.Combobox(self.window, values=[i for i in range(11)]),
            ttk.Combobox(self.window, values=[i for i in range(11)]),
            ttk.Combobox(self.window, values=[i for i in range(11)]),
            ttk.Combobox(self.window, values=[i for i in range(11)]),
            ttk.Combobox(self.window, values=[i for i in range(11)]),
            ttk.Combobox(self.window, values=[i for i in range(11)]),
            ttk.Combobox(self.window, values=[i for i in range(11)]),
            ttk.Combobox(self.window, values=[i for i in range(11)]),
            ttk.Combobox(self.window, values=[i for i in range(11)]),
            ttk.Combobox(self.window, values=[i for i in range(11)])
        ]

        for i in range(len(self.comboboxes)):
            self.comboboxes[i].current(0)

        c = 1
        r = 3
        for i in range(len(labels)):
            if i % 4 == 0:
                r += 2
                c = 1

            labels[i].grid(column=c, row=r, padx=5, pady=5)
            labels[i].config(text=f"{self.items[i]} ({self.prices[i]})", pady=5, padx=15, font=("Arial", 12, "italic"))
            self.comboboxes[i].grid(column=c, row=r + 1, pady=5, padx=5)
            c += 1

        generate_bill = Button(text="Generate Bill", command=self.button_clicked, font=("Arial", 20, "bold"),
                               bg="#E5E5E5", borderwidth=2)
        generate_bill.grid(columnspan=2, row=11, column=2, pady=20)


vm = VendingMachine()
vm.buttons()
vm.mainloop()
