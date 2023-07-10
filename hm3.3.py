
do = int(input('Введите число до ')) + 1
_2or_8_5 = 0
kv = 1

for i in range(1,do):
    kv = i ** 2
    if kv % 10 == 2 or kv % 10 == 5 or kv % 10 == 8 :
        _2or_8_5 += i  
        

print(_2or_8_5)
    