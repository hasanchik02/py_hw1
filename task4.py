# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).


a = int(input('В-те 1-ю сторону: '))
b = int(input('В-те 2-ю сторону: '))
c = int(input('В-те кол-во долек: '))
if c%a == 0 or c%b == 0:
    print('Yes')
else: print('No')