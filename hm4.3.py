n = int(input('Напишите сколько раз '))
rezult = 1

for i in range(n):
    n2 = int(input())
    if n2 == 0 :
        continue
    rezult *= n2

print('Произведение', rezult)