x = int(input('Введіть число яке хочете помножити: '))
y = int(input('Введіть число на яке хочете помножити: '))


def mult(x, y):
    if x == 1:
        return y
    else:
        return y + mult(x - 1, y)


print(mult(x, y))