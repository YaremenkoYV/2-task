n = int(input('Введіть число n:'))
N = int(input('Введіть число N:'))
sum_=0

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

print('Факторіал числа:',n, 'це:', (factorial(n)))
for y in range(N):
    y= ((3**n)*factorial(n))/(n**n)
    sum_+=y
print('Сума ряду дорівнює:',sum_)