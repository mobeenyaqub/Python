from tkinter import *
from tkinter import ttk
import requests
import iso4217parse

# fetch API response
URL = "https://openexchangerates.org/api/latest.json?app_id=3a7a1d3d1f97409ab8c24a9d8239808c"
response = requests.get(URL).json()

# initialize tkinter window
window = Tk()
window.title("Currency Converter")
window.config(padx=50, pady=20, bg="#1F2124")

# main heading of GUI
heading = Label(text="Currency Converter", font=("Arial", 24, "bold"), fg="#F0F0FF", bg="#1F2124")
heading.grid(column=2, row=1, pady=20)

# initializing currencies to use in the program
currencies = sorted(f"{iso4217parse.parse(c)[0][2]} ({c})".title() for c in sorted(response["rates"].keys()))

# labeling and setting the dropdown/combobox for currency selection
n = StringVar()
currency_select_label = Label(text="Select Currency", font=("Arial", 12, "underline"), bg="#1F2124", fg="#ffffff")
currency_select_label.grid(column=2, row=2, pady=10)
currency_select = ttk.Combobox(window, values=currencies, width=45, textvariable=n)
currency_select.grid(column=2, row=3)

# entry box for user to enter amount he/she wants to convert
enter_amount = Label(text="Enter amount", font=("Arial", 11, "italic", "underline"), bg="#1F2124", fg="#ffffff")
enter_amount.grid(column=2, row=4, pady=10)
amount_to_convert = Entry(width=25)
amount_to_convert.grid(column=2, row=5)

# dropdown for currency to convert into
convert_into_label = Label(text=f"Convert currency into", font=("Arial", 12, "underline"), bg="#1F2124", fg="#ffffff")
convert_into_label.grid(column=2, row=6, pady=10)
m = StringVar()
convert_into = ttk.Combobox(window, values=currencies, width=45, textvariable=m)
convert_into.grid(column=2, row=7)
converted = Label()


# convert button function
def convert():
    global converted
    # converted currency label
    converted = Label(font=("Arial", 11, "bold"), fg="#ffffff", bg="#1F2124", pady=10)

    try:
        # save amount
        amount = int(amount_to_convert.get())

        # saving the user input of currency to convert from
        currency_1 = currency_select.get()[-4:-1]

        # saving the currency to convert to
        currency_2 = convert_into.get()[-4:-1]

        # fetch required values from API rates
        val_c1, val_c2 = response["rates"][currency_1], response["rates"][currency_2]

        # display converted currency
        converted.config(
            text=f"\n1 {currency_1} = {round(val_c2 / val_c1, 4)} {currency_2}\n\n{amount:,.2f} {currency_1}"
                 f" = {round(val_c2 / val_c1 * amount, 2):,.2f} {currency_2}")
        converted.grid(column=2, row=8)
    except:
        pass


# convert currency button
convert_button = Button(text="Convert", width=12, font=("Arial", 20, "bold"), command=convert)
convert_button.grid(column=2, row=9, pady=25)


# reset button function
def reset():
    # reset all the states
    currency_select.delete(0, "end")
    convert_into.delete(0, "end")
    amount_to_convert.delete(0, "end")
    converted.destroy()


# reset button
reset_button = Button(text="Reset", width=10, font=("Arial", 15, "bold"), command=reset, bg="#FF0000", border=0)
reset_button.grid(column=2, row=10, pady=20)

# tkinter window loop
window.mainloop()
