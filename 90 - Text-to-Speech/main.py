import pyttsx3
import PyPDF2
from tkinter import *
from tkinter.filedialog import askopenfilename

window = Tk()
window.title("Text-to-speech")
window.minsize(width=250, height=100)
window.config(padx=70, pady=70)

filename = ""


def choose_file():
    global filename
    filename = askopenfilename()


def play_pdf():
    global filename
    with open(filename, 'rb') as file_to_read:
        pdf_reader = PyPDF2.PdfFileReader(file_to_read)
        total_pages = pdf_reader.numPages

        for i in range(total_pages):
            page = pdf_reader.getPage(i)
            page_to_read = page.extractText()
            print(page_to_read)
            engine = pyttsx3.init()
            engine.say(page_to_read)
            engine.runAndWait()


button_upload = Button(text="Upload PDF", command=choose_file, )
button_upload.grid(column=1, row=0, padx=20, pady=20)
button_play = Button(text="Play PDF", command=play_pdf)
button_play.config(padx=20, pady=20)
button_play.grid(column=1, row=1)

window.mainloop()
