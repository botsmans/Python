'''Дана строка, состоящая из слов, разделенных пробелами. Напишите программу, которая подсчитывает количество слов в этой строке.

Формат входных данных
На вход программе подается строка.

Формат выходных данных
Программа должна вывести количество слов в строке.

Примечание 1. Кроме слов в тексте могут присутствовать только пробелы (один или несколько).

Примечание 2. Решите задачу в одну строчку кода 😎.

Тестовые данные 🟢
Sample Input 1:

Hello world
Sample Output 1:

2'''
print(len(input().split()))
#print(input().count(' ') + 1)