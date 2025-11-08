from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import Label, Entry, Button, Text, END


class Settlement(ABC):
    def __init__(self, name, population, area, region):
        self.name = name
        self.population = population
        self.area = area
        self.region = region

    def __del__(self):
        print(self.name)

    def Info(self):
        return f"Name: {self.name}, Population: {self.population}, Area: {self.area}, Region: {self.region}"

    def CategoryByPopulation(self):
        if self.population < 5000:
            return "Small locality"
        elif self.population > 5000 and self.population < 50000:
            return "Middle locality"
        elif self.population > 50000:
            return "Large locality"

    @abstractmethod
    def GetStatusOfSettlement(self):
        pass

    def calculatePopulationDensity(self):
        pass


class Village(Settlement):
    def __init__(self, name, population, area, region, countOfFarm):
        super().__init__(name, population, area, region)
        self.countOfFarm = countOfFarm

    def GetStatusOfSettlement(self):
        return "It`s Village"

    def calculatePopulationDensity(self):
        return self.population / self.area

    def ShareOfFarm(self):
        return self.area / self.countOfFarm


class City(Settlement):
    def __init__(self, name, population, area, region, countOfIndustrialZones):
        super().__init__(name, population, area, region)
        self.countOfIndustrialZones = countOfIndustrialZones

    def GetStatusOfSettlement(self):
        return "It`s City"

    def calculatePopulationDensity(self):
        return self.population / self.area

    def InfrastuctureLoad(self):
        return self.population / self.countOfIndustrialZones


def main():
    root = tk.Tk()
    root.title("Settlement Database")
    root.geometry("900x700")

    settlements = [
        Village("Velyka Dolyna", 2500, 30.5, "Odesa", 120),
        Village("Mala Kamyanka", 6000, 45.2, "Cherkasy", 210),
        City("Kyiv", 2800000, 839, "Kyiv Region", 350),
        City("Lviv", 720000, 182, "Lviv Region", 120),
        Village("Zelenyi Hai", 800, 10.1, "Vinnytsia", 50)
    ]

    title = Label(root, text="Settlement Information", font=("Arial", 20))
    title.pack(pady=10)

    text_box = Text(root, width=110, height=22, font=("Arial", 12))
    text_box.pack(pady=10)

    def show_all():
        text_box.delete(1.0, END)
        for s in settlements:
            text_box.insert(
                END,
                f"{s.Info()}, Status: {s.GetStatusOfSettlement()}, "
                f"Category: {s.CategoryByPopulation()}\n"
            )

    def search_by_population():
        text_box.delete(1.0, END)
        try:
            target = int(entry_population.get())
            found = [s for s in settlements if s.population == target]
            if found:
                for s in found:
                    text_box.insert(
                        END,
                        f"{s.Info()}, Status: {s.GetStatusOfSettlement()}, "
                        f"Category: {s.CategoryByPopulation()}\n"
                    )
            else:
                text_box.insert(END, "No settlements found with that population.\n")
        except ValueError:
            text_box.insert(END, "Please enter a valid number.\n")

    # Кнопки і поле для введення
    btn_show = Button(root, text="Show All Settlements", command=show_all, font=("Arial", 12))
    btn_show.pack(pady=5)

    lbl_population = Label(root, text="Enter population to search:", font=("Arial", 12))
    lbl_population.pack(pady=5)

    entry_population = Entry(root, font=("Arial", 12))
    entry_population.pack(pady=5)

    btn_search = Button(root, text="Search", command=search_by_population, font=("Arial", 12))
    btn_search.pack(pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
