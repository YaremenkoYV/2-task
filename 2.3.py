a = int(input('Введіть ділене: '))
b = int(input('Введіть дільник: '))


def deli(x, y):
    if y == 1:
        return x
    elif x < y:
        return print("Введіть таке ділене, щоб воно було більше дільника")
    elif y == 0:
        return print("Ділити на нуль не можливо")
    elif x == 0:
        return print("Нуль не можливо поділити")
    else:
        return deli(x - y, y) if x >= y else x
print("Результат ділення: ", deli(a, b))
