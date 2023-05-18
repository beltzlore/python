""" 28. Дана строка (возможно, пустая), состоящая из букв A-Z: 
AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB 
Нужно написать функцию RLE, которая на выходе даст строку вида: 
A4B3C2XYZD4E3F3A6B28 
И сгенерирует ошибку, если на вход пришла невалидная строка. 
Пояснения: Если символ встречается 1 раз, он остается без изменений; 
Если символ повторяется более 1 раза, к нему добавляется количество повторений. """

string = input('Введите строку: ')
def string_compression (text):
    temp_list = []
    count = 1
    if text.isalpha:
        for i in range (0, len(text)-1):
            if text[i] == text [i+1]:
                count += 1
            else:
                temp_list.append(text[i])
                temp_list.append(count)
                count = 1
        if text[-1] != text [-2]:
            temp_list.append(text[-1])
            temp_list.append(count)
        else:
            temp_list.append(text[-1])
            temp_list.append(count)
    else:
        print ('Invalid string')    
    print (*temp_list)
string_compression(string)    