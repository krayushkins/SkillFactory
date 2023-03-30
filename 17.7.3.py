per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
money = input('Вводите сумму, которую планируете положить под проценты: ')

l = '_'
print(l*100)

deposit.append(int(per_cent['ТКБ'] * int(money) / 100))
deposit.append(int(per_cent['СКБ'] * int(money) / 100))
deposit.append(int(per_cent['ВТБ'] * int(money) / 100))
deposit.append(int(per_cent['СБЕР'] * int(money) / 100))
print('Накопленные средства за год вклада в каждом из банков: ', deposit)

print(l*100)

print('Ваш максимальный заработок может составить: {}'.format(max(deposit)))

print(l*100)