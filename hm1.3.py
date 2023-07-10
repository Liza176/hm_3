ot = int(input('Введите число от '))
do = int(input('Введите число до ')) + 1
_4or_9 = 0

for i in range(ot,do):
    i = i ** 3
    if i % 10 == 4 or i % 10 == 9 :
        _4or_9 = _4or_9 + 1

print(_4or_9)
    
