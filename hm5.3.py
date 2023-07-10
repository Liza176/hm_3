do = int(input('Введите число до ')) + 1
rez = 0

for i in range(1,do):
    
    if do % i == 0 :
        rez += i  
        
print(rez)
    