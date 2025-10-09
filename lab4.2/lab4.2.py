import tkinter as tk
from tkinter import Label, Entry, Button
import re

root = tk.Tk()
file1 = "D:\\PKPZ\\Python-lab\\lab4.2\\TF_1.txt"
file2 = "D:\\PKPZ\\Python-lab\\lab4.2\\TF_2.txt"
find = re.findall(r"\b\w*[aA]\w*\b", open(file1, "r", encoding="utf-8").read())
count = 0
Label(root, text="Sentence from txt file: ").grid(row=0, column=1)
Label(root, text=open(file1, "r", encoding="utf-8").read()).grid(row=1, column=0)
Label(root, text="Word with 'a' in the sentence: ").grid(row=3, column=1)
if (len(find) > 0):
    for i in find:
        open(file2, "a", encoding="utf-8").write(i + "\n")
    Label(root, text=find).grid(row=4, column=0)
else:
    open(file2, "w", encoding="utf-8").write("Not match")
    Label(root, text="Not match").grid(row=4, column=0)

root.geometry("600x400")
root.mainloop()