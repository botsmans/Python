'''На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел. Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.). Если в списке нечетное количество элементов, то последний остается на своем месте.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.

Формат выходных данных
Программа должна вывести измененный список, разделяя его элементы одним пробелом.

Sample Input 1:

1 2 3 4 5
Sample Output 1:

2 1 4 3 5'''
a = [int(i) for i in input().split()]
if len(a)%2 == 1:
    b = 1
else: b = 0
for i in range(0,len(a)-b, 2):
    c = a[i + 1]
    a[i + 1] = a[i]
    a[i] = c
print(*a)