alfa = [1, 4, 7, 21, 19, 5, 6, 11, 9]
sum = 0
sumar = 0
for i in range(len(alfa)):
    sum  += alfa[i]
    sumar = sum/len(alfa)
print(alfa)
print(sumar)



sumi = 0
beta = alfa[::2]
print(beta)
for i in range(len(beta)):
    sumi  += beta[i]
print(sumi)



from functools import reduce
gamma = alfa[::4]
print(gamma)
print(reduce(lambda x, y: x*y, gamma))

