def WhiteBishop1():
    x = int(input("Enter x for first white bishop1: "))
    y = int(input("Enter y for first bishop1: "))
    if (x < 1 or x > 8 or y < 1 or y > 8):
        print("Error")
        return None
    return x, y

def WhiteBishop2():
    x = int(input("Enter x for first white bishop2: "))
    y = int(input("Enter y for first bishop2: "))
    if (x < 1 or x > 8 or y < 1 or y > 8):
        print("Error")
        return None
    return x, y

def BlackBishop1():
    x = int(input("Enter x for first black bishop1: "))
    y = int(input("Enter y for first black bishop1: "))
    if (x < 1 or x > 8 or y < 1 or y > 8):
        print("Error")
        return None
    return x, y

def BlackBishop2():
    x = int(input("Enter x for first black bishop2: "))
    y = int(input("Enter y for first black bishop2: "))
    if (x < 1 or x > 8 or y < 1 or y > 8):
        print("Error")
        return None
    return x, y

def Chess(wb1, wb2, bb1, bb2):
    def can_attack(a, b):
        return abs(a[0] - b[0]) == abs(a[1] - b[1])

    if can_attack(wb1, bb1) or can_attack(wb1, bb2):
        print("1 attack")
    elif can_attack(wb1, wb2):
        print("2 defend")
    else:
        print("3 skip")

    if can_attack(wb2, bb1) or can_attack(wb2, bb2):
        print("1 attack")
    elif can_attack(wb2, wb1):
        print("2 defend")
    else:
        print("3 skip")


wb1 = WhiteBishop1()
wb2 = WhiteBishop2()
bb1 = BlackBishop1()
bb2 = BlackBishop2()

if wb1 and wb2 and bb1 and bb2:
    Chess(wb1, wb2, bb1, bb2)
