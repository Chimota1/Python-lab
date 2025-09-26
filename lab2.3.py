import random

income = []

for i in range(10):
    row = []
    for j in range(12):
        value = random.randint(1000, 10000)  # випадковий дохід
        row.append(value)
    income.append(row)

print("Дохід магазинів по місяцях:")
for i in range(10):
    print("Магазин", i + 1, ":", income[i])

store = int(input("\nВведіть номер магазину (1-10): "))
store_index = store - 1

quarter = int(input("Введіть номер кварталу (1-4): "))

if quarter == 1:
    start = 0
    end = 3
elif quarter == 2:
    start = 3
    end = 6
elif quarter == 3:
    start = 6
    end = 9
else:
    start = 9
    end = 12

quarter_income = 0
for month in range(start, end):
    quarter_income += income[store_index][month]

print("\nДохід магазину", store, "за", quarter,"-й квартал:", quarter_income)
