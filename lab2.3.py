import math
import random

def create_massive(data_market):
    for i in range(10):
        row = []
        for j in range((4)):
            row.append(random.randint(2000,1000000))
        data_market.append(row)

def show_market(data_market,choice):
    create_massive(data_market)
    for i in range(len(data_market)):
        if i == choice:
            for j in range(len(data_market[i])):
                print (data_market[i][j])


data_market = []
choice = int(input("Enter the number of market: "))
show_market(data_market,choice)


