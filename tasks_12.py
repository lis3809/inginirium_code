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
    spis = []
    for char in input_string:
        if char == '(':
            spis.append(char)
        elif char == ')':
            if len(spis) == 0:
                print('No')
                return
            spis.pop()
    if len(spis) == 0:
        print('Yes')
    else:
        print('No')


check_string_brackets('()')

