x = int(input('Введіть число яке хочете поділити: '))
y = int(input('Введіть число на яке хочете поділити: '))


def deli(x, y):
    if y == 0:
        return
    return deli(x - y, y) if x >= y else x
print(deli(x, y))
