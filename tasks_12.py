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
    spisok = []
    for char in input_string:
        if char == '(':
            spisok.append(char)
        elif char == ')':
            if len(spisok) == 0:
                print('No')
                return
            spisok.pop()
    if len(spisok) == 0:
        print('Yes')
    else:
        print('No')


check_string_brackets('()')
check_string_brackets('())')
