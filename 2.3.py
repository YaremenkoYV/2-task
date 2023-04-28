a = int(input('Введіть число яке хочете поділити: '))
b = int(input('Введіть число на яке хочете поділити: '))


def deli(x, y):
    if y == 1:
        return x
    elif y==0:
        return
    else:
        return deli(x - y, y) if x >= y else x
print("Результат ділення: ", deli(a, b))
