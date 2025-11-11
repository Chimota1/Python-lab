import tkinter as tk


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def to_list(self):
        result = []
        if not self.head:
            return result
        current = self.head
        result.append(current.data)
        while current.next != self.head:
            current = current.next
            result.append(current.data)
        return result


class Doctor:
    def __init__(self, surname):
        self.surname = surname
        self.patients = []  # список пацієнтів


root = tk.Tk()
root.title("Розподіл пацієнтів по лікарях")

output_label = tk.Label(root, text="", justify="left", font=("Arial", 12))
output_label.pack(padx=20, pady=20)


def distribute_patients():
    doctors_list = CircularLinkedList()
    patients_list = CircularLinkedList()

    # лікарі з файлу
    try:
        with open("doctors.txt", "r", encoding="utf-8") as f:
            for line in f:
                name = line.strip()
                if name:
                    doctors_list.append(Doctor(name))
    except FileNotFoundError:
        output_label.config(text="Файл doctors.txt не знайдено!")
        return

    try:
        with open("patients.txt", "r", encoding="utf-8") as f:
            for line in f:
                name = line.strip()
                if name:
                    patients_list.append(name)
    except FileNotFoundError:
        output_label.config(text="Файл patients.txt не знайдено!")
        return

    n = 3
    doctors = doctors_list.to_list()
    doctor_index = 0
    for pat in patients_list.to_list():
        doctors[doctor_index].patients.append(pat)
        if len(doctors[doctor_index].patients) >= n:
            doctor_index = (doctor_index + 1) % len(doctors)

    text = ""
    for doc in doctors:
        text += f"Лікар {doc.surname}:\n"
        for pat in doc.patients:
            text += f" - {pat}\n"
    output_label.config(text=text)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(text)

btn = tk.Button(root, text="Розподілити пацієнтів", command=distribute_patients)
btn.pack(pady=10)

root.mainloop()
