import pyttsx3
import PyPDF2
from tkinter.filedialog import *
book = askopenfilename()
reader= PyPDF2.PdfFileReader(book)
pages = reader.numPages
for num in range(0,pages):
    page = reader.getPage(num)
    txt = page.extractText()
    player = pyttsx3.init()
    player.say(txt)
    player.runAndWait()
    player.setProperty('rate',160)