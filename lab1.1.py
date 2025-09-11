import random
import math

def GenerateX():
    return random.randint(0, 20)

def GenerateY():
    return random.randint(0, 20)

def SimulationOfShot(countOfTry,avilibleTries):
    print("| № Пострілу | Координати Пострілу | Результат |")
    for i in range(avilibleTries):
        x = GenerateX()
        y = GenerateY()
        formula1 = (x > 0 and x < (2 * R)) and (y > -R and y < 0)
        formula2 = pow(x, 2) + pow(y - R, 2) < pow(R, 2)
        countOfTry += 1
        if (formula1 or formula2):
            print("|",countOfTry ,"|","(",GenerateX(),",",GenerateY(),")","| Влучив |")
        else:
            print("|",countOfTry ,"|","(",GenerateX(),",",GenerateY(),")","| Промах |")

R = 5
avilibleTries = 10
countOfTry = 0
SimulationOfShot(countOfTry,avilibleTries)