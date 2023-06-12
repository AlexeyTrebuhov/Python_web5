# 1.	Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
#       Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


link = 'D:/Programs/Unity/2021.3.12f1/modules.json'

def stroc (link):
    return tom


subtext='/'
result = []

flag = False
n = 1
temp = 0

for i,element in enumerate(link):

    if flag:
        if n > len(subtext)-1:
            flag = False
            n = 1
        elif element == subtext[n]:
            n += 1
        elif element != subtext[n]:
            result = result[:-1]
            n = 1
            flag = False
    if element == subtext[0] and not flag:
        flag = True
        result.append(i)
        temp = i

*prefix, suffix = link.rsplit('/')
rash,r = suffix.split('.')

tom = (link[0:temp],rash, r)

print (stroc('D:/Programs/Unity/2021.3.12f1/modules.json'))










