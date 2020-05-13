# Натуральное число называется числом Армстронга,  (где N – количество цифр в числе)

# Найдите все трёхзначные числа Армстронга.

#пример числа
# #nb = (1 ** 3 + 3 ** 3 + 5 ** 3)
# 
# a = [" 10 :: 999 "]
# for i in range (a) :
# #задать формулу 3й степени
#     a = 
#     print(a)

def arm_sum(a,power):
    summ = 0
    
    while a > 0 :
        summ = summ + (a% 10) ** power
        
        return summ
for i in range (100, 1000):
    if i == arm_sum(i,3):
        print(i)
