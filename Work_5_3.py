# Создайте функцию генератор чисел Фибоначчи (см. Википедию)


def gener_fib (m):

    a=0
    b=1

    for n in range(0,m):
        yield a + b
        temp = a + b
        a = b
        b = temp

a = gener_fib(370)

for i in a:
    print(i)