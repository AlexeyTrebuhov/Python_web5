# 	Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# 	имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь
# 	с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка
# 	умноженная на процент премии


name = ['Ivan', 'Sergey','Alibaba']
stavka = [7,5,4]
prem = ['10.25%', '7.43%', '24.2%']

print("Stavka = ", stavka,"Name = ", name, "Prem = ", prem)
print("-"*100)

list = []
for x in prem: list.append (x.replace('%', ''))


the_dict = dict(zip(name,[x * y for x, y in zip(stavka, [float(x) for x in list])]))
print("Dict = ", the_dict,type(the_dict))
