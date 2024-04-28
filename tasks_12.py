"""
Задание:
Напишите функцию check_string_brackets(input_string), 
которая проверяет, является ли поступившая на вход строка 
правильной скобочной последовательностью. Если да, 
она должна печатать YES, в противном случае — NO. 
Обратите внимание, что пустая строка также является 
правильной скобочной последовательностью.
"""
"""
Задание:
Напишите функцию check_string_brackets(input_string), 
которая проверяет, является ли поступившая на вход строка 
правильной скобочной последовательностью. Если да, 
она должна печатать YES, в противном случае — NO. 
Обратите внимание, что пустая строка также является 
правильной скобочной последовательностью.
"""

def check_string_brackets(input_string):
    list = []
    for i in input_string:
        if i == '(':
            list.append(i)
        if i == ')':
            if len(list) != 0:
                list.pop()
            else:
                print('NO')
                return 
    if len(list) == 0:
        print('YES')
    else:
        print('NO')

check_string_brackets('()')
check_string_brackets('(()())')
check_string_brackets('(()(()')
check_string_brackets(')(')
