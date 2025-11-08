import tkinter as tk
from collections import namedtuple

Employee = namedtuple('Employee', ['surname', 'year', 'position', 'salary'])

employees = (
    Employee('Ivanov', 1985, 'Manager', 50000),
    Employee('Petrov', 1990, 'Developer', 60000),
    Employee('Sidorov', 1988, 'Analyst', 45000),
    Employee('Kovalenko', 1992, 'Designer', 55000),
    Employee('Shevchenko', 1987, 'Tester', 48000),
    Employee('Bondarenko', 1991, 'HR', 47000),
    Employee('Melnyk', 1989, 'Support', 52000)
)

def min_salary(emp_list):
    avg_salary = sum(e.salary for e in emp_list) / len(emp_list)
    below_avg = [e.surname for e in emp_list if e.salary < avg_salary]
    text = "Співробітники:\n"
    for s in below_avg:
        text += s + "\n"
    text += "отримують надбавки до зарплати"
    return text, below_avg

root = tk.Tk()
root.title("Employees Salary")

label = tk.Label(root, text="", justify="left", font=("Arial", 12))
label.pack(padx=20, pady=20)

def show_salary():
    global employees
    text, below_avg = min_salary(employees)
    employees = tuple(
        e._replace(salary=e.salary + 5000) if e.surname in below_avg else e
        for e in employees
    )
    label.config(text=text)

btn = tk.Button(root, text="Перевірити зарплату", command=show_salary)
btn.pack(pady=10)

root.mainloop()
