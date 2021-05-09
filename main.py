import pyttsx3
import PyPDF2
import tkinter as tk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

instructions = tk.Label(root, text="Select a PDF file on your computer to extract all its text", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)


def open_file():
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetype=[("Pdf file", "*.pdf")])
    if file:
        pdf_file = file.name

        with open(pdf_file, 'rb') as book:
            full_text = ""

            reader = PyPDF2.PdfFileReader(book)

            engine = pyttsx3.init()

            # velocidad
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate + 20)

            for page in range(reader.numPages):
                next_page = reader.getPage(page)
                content = next_page.extractText()
                full_text += content

    # engine.say(full_text)
    engine.save_to_file(full_text, 'eur.mp3')
    engine.runAndWait()


browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda: open_file(), font="Raleway", bg="#20bebe",
                       fg="white", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

root.mainloop()
