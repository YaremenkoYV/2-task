a = int(input('Введіть число яке хочете помножити: '))
b = int(input('Введіть число на яке хочете помножити: '))


def mult(x, y):
    if x == 1:
        return y
    elif y == 1:
        return x
    elif x == 0 or y == 0:
        return 0
    else:
        return y + mult(x - 1, y)

print("Результат множення: ", mult(a, b))
