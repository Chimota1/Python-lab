import tkinter as tk
from tkinter import Label, Entry, Button

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def CountOfPages(self,pages):
        return pages

    def Show(self):
        return f"Title : {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __del__(self):
        print("Created by Anatolii Kindrat 243(1)")

class Gournal(Book):

    def __init__(self, title, author, pages):
        super().__init__(title, author, pages)

    def CountOfPages(self,pages):
        return pages // 2

    def Show(self):
         return f"Title : {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __del__(self):
        print("Destructor of Gournal class")

class TextBook(Book):

    def __init__(self, title, author, pages):
        super().__init__(title,author,pages)

    def CountOfPages(self,pages):
        return pages * 2

    def Show(self):
        return f"Title : {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __del__(self):
        print("Destructor of TextBook class")

class PrintedEdition(Book):

    def __init__(self, title, author, pages):
        super().__init__(title,author,pages)

    def CountOfPages(self,pages):
        return pages * 5

    def Show(self):
        return f"Title : {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __del__(self):
        print("Destructor of PrintedEdition class")

def bookButton():
    result.config(text = book.Show())

def gournalButton():
    result.config(text = gournal.Show())

def textBookButton():
    result.config(text = textbook.Show())

def printedEditionButton():
    result.config(text = printedEdition.Show())

def BookCountOfPages():
    result2.config(text= book.CountOfPages(0))

def GournalCountOfPages():
    result2.config(text= gournal.CountOfPages(30))

def TextBookCountOfPages():
    result2.config(text= textbook.CountOfPages(70))

def PrintedEditionCountOfPages():
    result2.config(text= printedEdition.CountOfPages(50))

book = Book("Unknown ", "Unknown", 0)
gournal = Gournal("Corruption", "UkrPravda", 30)
textbook = TextBook("Matematuka", "Merzlyak", 70)
printedEdition = PrintedEdition("Kharkiv", "Misk rada", 50)

root = tk.Tk()
root.geometry("800x600")
root.resizable(False, False)
root.title("Inheritance")
Title = Label(root, text="Title",font=("Arial", 20))
Title.pack(side=tk.TOP, fill=tk.X)
result = Label(root, text="")
result.pack(pady=10)
result2 = Label(root, text="")
result2.pack(pady=10)
ShowBook = Button(root, text="Show Book", command=bookButton)
ShowGournal = Button(root, text="Show Gournal", command=gournalButton)
ShowTextBook = Button(root, text="Show TextBook", command=textBookButton)
ShowPrintedEdition = Button(root, text="Show PrintedEdition", command=printedEditionButton)
CountBookOfPages = Button(root, text="Count Book of Pages", command=BookCountOfPages)
CountGournalOfPages = Button(root, text="Count Gournal of Pages", command=GournalCountOfPages)
CountTextbookOfPages = Button(root, text="Count Textbook of Pages", command=TextBookCountOfPages)
CountPrintedEditionOfPages = Button(root, text="Count Printed Edition", command=PrintedEditionCountOfPages)
CountBookOfPages.pack(side=tk.LEFT, fill=tk.X)
CountBookOfPages.pack(side=tk.BOTTOM, fill=tk.Y)
CountGournalOfPages.pack(side=tk.LEFT, fill=tk.X)
CountGournalOfPages.pack(side=tk.BOTTOM, fill=tk.Y)
CountTextbookOfPages.pack(side=tk.LEFT, fill=tk.X)
CountTextbookOfPages.pack(side=tk.BOTTOM, fill=tk.Y)
CountPrintedEditionOfPages.pack(side=tk.LEFT, fill=tk.X)
CountPrintedEditionOfPages.pack(side=tk.BOTTOM, fill=tk.Y)
ShowBook.pack(side=tk.LEFT, fill=tk.X)
ShowGournal.pack(side=tk.LEFT, fill=tk.X)
ShowTextBook.pack(side=tk.LEFT, fill=tk.X)
ShowPrintedEdition.pack(side=tk.LEFT, fill=tk.X)
root.mainloop()