from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import Image
import pytesseract
root = Tk()
root.geometry("250x300")
def readphoto():
    path = PathTextBox.get('1.0', 'end-1c')
    if path:
        im = Image.open(path)
        text = pytesseract.image_to_string(im, lang='eng')
        #ResultTextBox.delete('1.0', END)
        ResultTextBox.insert(END,text + '\n')
    else:
        ResultTextBox.delete('1.0', END)
        ResultTextBox.insert(END, "ERROR")
def showFile():
    name = askopenfilename(initialdir="/",
                           filetypes=(("PNG File", "*.png"), ("BMP File", "*.bmp"), ("JPEG File", "*.jpeg")),
                           title="Choose a file."
                           )
    PathTextBox.delete("1.0", END)
    PathTextBox.insert(END, name)
Title = root.title("Image shower")
path = StringVar()
InputLabel = Label(root, text="Insert image:")
InputLabel.grid(row=2, column=0)
BrowseButton = Button(root, text="Find image", command=showFile)
BrowseButton.grid(row=3, column=0)
PathLabel = Label(root, text="From:")
PathLabel.grid(row=4, column=0)
PathTextBox = Text(root, height=2)
PathTextBox.grid(row=5, column=0, columnspan=2)
ReadButton = Button(root, text="scan image", command=readphoto)
ReadButton.grid(row=6, column=0)
DataLabel = Label(root, text="Result:")
DataLabel.grid(row=7, column=0)
ResultTextBox = Text(root, height=6)
ResultTextBox.grid(row=7, column=1, columnspan=2)
root.mainloop()
