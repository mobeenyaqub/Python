from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(width=300, height=200)
window.config(pady=30, padx=30)


def on_click():
    answer["text"] = 1.6 * float(text_box.get())


label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)

label_3 = Label(text="Km")
label_3.grid(column=2, row=1)

button = Button(text="Calculate", command=on_click)
button.grid(column=1, row=2)

text_box = Entry(width=10)
text_box.focus()
text_box.grid(column=1, row=0)

answer = Label(text=0)
answer.grid(column=1, row=1)
answer.config(padx=10, pady=10)

window.mainloop()
