import math


def square(side_lenght):
    area = side_lenght * side_lenght
    if not side_lenght.is_integer():
        return math.ceil(area)

    return int (area)

while True:
    side = float(input("Введите число: "))
    if side > 0:
        break
    else:
        print("Неверное число, попробуйте еще раз: \n")

result = square(side)
print(f"Площадь квадрата = {result}") 