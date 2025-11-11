import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Solution")

path = "file.txt"
content = ""
stack = []

def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
    return content

content = read_file(path)

for c in content:
    if c == "(":
        stack.append(c)
    elif c == ")":
        if stack:
            stack.pop()

if stack is None:
    Label = Label(root, text="Balanced", font=("Arial", 14))
    Label.pack(pady=20)
else:
    Label = Label(root, text="Unbalanced", font=("Arial", 14))
    Label.pack(pady=20)

root.mainloop()