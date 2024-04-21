"""
Задание:
Напишите функцию check_string_brackets(input_string), 
которая проверяет, является ли поступившая на вход строка 
правильной скобочной последовательностью. Если да, 
она должна печатать YES, в противном случае — NO. 
Обратите внимание, что пустая строка также является 
правильной скобочной последовательностью.
"""
def chek_string_brakets(input_string):
    spisok = []
    for char in input_string:
        if char == '(':
            spisok.append(char)
        elif char == ')':
            if len(spisok) == 0:
                print('NO')
                return
            spisok.pop()
    if len(spisok) == 0:
        print('YES')
    else:
        print('NO')

chek_string_brakets('()')
