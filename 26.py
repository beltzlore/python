"""  26. Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B 
с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 """

a = int(input ('Введите A: ')) 
b = int(input ('Введите B: '))
def pow_rec (number, power):
    if power == 0:
        return 1
    elif power == 1:
        return number
    return number*pow_rec(number, power - 1)
print (pow_rec(a, b))