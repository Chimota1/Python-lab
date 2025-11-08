import tkinter as tk
from tkinter import Label, Entry, Button

class Plane:
    def __init__(self,mark,model,maxSpeed,maxHeight):
        self.mark = mark
        self.model = model
        self.maxSpeed = maxSpeed
        self.maxHeight = maxHeight

    def Cost(self):
        return self.maxSpeed * 1000 + self.maxHeight * 1000

    def Info(self):
        return f"Mark: {self.mark}, Model: {self.model}, Max Speed: {self.maxSpeed}, Cost: {self.Cost()}"

    def __del__(self):
        print("Destructor of plane")

class Bomber(Plane):
    def __init__(self,mark,model,maxSpeed,maxHeight,nameOfPilot):
        super().__init__(mark,model,maxSpeed,maxHeight)
        self.nameOfPilot = nameOfPilot

    def Cost(self):
        return (self.maxSpeed * 1000 + self.maxHeight * 1000) * 2

    def Info(self):
        return f"Mark: {self.mark}, Model: {self.model}, Name of Pilot {self.nameOfPilot} ,Max Speed: {self.maxSpeed}, Cost: {self.Cost()}"

    def __del__(self):
        print("Destructor of bomber")

class Fighter(Plane):
    def __init__(self,mark,model,maxSpeed,maxHeight,group):
        super().__init__(mark,model,maxSpeed,maxHeight)
        self.group = group

    def Cost(self):
        return (self.maxSpeed * 1000 + self.maxHeight * 1000) * 3

    def Info(self):
        return f"Mark: {self.mark}, Model: {self.model}, Group: {self.group} ,Max Speed: {self.maxSpeed}, Cost: {self.Cost()}"

    def __del__(self):
        print("Destructor of fighter")

if __name__ == "__main__":
    def main():
        root = tk.Tk()
        plane = Plane("Antonov","An-225", 85, 150)
        bomber = Bomber("TU","TU-95", 83, 105,"Maksym")
        fighter = Fighter("Syhui", "SU-27",25,18,"KyivGhost")
        Title1 = Label(root,text="Plane", font=("Arial",20))
        Title1.pack(side= tk.TOP, fill= tk.X, pady=10)
        Title1.pack(side= tk.TOP, fill= tk.Y)
        text = Label(root,text=plane.Info(),font=("Arial",12))
        text.pack(side= tk.TOP, fill= tk.X, pady=5)
        text2 = Label(root,text=bomber.Info(),font=("Arial",12))
        text2.pack(side= tk.TOP, fill= tk.Y, pady=5)
        text3 = Label(root,text=fighter.Info(),font=("Arial",12))
        text3.pack(side= tk.TOP, pady=5)
        root.geometry("800x600")
        root.mainloop()


main()