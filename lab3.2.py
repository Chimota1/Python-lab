import tkinter as tk
import re
from tkinter import Entry, Label

def output_REGEXcount():
    user_text = text.get()
    find = re.findall(r"[A-ZА-Я]{2,}", user_text)
    lbl_count.config(text=len(find))

def outputText():
    lbl_output.config(text=text.get())

def delete_REGEX():
    user_text = text.get()
    find = delete_input.get()
    if find:
        new_text = re.sub(find, "", user_text)
        lbl_deleted.config(text=new_text)

def change_text():
    user_text = text.get()
    find = r"[A-ZА-Я]{2,}"
    new_text = lbl_changed_input.get()
    if new_text:
        result = re.sub(find, new_text, user_text)
        lbl_changed.config(text=result)


root = tk.Tk()
Label(root, text="Enter the sentence: ").grid(row=0, column=0)
text = Entry(root, width=40)
text.grid(row=1, column=0)

lbl_output = Label(root, text="")
lbl_output.grid(row=2, column=0)

lbl_count_text = Label(root, text="Count:")
lbl_count_text.grid(row=4, column=0)
lbl_count = Label(root, text="0")
lbl_count.grid(row=4, column=1)

lbl_deleted_text = Label(root, text="Deleted Text:")
lbl_deleted_text.grid(row=5, column=0)
lbl_deleted = Label(root, text="")
lbl_deleted.grid(row=5, column=1)

lbl_changed_text = Label(root, text="Changed Text:")
lbl_changed_text.grid(row=6, column=0)
lbl_changed = Label(root, text="")
lbl_changed_input = Entry(root, width=30)
lbl_changed_input.grid(row=6, column=1)
lbl_changed.grid(row=6, column=2)

btnOutput = tk.Button(root, text="Output", command=outputText)
btnOutput.grid(row=1, column=1)

button = tk.Button(root, text="Output quantity", command=output_REGEXcount)
button.grid(row=3, column=0)

delete_input = Entry(root, width=20)
delete_input.grid(row=3, column=1)
buttonDel = tk.Button(root, text="Remove atrib", command=delete_REGEX)
buttonDel.grid(row=3, column=2)

buttonChange = tk.Button(root, text="Change text", command=change_text)
buttonChange.grid(row=7, column=0)

root.geometry("600x700")
root.resizable(False, False)
root.mainloop()
