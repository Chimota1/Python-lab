import datetime
import tkinter as tk
from tkinter import *
from datetime import *

root = tk.Tk()
root.title("UKRZALIZNYTSYA")

marschrut = ''
number = 0
number_colia = 0
departure_time = 0
now = datetime.now()


def SaveRouth(marschrut):
    marschrut = routh_entry.get()
    return marschrut

def SavePlatform(number):
    number = platform_entry.get()
    return number

def SaveColia(number_colia):
    number_colia = colia_entry.get()
    return number_colia

def SaveTime(departure_time):
    departure_time = time_entry.get()
    return departure_time

def OutputInfo():
    new_marschrut = SaveRouth(marschrut)
    new_number = SavePlatform(number)
    new_number_colia = SaveColia(number_colia)
    new_time = SaveTime(departure_time)
    difference = datetime.strptime(new_time,"%H:%M:%S") - now
    time_result = difference.seconds // 60
    result.config(text=f"Потяг слідуванням: {new_marschrut}, відправляється від: {new_number_colia}, платформи: {new_number}, колії через  {time_result}, хвилин")



title = Label(root, text="UKRZALIZNYTSYA", font=("Arial", 20))
title.grid(row=0, column=1, columnspan=2, pady=20)


routh_title = Label(root, text="ROUTE:", font=("Arial", 14))
routh_title.grid(row=1, column=0, sticky="e", padx=10, pady=10)

routh_entry = Entry(root, width=40)
routh_entry.grid(row=1, column=1, padx=10, pady=10)

routh_button = Button(root, text="Set route", command=lambda :SaveRouth(marschrut))
routh_button.grid(row=1, column=2, padx=10, pady=10)


platform = Label(root, text="NUMBER OF PLATFORM:", font=("Arial", 14))
platform.grid(row=2, column=0, sticky="e", padx=10, pady=10)

platform_entry = Entry(root, width=40)
platform_entry.grid(row=2, column=1, padx=10, pady=10)

platform_btn = Button(root, text="Set platform", command=lambda : SavePlatform(number))
platform_btn.grid(row=2, column=2, padx=10, pady=10)

colia = Label(root, text="COLIA:", font=("Arial", 14))
colia.grid(row=3, column=0, sticky="e", padx=10, pady=10)

colia_entry = Entry(root, width=40)
colia_entry.grid(row=3, column=1, padx=10, pady=10)

colia_btn = Button(root, text="Set colia", command= lambda :SaveColia(number_colia))
colia_btn.grid(row=3, column=2, padx=10, pady=10)

time = Label(root, text="TIME:", font=("Arial", 14))
time.grid(row=4, column=0, sticky="e", padx=10, pady=10)

time_entry = Entry(root, width=40)
time_entry.grid(row=4, column=1, padx=10, pady=10)

time_btn = Button(root, text="Set time", command=lambda :SaveTime(time))
time_btn.grid(row=4, column=2, padx=10, pady=10)

result_btn = Button(root, text="RESULT", width=30, font=("Arial",12) ,command=lambda : OutputInfo())
result_btn.grid(row=5, column=1, padx=10, pady=10)

result = Label(root, text="", font=("Arial", 14))
result.grid(row=6, column=0, padx=10, pady=10)

root.resizable(False, False)
root.geometry("800x600")
root.mainloop()
