from _typeshed import SupportsLenAndGetItem
from collections import namedtuple
from re import L
from typing import AsyncIterable, Counter

Ctrl + ` #open terminal
Ctrl + / #Быстро добавить комментарий
Ctrl + G #Перейти к строке под номером
Alt + ↑ / ↓ #Поменять строку местами с соседними
Shift + Alt + ↓ / ↑ #Дублировать строку
Ctrl + Shift + \ #Перейти к парной скобке
Shift + Alt + F #Отформатировать документ (pep8)
F12 #Перейти к объявлению переменной
Alt + Z #Включить/выключить перенос слов
Ctrl + K Z #Включить дзен-режим
https://nikomedvedev.ru/other/vscodeshortcuts/hotkeys.html


cd #выбор дирректории
python # запуск интерпритатора 
quit #выход из интерпритатора
python test.py # запуск файла

print("Hello", name)
int(-2.3) --> -2
floal(5) --> 5
type(7) --> int # вычесление типа
s = int(input('Введите данные')) # ждет данные от пользователя и переводит в int и сохраняет в s
type(s) -->int

x y or and not
0 0 0  0   1
0 1 1  0   1
1 0 1  0   0
1 1 1  1   0

# БИРТОВЫЕ ОПЕРАТОРЫ
# Бинарное И (&)
# Проводит побитовую операцию and над двумя значением. Здесь бинарная 2 — это 10, а 3 — 11. Результатом побитового and является 10 — бинарная 2. Побитовое and над 011(3) и 100(4) выдает результат 000(0).
print(2&3)-->2
print(3&4)-->0
# Бинарное ИЛИ (|)
# Проводит побитовую операцию or на двух значениях. Здесь or для 10(2) и 11(3) возвращает 11(3).
print(2|3)-->3
# Бинарное ИЛИ НЕТ (^)
# Проводит побитовую операцию xor (исключающее или) на двух значениях. Здесь результатом ИЛИ НЕ для 10(2) и 11(3) будет 01(1).
print(2^3)-->1
# Инвертирующий оператор (~)
# Он возвращает инвертированные двоичные числа. Другими словами, переворачивает биты. Битовая 2 — это 00000010. Ее инвертированная версия — 11111101. Это бинарная -3. Поэтому результат -3. Похожим образом ~1 равняется -2
print(~-3)-->2
# Бинарный сдвиг влево (<<)
# Он сдвигает значение левого операнда на позицию, которая указана справа. Так, бинарная 2 — это 10. 2 << 2 сдвинет значение на две позиции влево и выйдет 1000 — это бинарная 8
print(2<<2)-->8
# Бинарный сдвиг вправо (>>)
print(3>>2)-->0
print(3>>1)-->1

# по порядку вычисления not and or

10 > 2 and 10 > 9         # True
10 > 2 and 10 > 11        # False
10 > 2 or 10 > 11         # True
10 > 2 and not 10 > 11    # True
not (10 > 2 or 10 > 11)   # False

#True = 1, False = 0
print(True + True + True - False)-->3
print(True + (False / True))-->1.0

#сокращения
if flag: #if flag == True:
if not flag: #if flag == False:

#Для приведения других типов данных к булеву существует функция bool(), работающая по следующим 
# соглашениям:
#строки: пустая строка — ложь (False), непустая строка — истина (True);
#числа: нулевое число — ложь (False), ненулевое число (в том числе и меньшее нуля) — истина (True);
#списки: пустой список — ложь (False), непустой — истина (True).
print(bool('Beegeek'))-->True
print(bool(17))-->True
print(bool(['apple', 'cherry']))-->True
print(bool())-->False
print(bool(''))-->False
print(bool(0))-->False
print(bool([]))-->False

isinstance() #функция для проверки соответствия типа объекта какому-либо типу данных
print(isinstance(3, int))-->True
print(isinstance(3.5, float))-->True
print(isinstance('Beegeek', str))-->True
print(isinstance([1, 2, 3], list))-->True
print(isinstance(True, bool)-->True
print(isinstance(3.5, int))-->False
print(isinstance('Beegeek', float))-->False

type()#function позволяющая получить tipe указанного в качестве аргумента объекта
print(type(3))--><class 'int'>
print(type(3.5))--><class 'float'>
print(type('Beegeek'))--><class 'str'>
print(type([1, 2, 3]))--><class 'list'>
print(type(True))--><class 'bool'>
print(type(None)--><class 'NoneType'>
s = "asdf"
print(type(s))--><class str>
print(type(int))--><class type>

if var is None:#Проверка на None 
if var == None:#Проверка на None, оператор "==" менее предпочтителен

print(None == None)-->True

#функции, не возвращающие значений, на самом деле возвращают значение None

print('*', end='') # печать символа без переноса на следующюю строку

a = [1, 2, 3]
print(*a)-->1 2 3


if (x=1):
    print(1)
elif (x=2):
    print(2)
else:
    print(3)

len('abcdef') --> 6
'\n' #символ перевода строк
'\t' #символ табуляции
# # комментарий
'''
multi-line comments
'''

while i < 5: # оператор выполняющий цикл пока выполняется устловие
a, b = input().split() # сохраняет и разделяет пользовательский ввод
break # завершает цикл
continue # переходит на следующий цикл
for i in 1, 2, 3, 4 # оператор для последовательности чисел, i пройдет по всем числам после in
for i in range(2, 15, 4) # числа от 2 до 14 с шагом 4

for
   break
else:

while
else: somethink # else после for при выходе с break или выход с while будет выполнено 

for
    for
        if
            break
    if # можно использовать если break не было

# LIST COMPREHENSION

a, b = (int(i) for i in input().split()) # для пременных
a = [int(i) for i in input().split()] # для списка


x = [-2, -1, 0, 1, 2]
y = [i*i for i in x]
print(y) --> [4, 1, 0, 1, 4]

y = [i*i for i in x if i > 0] # with if
print(y) --> [1, 4]


z = []
for x in range(3):
    for y in range(3):
        if y >= x:
            z.append((x, y))
#same as
z =[(x, y) for x in range(3) for y in range(3) if y >= x] --> [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]


z =((x, y) for x in range(3) for y in range(3) if y >= x) # если круглые скобки
print(z) --> generator object
print(next(z)) --> (0, 0)
print(next(z)) --> (0, 1)




# STRING

#преобразование в строку
a = len(input())*60
print(str(a//100)+' р. '+str(a%100)+' коп.')

# строки не изменяемы
genome = 'ATTG'
for c in genome:
    print(c)   # проход по строке

#f string
print(f'genome = {gemome}')--> genome = ATTG

genome = 'ATTG'
print(genome.count('T')) # считает сколько T в genome 

s='aTGcc' p='cc'
s.title()#all first simbol is big
s.upper() --> 'ATGCC'
s.lower() --> 'atgcc'
s.count(p) --> 1 # количество не пересекающихся вхождений, s.count(p, 3, 4) - 3 and 4 is position for search
s.find(p) --> 3 #retun only first position of simbols or -1, s.find(p, 3, 5) -3 and 5 is position for seaech
s.rfind(p)#см выше, только проверка идет справа
s.find('A') --> -1 #  не входит
if 'TG' in s:-->True #проверка вхождения в строку
s.replace('c', 'C') --> 'aTGCC'# s.replace ('c', 'C', 2) - max 2 first replace
s.index("TG")-->1 #index of first вхождения or ValueError
s.startswith("The man in black") # проверка начинается ли строка с данного набора символов, функция может принемать кортеж
s.endswith(".png")# см. выше, только проверяет окончание строки
s.split() # разделение по пробелу или заданному символу
s.strip() # clear simbols("\t", " ")
s.rstrip()# clear right side
s.lstrip()# clear left side
s.isalpha()# строка состоит только из букв
s.isdigit()# проверяет состоит ли строка только из цифр
s.rjust(10, '0' ) #делает строку равную длинне 10, а свободное место заполняет '0' или пробелами по дефолту
s.ljust(10) # см выше, два символа для заполнения передовать нельзя

s = 'agTtcAGtc'
genome.upper().count('gt'.upper()) --> 2 # с начала поднимает s, потом поиск поднятого gt

w ='Ivanov Ivon Ivanovich'
w = ','.join.(w.split())-->'Ivanov,Ivan,Ivanovich'

x = r"hello\nworld" #raw
print(x)-->hello\nworld

#.format()
template = '{} is the capital of {}.'
print(template.format("London", "Great Britain"))
template = '{1} is the capital of {0}.' #выбираем порядок
print(template.format("London", "Great Britain"))
template = '{capital} is the capital of {country}.' #выбираем порядок
print(template.format(capital="London", coutnry="Great Britain"))

import requests
template = "Response from {0.url} with code {0.status_code}."
res = requests.get("https://docs.python.org/3.5/")
print(template.format(res))

from random import random
x = random
print("{:.3}".format(x)) # output onli first three simbols after dot
# SLICING

dna = 'ATTCGGAGCT'
dna[1] --> 'T'
dna[1:4] --> 'TTC'
dna[:4] --> 'ATTC'
dna[4:] --> 'GGTAGCT'
dna[1:-1] --> 'TTCGGAGC'
dna[1:-1:2] --> 'TCGG'
dna[::-1] --> 'TCGAGGCTTA'

# СПИСКИ LIST
students = [] # пустой список
students = ['olya', 'seriy', 'pasha'] # заполненный список
for student in students:
   print("hello, " + student + "!")

# можно явно исменять список: 
students[0] = 'Olya'
students += ['Katya'] или students.append('Katya') # students += 'Katya' прибавит 5 элементов в список
list1 = list2 + list3 # сложение списков не путать с append
list.extend(list2) #сложение списков
students.insets(1, 'Boris') # вставляет элемент между 0 и 1 элементами
students.remove('Boris') # удаляет первое вхождение элемента 'Boris'
del students[0] # удаляет нулевой элемент
----
numbers = [10, 20, 30, 40]
del numbers[0:6]
print(numbers)-->[]#out of range не наступает
-------
list.pop([i]) # Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
list.index(x, [start [, end]]) # Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)
list.count(x) # Возвращает количество элементов со значением x
list.copy() # Поверхностная копия списка
list.clear() # Очищает список
list.reverse() # инвертирует порядок следования значений в списке, то есть меняет его на противоположный
list.split() # разбивает строку на слова, используя в качестве разделителя последовательность пробельных символов, символ табуляции (\t) или символ новой строки (\n)
list.join() # собирает строку из элементов списка, используя в качестве разделителя строку, к которой применяется метод.

numbers = [4, 8, 12, 16, 34, 56, 100]
numbers[1:4] = [20, 24, 28]
print(numbers)-->[4, 20, 24, 28, 34, 56, 100]

#list copy
letters = ['a', 'b', 'c', 'd']
new_letters1 = letters.copy()
new_letters2 = letters[:]
new_letters3 = list(letters)

#max and min
words = ['xyz', 'zara', 'beegeek']
print(max(words))-->zara

list1 = [[1, 7, 12, 0, 9, 100], [1, 7, 90], [1, 10]]
list2 = [['a', 'b'], ['a'], ['d', 'p', 'q']]
print(min(list1))-->[1, 7, 12, 0, 9, 100]
print(max(list1))-->[1, 10]
print(min(list2))-->['a']
print(max(list2))-->['d', 'p', 'q']

# поиск элементов в списке
if 'ivan' in students:
   print('ivan is here')

if 'ivan' not in students:
   print ('ivan is out')

ind = students.index('Sasha') # возвращает индекс элемента в списке или ошибку

# сортировка

sorted_students = sorted(students) # не меняет изначальный список
student.sort() # меняет изначальный список
min() , max() # выводит максимальный и мин элемент (если элементы сравнимы)

students.reverse() или students[::-1] # переворачивает список
reversed(students)  # тоже но без изменения изначального списка

# создание списков
a = [] 
a = [1, 3, 5]
b = a // ссылка будет идти на один и тотже объект
a = [0] * 5 --> [0, 0, 0, 0, 0]  
a = [0 for i in range(5)] --> [0, 0, 0, 0, 0]
a = [i * i for i in range(5)] --> [0, 1, 4, 9, 16]

# двумерные списки
a = [[1,2],[3,4]]
a = [1][1] --> 4

my_list = ['Python', [10, 20, 30], ['Beegeek', 'Stepik!']]
print(my_list[2][-1][-1])-->!

a = [[0] * m for i in  range(n)] 
b = [[0 for j in range(m)] for i in range(n)] #same as
c = [[0] * m for _ in range(n)] #same as, можно ставить "_" если i не будет использована
d = [[0] * m ] * n # !!!! так нельзя, ссылка будет одна и таже

# КОРТЕЖИ(TUPLE)

# не изменяемы, быстрее чем списки, можно использовать в качестве ключей словаря,
#  удобно если зотим сделать что-то не изменяемое
# не имеют метода index, но имеют in
# Кортежи поддерживают:
# доступ к элементу по индексу (только для получения значений элементов);
# методы, в частности index(), count();
# встроенные функции, в частности len(), sum(), min() и max();
# срезы;
# оператор принадлежности in;
# операторы конкатенации (+) и повторения (*).

info = ('a', 0, False, (4, 5, 6), [])
g = (5) # это не кортеж
g = (5,) # это кортеж
g = () # пустой картеж
info[3:4] # срезы в кортежах это новый кортеж
g =([1, 3]) # списки внутри 

#list to tuple
str_list = ['один', 'два', 'три']
str_tuple = tuple(str_list)
print(str_tuple)-->('один', 'два', 'три')
str_list = list(str_tuple)
print(str_list)-->['один', 'два', 'три'] # tuple to list

# проверка на пустоту
tuples = [(), (), ('',), ('a', 'b'), (), ('a', 'b', 'c'), (1,), (), (), ('d',), ('', ''), ()]
non_empty_tuples = [i for i in tuples if len(i)>0]


is_target_node = False
node = 'Node1'
if (node == 'Node1' or node == 'Node2' or node == 'Node3')
    is_target_node = True
# сократим-->
node = 'Node1'
is_target_node = (node == 'Node1' or node == 'Node2' or node == 'Node3')
# сократим используя кортеж
node = 'Node1'
is_target_node = node in ('Node1', 'Node2', 'Node3')

# присваивание кортежу
f, s, *c, l = [1, 2, 3, 4, 5, 6, 7]  # *c--> [3, 4, 5, 6]

# передача dict to function argument
d = {'a': 1, 'b': 2}
def foo(a, b):
    pass
foo(**d)

# ФУНКЦИИ

def f(n):
    return n * 10 + 5 # Функция объявляется в начале программы

def min(*a): # Функция с произвольным количеством параметров
def my_range(start, stop, step = 1): # Функция с заданными параметрами

# ПЕРЕДАЧА АРГУМЕНТОВ В ФУНКЦИЮ

def printab(a, b):
    print(a)
    print(b)

printab(10, 20)
printab(a=10, b=20)
lst=[10 ,20]
printab(*lst)
args = {'a': 10, 'b': 20}
printab(**args)

def foo(a, b=10): # b - значение по умолчанию если не задано
def foo(a=20, b): --> Error syntacsis

def foo(a, b ,*args):
foo(1, 2, 3, 4, 5) # можно передовать произвольное количество аргументов

def printab(a, b, **kwargs):
    print(a, b)
    for key in kwargs:
        print(key, kwargs[key])
printab(10, c=30, jimmi=123, b=20)

# порядок инициализирования аргументов
def function_name([positional_args,
                  [positional_args_with_default,
                  [*post_args_name,
                  [keyword_only_name,
                  [**kw_args_name]]]]]):
def printab(a, b=10, *args, c=10, d, **kwargs):
    print(a, b, c, d)
print(15, d=15)-->15 10 10 15

# GLOBAL VARIABLE

ok_status = True
vowels = ["a", "u", "i", "e", "o"]
def check(word):
    global ok_status # использование не локальной переменной функции, а глобальной
    for vowel in vowels:
        if vowerl in word:
            return = False
    ok_status = False
    return False

#bild in - встроенное пространство имен, внутри него файл example.py c Глобальной областью видимости (global), внутри функций локальная область видимости (local)

# NONELOCAL VARIABLE

def f():
    ok_status = True
    def t():
        nonlocal ok_status #идет обращение на уровень(или несколько(пока не найдет нужную переменную)) 
        #выше локальной функции  
        ok_status = False
    s()
    print(ok_status)

f()-->False
print(ok_status) --> NameError #так как данной переменной нет в глобальном пространстве имен

#ЗАМЫКАНИЯ CLOSURE
#1
def main_func(name):
    n = name
    def inner_func():
        print('Hello', name)#что бы происходило замыкание необходимо использовать переменную из внешней функции
    
    return inner_func#мы передаем саму функцию а не ееё результат по этому без скобок
v = main_func('Vasya') #y ссылаеться на main_func('Vasya')
v() --> Hello Vasya
s = main_func('Sveta')
s() --> Hello Sveta
v() --> Hello Vasya #переменные сохраняются как в экземплярах класса это и называеться замыкание

#2
def adder(value):
    def inner(a):
        return (value + a)
    return inner
a2 = adder(2)
a2(5)-->7
a2(10)-->12
a5 = adder(5)
a5(10) -->15

#3
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner
q = counter()
q() --> 1
q() --> 2
r = counter()
r() --> 1
r() --> 2
q() --> 3

#4
def averege_numbers():
    summa = 0
    count = 0
    def inner(number):
        nonlocal summa
        nonlocal count
        summa = summa + number
        count += 1

        return summa / count
    
    return inner
a = average_numbers()
a(100) -->100
a(200) -->150

#5
from datetime import datetime
def timer():
    start = datetime.now()
    def inner():
        return datetime.now() - start
    return inner
r = timer()
r() #веренет разницу между перевым и последним вызовом

#6 передача функциив качестве параметра
def add(a + b):
    return a + b
def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print (f"Функция {func.__name__} вызывалась {count} раз")
        return func(*args, **Kwargs)
    return inner
q = counter(add)
q(10, 20) --> 30 Функция add вызывалась 1 раз
q(3, 4) --> 7 Функция add вызывалась 2 раз

#DECORATOR декораторы
def decorator(func):
    def inner(*args, **kwargs): # желательно всегда вставлять такие конструкции для параметров
        #в виде *args, **kwargs так как мы за ранее не знаем сколько будет параметров у функции 
        # которую мы будем декорировать
        print('start decorator...')
        func(*args, **kwargs)
        print('finish decorator...')

        return inner

def say(name, surname):
    print('hello', name, surname)

say = decorator(say)#now func working different
say('Vasya', 'Ivanov') --> start decorator...\n hello Vasya Ivanov \n finish decorator...

#2
def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')
        return inner

def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
        return inner


def say(name, surname):
    print('hello', name, surname)

say = table(header(say))# обернули в 2 decorators
say('Vasya', 'Ivanov') --> <table><h1>hello Vasya Ivanov <\h1><\table>

#2a
#same as
@table
@header # '@table' and '@header' same as 'say = table(header(say))'
def say(name, surname):
    print('hello', name, surname)
say('Vasya', 'Ivanov') --> <table><h1>hello Vasya Ivanov <\h1><\table>



# МНОЖЕСТВА

s = set() # создание множества пустого
basket = {'apple', 'orange', 'apple'} # создание множества
print(basket) --> {'orange', apple'} # повторы исключаются
'orange' in basket --> True # проверка нахождения в множестве

# операции множеств

s.add(element)
s.remove(element) #вызывает ошибки при удалении если элемент отсутствует
s.discard(element) #не вызывает ошибок при удалении 
s.clear()

# СЛОВАРИ DICTIONARY

https://webdevblog.ru/kak-perebrat-slovar-v-python/

d = dict()
d = {}
d = {'a': 239, 10:100}
print(d['a']) # выведет ошибку если такого ключа нет в словаре
d[key] = value # присвоение нового значения ключу
d.get(key) # выдает либо значение либо None если ключа такого нет
del d[key] # удаление пары ключ и заначение


dict.clear() # очищает словарь.
dict.copy() # возвращает копию словаря.
dict.get(key[, default]) # возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).
dict.items() # возвращает пары (ключ, значение).
dict.keys() # возвращает ключи в словаре.
dict.pop(key[, default]) # удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).
dict.popitem() # удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.
dict.setdefault(key[, default]) # возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ с значением default (по умолчанию None).
dict.update([other]) # обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
dict.values() # возвращает значения в словаре
for key in sorted(d): # сортировка словаря по ключу


# перебор элементов словаря

d = {'C':14, 'A':12, 'T':9, 'G':18}
for key in d
    print(key, end=' ') --> G T A T
for key in d.keys():
   print(key, end=' ') --> G T A T
for value in d.values():
    print(value, end=' ') --> 18 14 12 9
for key, value in d.items():
    print(key, value, end='; ') --> G 18; C 14; A 12; T 9;

d['aaa'] = ['a', 'b'] # одному ключу может соответствовать список заначений


# WORK WITH FILE

# r (read) - open for read (default)
# w (write) - open for write, file clear
# a (append) - open for write, write in end
# b (binary) - open in binary mode
# t (text) - open in text mode
# r+ - open for read and write
# w+ - open for read adn write, file clear
f = open("test.txt", "rb")
x = f.read(5) # read first 5 simbols
y = f.read() # чтение всего оставшегося файла
print(repr(x)) # выводит строку со служебными символами ()
x = x.splitlines() # разделение на строки без спец сиволов и перенос в список
x = f.readline() # чтение построчно, так как целый фаил может занимать много места и чтение по строкам рациональнее
x = x.rstrip() # убирание символов с права от строки
f.close

f = open("text.txt")
for line in f:
    line = line.rstrip()
    print(repr(line))
    # в конце остается пустая строка
x = f.read()
print(repr(x)) -->'' # выводит посленюю строку
f.close

# ЧТЕНИЕ ИЗ ФАЙЛА

with open('text.txt', 'r') as inf:
    s1 = inf.readline()
    s2 = inf.readline()

inf.readline() # читает строку
inf.read() # читает весь текст
inf.readline().strip() # убирает спец символы в строке('\t', '\n')
inf.read().splitlines() # делит текст на строки

with open('text.txt', 'r') as inf:
    for line in inf:
        line = line.strip()
        print(line) # чтение всех строк в файле

 




import codecs# for reading cirilic and other
 
with codecs.open('file.txt', encoding='utf-8') as fin:
    line = next(fin)
    print type(line)
    print line.strip()

# ЗАПИСЬ В ФАЙЛ

with open('text.txt', 'w') as out:
    ouf.write('Some text\n') # \n oбязательна иначе переноса не будет
    ouf.write(str(25)) # перевод в строку обязателен

# write file

f = open("test.txt", "w") # если такого файла нет, то он будет создан
f.write("hello")
f.write("world") --> helloworld # для переноса нужет \n

lines = ["Line 1", "Line 2", "Line 3"]
contents = "\n".join(lines)
f.write(contents) # будет записано 3 строки

#append in file

f = open("test_append.txt", "a") # будет создан файл даже если он не создан
f.write("Hello")

f.close

# with - same as open-close

with open("text.txt") as f, open("text_copy.txt", "w") as w:
    for line in f:
        w.write(line) # copy in text_copy
        line = line.rstrip()
        print(line)

f.close


# МОДУЛИ

# имя модуля - это имя файла без расширения
import my_module # импорт модуля
my_module.foo() # использование функции из импортированного модуля

from my_module import foo
foo() # импорт одной функции из модуля

from my_module import *
foo() # импорт всех функций

from my_module import foo as my_foo
my_foo() # импор функции из модуля и назначение ей особого имени

# Модуль os
os.path.join('.', 'dirname', 'filename.txt') # подключаемый модуль позволяющий 
# переделывать путь к файлу в разных ОС --> './dirname/filename.txt' или '.\dirname\filename.txt'
os.path.dirname(path) # возвращает имя директории пути path
os.path.abspath(path) # возвращает нормализованный абсолютный путь.
__file__ # возвращает путь к файлу
print(os.path.dirname(os.path.abspath(__file__))) # выведет один и тот же путь как из интерпритатора
# так и из среды разработки


# Модуль sys показывает список аргументов командной строки
# запуск через cmd 
python file.py
import sys
print(len(sys.argv)) --> 1 # показывает что программа запущенна с одним аргументом (file.py)
print(sys.argv) --> file.py

# Модуль subprocess может запускать внешние процессы с параметрами
subprocess.call(["python", "-h"])

subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None) # можно назначить stdout и тогда вывод будет осуществлен в фаил, а не командную строку

# Установка библиотек

# после установки miniconda с галочкой PATH
# cmd от админа
conda install requests # установка библиотеки для работы в интернете

# Модуль requests может взамодействовать с сайтами 
import requests
r = requests.get('http://example.com') 
print(r.text) # выведет текст сайта
print(r.status_code)
print(r.url)
print(r.headers['Content-Type'])

from requests import get
get('https://stepic.org/favicon.ico').headers['Server'] # show server name



# Библиотека NumPy # работа с числовыми массивами
conda install numpy
a = array([2, 3, 4]) # создание одномерного массива, массивы могут быть только одного типа
a.ndim --> 1 # размерность массива
a.shape--> (1, 3) # 1строка 3 столбца
z = zeros((3,2)) # заполнение массива 3 на 2 нулями
arange(10, 30, 5) # генерирование массива от 10 до 30 с шагом 5
linspace(0, 2, 9) # генерация массива от 0 до 2 (ключительно) в размере 9 точек
b = arrage(12).reshape(4, 3) # превращение одноменого массива в 4 на 3

# сложение массивов
a = array([10, 20, 30])
b = arange(3)
print(a) --> [10 20 30]
print(b) --> [0 1 2]
print(a + b) --> [10 21 32] # сложение и вычитание происходит поэлементно
print(a**2)--> [100 400 900]
print(2*sin(a)) --> [-1.08 1.82 -1.97]
print(a<20) --> [True Folse Folse]



# Библтотека matplotlib # построение графиков
conda install matplotlib



# УСЛОВИЯ
if foo == True:
...
if boo == False:
# сократим
if foo:
...
if not boo:


if len(value) > 0:
# сократим
if len(value):
# сократим
if value !=[]: # '' для строк, {} для словарей, set() для множеств, () для кортежей
# сократим
if value:

# ЦИКЛЫ
# по циклу лучше проходить не используя индекс, а проходя по значению

# если требуется иметь доступ к индексу и значению то стоит использовать функцию enumerate
my_list = ['Node1', 'Node2', 'Node3']
for i, value in enumerate(my_list):
    print(i, value)
# enumerate превращает список в кортеж, где по два элемента (( , ),( , ))


# функция формат {}.format (потом поискать в интернете)


# FUNCTION .join

l = ['a', 'b' , 'c']
s = ''
for value in l:
    s += value + ', '
print(s)
***
l = ['a', 'b' , 'c']
print(', '.join(l))
# если требуется преобразование
l = [1, 2 , 3]
print(', '.join(str(x) for x in l))


# так как значение по умолчанию для функции вычисляется один раз, не стоит использовать изменяющиеся обьекты (списки, словари)
def f(x, l=[]):
    l.append(x)
    return l
print(f(1)) -->[1]
print(f(2)) -->[1, 2]
print(f(3)) -->[1, 2, 3]
***
def f(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l
print(f(1)) -->[1]
print(f(2)) -->[2]
print(f(3)) -->[3]

# формирование словаря

def foo()
    somethink
cache = {x: foo(x) for x in range(-100, 100)}

# при генерации в круглых скобках производится экономия памяти

l = [...]
v1 = [x for x in l if x % 2 == 0]
v2 = (x for x in l if x % 2 == 0)

# ИДЕНТИФИКАТОР ОБЪЕКТА

x = [1, 2, 3]
print(id(x)) --->12345
print(id([1, 2, 3])) --->44385

# ОПЕРАТОР is проверяет ссылаются ли переменные на один и тотже обьект
x = [1, 2, 3]
y = x
y is x ---> True
y is [1, 2, 3] ---> False
x is None # проверяет объект на пустоту

type(x) #показывает тит объекта

Immutable                          Mutable
int                                list
float                              dict
complex(комплексные числа)         set
bool
tuple(кортеж)
str
frozenset(не изменяемое множество)

def от define(определим)

# +РАБОТА ФУНКЦИИ

a = []
def foo(arg1, arg2):
  a.append("foo")
foo(a.append("arg1"), a.append("arg2"))
print(a) --> ['arg1', 'arg2', 'foo']

# СТЕК ВЫЗОВА

x = [1, 2, 3]
print(x.pop())-->3
print(x)-->[1, 2]
print(x.append(4))-->None
print(x)-->[1, 2, 4]


# CLASSES

class MyClass:
    a = 10
    def func(self):
        print('Hello')
    def drive():
        print('Go Go Go')
print(MyClass.a) # MyClass.a атрибут класса MyClass
print(MyClass.func) #  MyClass.func атрибут класса MyClass
# в отличии от функций тело класса исполняется в момент определения самого класса и за ним закрепляется определенный namespace
print(MyClass.__dict__) # show attributes and other info of class
print(getattr(MyClass, 'a', 100))--> 10 #show attribute 'a' (quotes is necessary), 100 - return value, if attribute 'a' does not exist(не существует)
#100 - not necessary attrebute
MyClass.b = 'something' #in MyClass added attribute 'b' wint value 'something'
setattr(MyClass, 'c', 200) #in Myclass added attribute 'c' with value 200
del MyClass.a #deleting attribute 'a'
delattr(MyClass, 'b') #deleting attribute 'b'
#functions
MyClass.drive() --> Go Go Go #скобки это оператор вызова
MyClass.drive-->#show link
getattr(MyClass, 'drive')-->#show link
getattr(MyClass, 'drive')()-->Go Go Go
hasattr(MyClass, 'name')-->True/False #show есть ли такой attribute(var or method) in MyClass

class A:
    if hasattr(self, '__init__'):
        self.__init__()

# OBJECT OF CLASS

class MyClass:
    a = 10
    def func(self): #self - общепринятое название(можно заменить на любое другое),
        #when instance run func of class he вставляет youself за место self
        #по этому MyClass.func - запуститься, а a.func - выдаст ошибку так как будет передан аргумен в виде instance
        print('Hello')
x = MyClass() # x is instance(экземпляр) of class MyClass. MyClass() it's constructor of class MyClass
print(type(x))
print(type(MyClass))
b = MyClass()
print(MyClass.__dict__) #show all attributes
print(b.__dict__ ) #show empty list
b.a = 20
print(b.__dict__) #show attribute 'a'
del b.a 
print(b.a)-->10 #if we don't have attribute in instance of class, Python search attribute in class and parents




class Counter:
    pass # when hollow(empty) class
Counter -->class object
x = Counter() # x is instant object
x.count = 0
x.count += 1


class Counter:
    def __init__(self):  # a function __init__ принимает ещё не существующий instance(экземпляр) self
        self.count = 0 # к ещё не существующему instance, add attribute
Counter
x = Counter()
print(x.conut) --> 0
x.count += 1


class Counter:
    def __init__(self, start = 0):   
        self.count = start 
Counter
x1 = Counter(10) # аргумент 10 встает after self in def __init__
x = Counter()
print(x.conut) --> 0
x.count += 1

# METHOD
class Cat:
    def voice():
        print('mao')
bob = Cat()
bob.voice()--> #вызовет ошибку так как в def voice() нет аргумента, а показано что был передан один аргумент
print(Cat.voice) #покажет что это функция
print(Cat.voice) #покажет что это метод
#метод это таже функция, но у класса, метод привязан к конкретному обьекту, а функция не с кем не связана
#в функцию в классе(в метод), при вызове её от экземпляра передается сам экземпляр 'voice(bob)'

class Cat:
    def voice(*args): # *args - any quantity of arguments
        print('mao', *args)
jim = Cat()
jim.voice()-->mao (<__main__.Cat Object at 0x5234534534>,)#main - this file, 0x124232532 - place in storege


#__init__
#чтобы не add attribute thought func, we can add attribute when initing instance
class Counter:
    def __init__(self):  
        self.count = 0
    def inc(self):
        self.count += 1
    def reset(self):
        self.count = 0
x = Counter()#in this moment adding attribute count in instance, хотя функция __init__ на прямую не вызывалась
#если в __init__ добавить больше арибутов (__init__(self, name)) то получим конструктор
x.inc --> 1
print(x.count)
Counter.inc(x) -->2 # Тоже самое что и x.inc строчкой выше (Bound Method(связанный метод))
print(x.count)
x.reset()-->0
print(x.count)

#dry (don't repeat youself)
class Point:
    list_points = []
    def __init__(self, x, y):
        self.change(x, y)
        Point.list_pints.append(self) #для обращения к аттрибутам класса необходими указывать сласс
        #даже если функция внутри класса
    def change(self, x, y):
        self.x = x
        self.y = y
    def go_home(self):
        self.change(0, 0)

#моносостояние for instance
#when при changing or adding attribute in one instance происходит changing all instance 
class Cat:
    def __shared_attr = {
        'breed': 'pers'
        'color': 'black'
    }
    def __init__(self):
        self.__dict__ = __shared_attr
a = Cat()
b = Cat()
a.breed = 'pers'
print(b.bread)--> pesr

#public protected privated attr and methods
#public _protected __privated
#_protected - никак не защищает "_" просто общепринятое обозначение
class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport
    
    def print_public_data(self):
        self.__print_pvivate_data()

    def print_protected_data(self):
        print(self.__name, self.__balance, self.__passport)

account1 = BankAccount()
account1.__name -->Error
account1.__print_private_data() --> Error
account1.print_public_data #так можно
print(dir(account1)) #show all attr and private attr
account1._BankAccount.__print_private_data() #и так он показывает защищенные атрибуты
#по сути Python не защищает ничего

#property getter setter delete
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = values
    
    def delete_balance(self):
        del self.__balance
    
    balance = property(fget = get_balance, fset = set_balance, fdel = delete_balance)
    # short name for using func
a = BankAccount()
a.balance #вызов get_balance
a.balance = 100 #вызов set_balance
del a.balance #вызов delete_balance

#decorator property
#избавлеяет от двойной функциональности
class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    
    @property #1 превращаем нашу функцию в свойство путем декорирования
    def my_balance(self):#1 change name to my_balance
        return self.__balance

    @my_balance.setter #2 property of my_balance (то что был getterom (#1))
    def my_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value
    
    @my_balance.deleter
    def my_balance(self):
        del self.__balance

p = BankAccount('Tod', 900)
p.my_balance --> 900 # скобки не нужны так как это свойства  
p.my_balance = 901
p.my_balance --> 901
del p.my_balance
p.my_balance --> Error

#2
class Money():
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents

    @property
    def dollars(self):
        return self.total_cents//100

    @dollars.setter 
    def dollars(self, dollars):
        if isinstance(dollars, int) and dollars >= 0:
            self.total_cents = dollars*100 + self.total_cents%100
        else: print('Error dollars')

    @property
    def cents(self):
        return self.total_cents%100

    @cents.setter 
    def cents(self, cents):
        if isinstance(cents, int) and 100 > cents >= 0:
            self.total_cents = self.total_cents//100*100 + cents
        else: print('Error cents')

    def __str__(self): # __str__ change return of instance
        return f"Ваше состояние составляет {self.total_cents//100} долларов {self.total_cents%100} центов"
Bill = Money(101, 99)
print(Bill)  --> Ваше состояние составляет 101 долларов 99 центов
print(Bill.dollars, Bill.cents)  --> 101 99

#Вычисляемые Property
class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None
    
    @property
    def side(self):
        return self.__side
    
    @side.setter
    def side(self, value):
        self.__side = values
        self.__area = None #when change side, area change to None
    
    @property #for more comfortable call to area do it to property
    def area(self):
        if self.__area is None: # что бы не вычеслять area каждый раз, а только в первый раз
            print('calculate area')
            self.__area = __side**2
        return self.__area
a = Square(5)
a.area -->calculating area 25
a.area --> 25
a.side = 6
a.area -->calculating area 36
a.area -->36

#staticmethod and classmethod
class Example:
    def hello():
        print(hello) #работае только при вызове от класса
    
    def instance_hello(self):
        print(f'instance_hello {self}') #работает только при вызове от instance

    @staticmethod
    def static_hello():
        print(f'static_hello') #работает ото всех
    
    @classmethod
    def class_hello(cls): #работает ото всех, cls - class, и от instance и от class в cls попадает class
        print(f'class_hello {cls}')

Example.hello() --> hello
a = Example
a.hello() --> Error
Example.instance_hello() --> Error
a.instance_hello() --> instance_hello < a >
Example.static_hello() --> static_hello
a.static_hello() --> static_hello
Example.class_hello()--> class_hello <class Example>
a.class_hello()--> class_hello <class Example>

#способы обращения к переменным/методам класса
#1 если два файла в одной папке
import file1
Example.method1()
2#
class DepatrtmentIT:
    PYTHON_DEV = 4
    GO_DEV = 3
    REACT_DEV =2
    def info(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)
    def info2(self):
        print(DepatrtmentIT.PYTHON_DEV, DepatrtmentIT.GO_DEV, DepatrtmentIT.REACT_DEV)
    @property
    def info_prop(self):
        print(self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)
    @classmethod
    def info_class(cls):
        print(cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)
    @staticmethod
    def info_static():
        print(DepatrtmentIT.PYTHON_DEV, DepatrtmentIT.GO_DEV, DepatrtmentIT.REACT_DEV)

#включения сеттора при инициализации
from string import digit #digit - it is just list of digit
class User:

    def __init__(self, login, password):#так как сеттер и переменная называются одинаково
        # во время инициализации происходит проверка пароля через сеттер
        self.login = login
        self.password = password
    @property
    def password(self):
        print('getter called')
        return self.password
    @staticmethod
    def is_include_number(password):#just checing(проверка) to having digit in pass
        for digit in didgits:
            if digit in password:
                return True
        return False
    @password.setter
    def password(self, value):
        print('setter called')
        if not isinstance(value, str):
            raise TypeError('Password not the string')
        if len(value)<4:
            raise ValueError('Pass is too short, need min 4 simbols')
        if len(value)>12:
            raise ValueError('Pass is too long, need max 12 simbols')    
        if not User.is_include_number(value):
    



# extend

class Song:
    tags = []
    def __init__(self, artist, song):
        self.artist = artist
        self.song = song
        #self.tags = []
    def add_tags(self, *args):
        self.tags.extend(args) # extend() - тоже самое что и append(), но может добавлять несколько элементов
song1 = Song("Shakey", "Roll")
song1.add_tags("Americana", "Country")
song2 = Song ("Neuromonah", "Holodno")
song2.add_tags("Russian", "Drum")
print(song2.tags) --> "Americana" "Country" "Russian" "Drum" # все добавилось в tags = [] так как не объявлен атрибут self.tegs и интерпритатор ищет его в классе
таково бы не случилось если ракоментировать self.tags = [] и закоментировать tags = []

#MAGIC METHOD
#__repr__ and __str__
class Lion():
    def __init__(self, name):
        self.name = name
    def __repr__(self):#заменяет обычное отображение класса в том числе и для разработчиков, если нет
        return f'The object Lion - {self.name}' 
    def __str__(self):#заменяет обычное отображение класса в print() and str()
        return f'Lion - {self.name}'
a = Lion('alex')
a #__repr__
str(a) #__str__
print(a) #__str__

#__len__ and __abs__
class Otrezok:
    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self): #setting for comand 'len()'
        return abs(self)

    def __abs__(self):# setting for comand 'abs()'
        return abs(self.x2 - self.x1)

a = Otrezok(4, 8)
len(a) --> 4 #show 4, таким образом мы настроили work function len of our class


#__add__,__radd__,__mul__,__rmul__,__sub__,,__truediv__
#сложение, умножение, вычитание, деление. #r - тажа операция, но с заменой слагаемых/мнжителей местами
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ calc')
        if isinstance(other, BancAccount): #проверяем если складываем с такимже классом
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return self.balance + other
        raise NotImplemented
    
    def __radd__(self, other):
        print('__radd__ call')
        return self+other
r = BankAccount('Ivan', 200)
r+12 #run comand r.__add__(12)
12+r #run comand r.__radd__(12) #с начала Python пытаеться вызвать команду __add__ и когда это не получаеться он меняет слогаемые местами и вызывает команду __radd__

#2 передача обьекта а не числа
class BankAccount:
    def __init__(self, name, balance):
        print('New obj init')
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ calc')
        if isinstance(other, BancAccount): 
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return BankAccount(self.name, self.balance + other) #возвращаемь новый созданный обьект
        raise NotImplemented
t = BankAccount('Ivan', 200)
d = t + 30 #now we able to do so. 'd' is new obj

#методы сравнения
# __eq__ == (equal)
# __ne__ != (not equal)
# __lt__ < (less than)
# __le__ <= (less euqal)
# __gt__ >
# __ge__ >=

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area == other.area
        
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area < other.area

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

a = Rectangle(1, 2)
b = Rectangle(1, 2)
a == b --> True
b > a --> True #хоть мы и не делали __gt__, Python пробует перевернуть a < b и такая функция есть
#но нужно что бы второй аргумент тоже имел функцию a.__lt__(b).
b != a --> False # not (b == a) , __ne__ можно не реализовывать
b >= a --> True # a <= b 



#__eq__ and __hash__
#если переопределяем eq то нужно переопределить и hash, так как по умолчанию hesh от ссылки, а ты её переопределяем
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y = other.y
    def __hash__(self):
        return hash((self.x, self.y))
p1 = Point(3, 4)
p2 = Point(3, 4)
p3 = Point(6, 7)
p1 == p2 --> True
hash(p1) == hash(p2) --> True
p1 == p3 --> False
hash(p1) == hash(p3) -->False

#__bool__
class Point:
    class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __len__(self): #так как bool([])-->False и т.д. Bool ориентируеться по len, и парой len достаточно. Если bool не определен то он идет в len
        return abs(self.x - self.y)
    def __bool__(self):
        return self.x != 0 or self.y != 0
bool(Point(3, 4))-->True 
bool(Point(0, 0))-->False

#__call__
# '()' - оперератор вызова
#7 видов вызываемых(callable) объектов в Python
# 1 вызываемые функции len() abs() int() и т д
# 2 callable method a = [1, 2, 3] a.sort()
# 3 собственные функции def
# 4 classes Cat()
# 5 instance is not callable, but we might inicialising method __call__
class Cat:
    def __call__(self, *args, **kwargs):
        print('may')
bob = Car()
print(callable(bob))-->True
bob()--> 'may'
# 6 method of classes
# 7 function-generator
def f():
    n = 0
    while True:
        yield n
        n += 1
print(callable(f))--> True

#__call__
#избавляемся от замыкания
class Counter:
    def __init__(self):
        self.counter = 0
        self.summa = 0
        sefl.length = 0
    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length = += len(args)
        print(f'Наш экземпляр вызывался {self.counter} раз')
    def averege(self):
        return self.summa /self.length
r = Counter()
r(2, 4, 5, 6) # тепер можно вызавать таким образом instance
r.average()
#избавляемся от декорирования
from time import perf_counter
class Timer:
    def __init__(self, func):
        self.fn = func
    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f'call function {self.fn.__name__}')
        result = self.fn(*args, **kwargs)
        finish = pers_counter()
        print(f'функция отработала за {finish - start}')
        return result
#@Timer    
def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= 1
    return pr

def fib(n):
    if n<=2:
        return 1
    return fib(n-1) + fib(n-2)

fact = Timer(fact) #либо можно было поставить декоратор @Timer
fact(7)-->5040

fib = Timer(fib)
fib(20)
Timer(fib)(7) #декорируем и сразу вызываем с аргументом, сама фунция фиб здесь не задекорирована, задекорирован только ее вызов

#полиморфизм - это когда методы и атрибуты у разных классов называються одинакого и их можно прогонять через цикл и так далее

#__getitem__,__setitem__ and __delitem__ - настройка оператора '[]'
class Vector:
    def __init__(self, *args):
        self.values = args
    def __repr__(self):
        return str(self.values)
    def __getitem__(self, item):
        if 0<=item<len(self.values):
            return self.values[item]
        else:
            raise IndexError('Indeks out of range in our collection')
    def __setitem__(self, key, value):
        if 0<=key<len(self.values):
            self.value[key] = value
        else:
            raise IndexError('Indeks out of range in our collection')
    def __delitem__(self, item):
        if 0<=key<len(self.values):
            del self.value[key]
        else:
            raise IndexError('Indeks out of range in our collection')
v6 = Vector(5, 34, 43)
v6[2]-->43
v6[1] = 3
v6-->[5,3,43]
del v6[0]
v6-->[3, 43]

#__iter__ and __next__
a = [1, 2, 3]
b = iter(a) #сказали какой объект итерировать #same as b = a.__iter__(a)
next(b)-->1 #same as b.__next__()
next(b)-->2
next(b)-->3
next(b)-->StopIteration #Пройтись по объекту можно только один раз

#1
class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks
    def __getitem__(self, item): #не основной способ реализации итерации(не работает если есть __iter__), (не рекомендуется)
        return self.name[item]
    def __iter__(self):
        print('call iter student')
        self.index = 0 #нужно для next
        return self # полная итерация и с ней надо реализовать __next__                                                
        #return iter(self.name) - если вставить это то у строки реализован итер будет за счет 'str' и метод next не нужен
    def __next__(self):
        if self.index >= len(self.name):#проверяем что индекс не вышел за границы
            raise StopIteration
        letter = self.name[self.index] #если вставить сразу в return то будет пропущенна первый элемент
        self.index += 1
        return letter
igor = Student('Igor', 'Nikolaev', [3, 4, 5, 6, 7])
for i igor:
    print(i)
#2
class Marks:
    def __init__(self, values):
        self.value = values
    def __iter__(self):
        print('call iter marks')
        self.index = 0
        return self
    def __next__(self):
        print('call next marks')
        if self.index >= len(self.value):
            raise StopIteration
        letter = self.value[self.index] 
        self.index += 1
        return letter
class Student:
    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks
    def __iter__(self):
        print('call iter student')
        self.index = 0 #нужно для next, при каждом новом вызове приходит в изначальное положение
        return iter(self.marks)                                                
    def __next__(self):
        print('call next students')
        if self.index >= len(self.name):#проверяем что индекс не вышел за границы
            raise StopIteration
        letter = self.name[self.index] #если вставить сразу в return то будет пропущенна первый элемент
        self.index += 1
        return letter
m = Marks([3, 4, 5, 6, 7])
igor = Student('Igor', 'Nikolaev', m)
for i in igor:
    print(i)

# НАСЛЕДОВАНИЕ(EXTEND) CLASS
# extend(расширяет) иначе говоря class a(b) - класс b расширяет класс а

class DerivedClassName (Base1, Base2, Base3): # Base1..3 классы от которых идет наследование


class MyList(list):
    def even_lenght(self):
        return len(self) % 2 == 0
x = MyList()
print(x)--> []
x.extend([1, 2, 3, 4, 5])
print(x)--> [1, 2, 3, 4, 5]
print(x.even_lenght()) -->False
x.append(6)
print(x.even_lenght()) -->True  # def __repr__(self): #от representation print смотрит в классе как показать что либо (урок 1.6.3)


class D: pass
class E: pass
class B(D, E): pass
class C: pass
class A(B, C): pass
issubclass(A, A) --> True # every class heir(наследник) is himself. issubclass is function for проверки является ли first argument heir of second argument
issubclass(C, D) --> False 
issubclass(A, D) --> True
issubclass(C, object) --> True # class object ancestor(предок) for every classes
issubclass(object, С) --> False # class object don't have parents
x = A()
isinstance(x, A) --> True # isinstance проверяет является ли объект экземпляром какого-либо класса
isinstance(x, B) --> True
isinstance(x, object) --> True
isinstance(x, str) --> False
print(A.mro()) # от method resolution order, показывает порядок перебора классов в множественном наследовании

#Расширение стандартных классов
#так как все наследуеться(extend) от object то если dir(object) то можно увидеть все его методы, а значит они все есть и у всех subclasses тоесть у всех
class NewInt(int):
    def repeat(self, n=2):
        return int(str(self)*n)
    def to_bin(self):
        return int(bin(self)[2:]) #bin is function for transcript in to binary
print(NewInt())
a = NewInt(9)
print(a.repeat())  # печатает число 99
d = NewInt(a + 5)
print(d.repeat(3)) # печатает число 141414
b = NewInt(NewInt(7) * NewInt(5))
print(b.repeat())
print(b.to_bin()) # печатает 100011 - двоичное представление числа 35

#Overriding
class Person:
    def __init__(self, name):
        print('init Person')
        self.name = name
    def breathe(self):
        print('Person breathe')
    def walk(self):
        print('Person walk')
    def combo(self):
        self.breathe()
        self.walk()
class Doctor(Person):
    def breathe(self):
        print('Doctor breathe')
    def __str__(self):
        return f"Doctor {self.name}"
p = Person('Adam')-->init Person
d = Doctor('John')-->init Person #если метода нет в классе, то поиск идет в родительском
p.combo()-->Person breathe \n Person walk
d.combo()-->Doctor breathe \n Person walk #так как метода combo в subclass нет он ищет в родительском, но сам метод combo ищет с начала методы в основном класе хоть и сам находиться с родительском

#Extending расширение класса
class Person:
    def combo(self):
        if hasattr(self, 'breathe')# for Person is not running
            self.breathe()
class Doctor(Person):
    def breathe(self): #method breathe extending(расширяет) class Doctor
        print('Doctor breathe')
p = Person('Adam')
d = Doctor('John')
p.combo()
d.combo()

#supper
#superclass - родительский класс
class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0
class MyList(list, EvenLengthMixin):
    def pop(self):
        x = super(MyList, self).pop() #функция супер застовляет искать функцию в предках MyList исключая MyList, тоже самое list.pop(self)
        print("Last valut is ", x)
        return x
ml = MyList([1, 2, 4, 17])
z = ml.pop() --> Last value is 17
print(z) --> 17
print(ml) --> [1, 2, 4]

#2 избавляемся от дублирования
class Person():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.age = 50
class Doctor(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname) #should running method supperclass first, becouse attr maight be override
        self.age = age

#Multiple extend (множественное наследование), __mpo__
class Doctor:
    def graduate(self):
        print('Ура, я отучился на доктора')
    def can_build(self):
        print('Я доктор, я тоже умею строить, но не очень')       
class Builder:
    def graduate(self):
        print('Ура, я отучился на строителя')
    def can_build(self):
        print('Я строитель, я умею строить')   
class Person(Doctor, Builder): #first method search in main class after первый по порядку наследования
    def graduate(self):
        print('Посмотрим, кем я стал')
        super().graduate()
        Builder.graduate(self) # так можно обратиться к методу не попавшему в наследование
s = Person()
s.graduate()--> Посмотрим, кем я стал/Ура, я отучился на доктора/Ура, я отучился на строителя #
print(Person.__mro__)--> (<class '__main__.Person'>, <class '__main__.Doctor'>, <class '__main__.Builder'>, <class 'object'>) #__mpo__ - show порядок inheritance (наследования)

#Add atrib to instance
class Doc:
    def __init__(self, x):
        self.x = x
x = Doc(5)
x.q = 8
print(x.q)-->8

#__slots__ - ограничение на add attrib, __sizeof__ - show size
#operation with slots run more faster and take less memory
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Point_slots:
    __slots__ = ('x', 'y') #перечисляем что можно add to instance
    def __init__(self, x, y):
        self.x = x
        self.y = y
s = Point(3, 4)
print(s.__sizeof__(), s.__dict__.__sizeof__())_--> 16 52 #show size instance and his dict
d = Point_slots(3, 4)
print(d.__sizeof__()) --> 16 # instance with slots don't have a dict
d.x --> 3 #get
d.x = 5 #set
del d.x #delete
d.x = 6 #add
d.q --> Error #for other attrib

#Slots property inheritance
class Restangle:
    __slots__ = '__weidth', 'heigth'
    def __init__(self, a, b):        
        self.weidth = a #так как мы обращаемся к prorerty которое задекорировано вызывается width.setter, тоесть на прямую к __width мы не обращаемся
        self.heigth = b
    @property    
    def weidth(self):
        return self.__weidth
    @weidth.setter
    def weidth(self, value):
        print('setter called')
        self.__weidth = value
class Square(Restangle): 
    __slots__ = 'color' # в потомке достаточно разрешить только новые переменные
    #__slots__ = tuple() #для просто запрета добовления всех других переменных
    def __init__(self, a, b, color):
        super().__init__(a, b)
        self.color = color

# EXCEPTIONS

try:                          # try ... except TypeError - catch Error (TypeError) and do somethink after except
    x = [1, 2, "hello", 7]
    x.sort
    print(x) 
except TypeError:
    print("Type Error :-(")
except ZeroDivisionError:
    print("ZeroDivisionError :-(") # we can make several exception 

print ("I can natch")
# if i:n function have error, then function return - None


#catch all exception
#1
try:
    1/0
except:
    print('Error')
#2
try:
    1/0
finally:
    print('end')

#else and try
try:
    1/0
except:
    print('Error')
else: print('None error') #run if don't have exception
finally:
    print('end')

#alias for except
try:
    1/0
except ZeroDivisionError as ERR: #ERR our alias
    print('Error')
#2
try:
    [1, 2, 3][15]
except (KeyError, IndexError) as ERR: #one alias for two exception
    print(f'Logging error: {ERR}, {repr(ERR)}') --> Logging error: list index out of range, IndexError('list index out of range')
#3
try:
    [1, 2, 3][15]
except (KeyError, IndexError) as ERR: #one alias for two exception
    print(f'Logging error: {ERR}, {repr(ERR)}')
    raise TypeError('ошибка типа') from None #показывате что ошибки не совпадают, но from None делает так что показываеться только raise. По умолчанию from ERR.
#4
try:
    raise ValueError('ошибка значания') #вызываем ошибку
except ValueError as first:
    try:#пытаемся обработать ошибку
        raise TypeError('ошибка типа')
    except TypeError as second:
        raise Exception('Big Exception') from <None, first, second> #Nono - show only last raise, first - show all rise, second - show second and last raise

#exception args
a = TypeError(1, 2, 3, 'ERROR')
print(a.args) --> 1, 2, 3, 'ERROR'


def f(x, y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError) as e: # catch in one exception two errors
        print(type(e)) # выводим параметры ошибки (и в строках ниже тоже)
        print(e)
        print(e.args)
    finally:  # блок finally запускается в любом случаи, была поймана ошибка или нет
        print("finally")
print(f(5, 0))

#raise 

def greet(name):
    if name[0].isupper():
        return "Hello,  " + name
    else:
        raise ValueError (name + " is inappropriate name") # is crate me exception

print(great("Anton"))
print(great("anton")) --> ValueError: anton in inappropriate name


# me can catch my exception
def greet(name):
    if name[0].isupper():
        return "Hello,  " + name
    else:
        raise ValueError (name + " is inappropriate name")

while True:
    try:
        name = input("Please enter you name: ")
        greeting = great(name)
        print(greeting)
    except ValueError:
        print("Please try again")
    else:
        break # if don't catch break

#MY EXCEPTION
# if we wont see our Error_name, then we create own Error_class
class BadName(Exception): # Exception is main class all exceptions
    pass

def great(name):
    if mane[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(name + " is inappropriate name")

print(great("Anton"))
print(great("anton"))--> BadName : antom is anapropriate name
#2 __init__
class MyException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else: self.message = None
    def __str__(self):
        print('str called')
        if self.message:
            return f'MyException ({self.message})'
        else: return 'MyException is empty'
raise MyException('hello', 1, 2, 3) --> MyException (hello)

# how catching errors
#1
def second():
    print('second start')
    1/0
    print('second finish') #this line won't be printing
def first():
    print('first start')
    try:
        second()
    except ZeroDivisionError:
        print('handing first')
    print('first second')
print('main')
#2
def second():
    print('second start')
    try:
        1/0
    except ZeroDivisionError:
        print('handing second')
    print('second finish') #this line will be printing
def first():
    print('first start')
    second()
    except ZeroDivisionError:
        print('handing first')
    print('first second')
print('main')

# IMPORT
(2.2.1)

#exceptions.py
class BadName(Exception):
    pass

def great(name):
    if mane[0].isupper():
        return "Hello, " + name
    else:
        raise BadName(name + " is inappropriate name")
print("Import is execution")

#import_lesson.py

import exceptions

print(exceptions.great("Students"))
-->
Import is execution # becouse import исполняется in time объявления



# что бы не исполнять не нужный код во время импорта в другой файл
# есть паттерн проверки по имени. Если прописать print(__name__) в файле и запустить из это го же файла 
# --> __main__


# fib.py
def fib(k):
    if k == 0 or k == 1:
        return 1
    else:
        return fib(k - 1) + fib(k -2)

if name == "__main__": # если  запуск из файла --> __main__
    print(__name__)
    print(fib(31)) # это строка исполняется очень долго и импорт её очень затратен

# import_lesson.py
import fib # если запуск из файла с импортом то имя будет fit и строки ниже if name == "__main__": не исполнятся


# большой урок 2.2.3 про import 
# 1) импорт исполняется один раз 
# 2) есть словать импорта куда всегда идет обращения, что бы не исполнять импорт 2 раза
# 3) если в словаре нет поиск идет по внешним библиотекам 

# IMPORT PART OF SOMETHINK
from exceptions import BadName, greet #импорт из файла exceptions.py  класса BadName и функции greet

from exceptions import BadName, greet as exc_greed # теперь в данном файле функция greed именнуется как exc_greed

from exceptions inport * # импортируются все имена exceptions.py, кроме имен начинающихся с "_" и не перечисленных в 
# __all__ если такая функция имеется

# exceptions.py
GREETING = "Hello"

class BadName(Exception):
    pass

def great(name):
    if mane[0].isupper():
        return GREETING + name
    else:
        raise BadName(name + " is inappropriate name")

__all__ = ["BadName", "greet"] # GREETING импортировано не будет

# PIP - Утилита pip позволит нам устанавливать пакеты из репозитория Python Package Index
pip --version
# или
pip3 --version


# ITERATOR

lst = [1, 2]
iterator = iter(lst)
print(next(iterator)) --> 1
print(next(iterator)) --> 2
print(next(iterator)) --> StopIteration


for i in lst:
    print(i)
# same as
it = iter(it)
while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break



# iterator in my_class
class RandomIterator:
    def __next__(self):
        return 0

x = RandomIterator()
print(next(x))



from random import random

class RandomIterator:
    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random
        else:
            raise StopIteration

x = RandomIterator(3)
print(next(x)) # next(x) эквивалентно x.__next__() 
print(next(x))
print(next(x))
print(next(x))--> StopIteration

# "for" in my_class
from random import random

class RandomIterator:
    def __iter__(self):
        return self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random
        else:
            raise StopIteration

for x in RandomIterator(10):
    print(x)

# "for" in my_class2
class DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0
    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            return self.lst[self.i-2], self.lst[self.i-1]
        else:
            raise StopIteration

class MyList(list)
    def __iter__(self): 
        return DoubleElementListIterator(self)

for pair in MyList([1, 2, 3, 4]): 
    print(pair)
#Метод __iter__() запускается один раз при создании экземпляра класса MyList и в этот момент 
# этот созданный экземпляр становится "итерируемым" (интерпретатор запоминает все, что ему нужно 
# для работы про этот объект). Дальше вы уже работаете с этим экземпляром и все что вы делаете, 
# в том числе итерируетесь по нему (вызываете метод next), связано именно с этим экземпляром. 
# При создании нового экземпляра __iter__() будет запущен еще раз, но этот вызов будет связан 
# именно с этим новым экземпляром и никак не повлияет на счетчики ранее созданных экземпляров.

# GENERATOR
# Генератор списка
a = [i**2 for i in range(1, 6)]
print(a)-->[1, 4, 9, 16, 25]#в памяти записан весь список

a = [i**2 for i in range(1, 100000000000000)]
print(a)-->Error #в память не влезает весь список
# Выражение-гениратор
a = (i**2 for i in range(1, 100000000000000))
print(a)-->generator #в памяти список не хранится
for i in a:
    print(i) -->1, 2, ... 100000000 #будет все выведено так как в памяти хранится только next element
#минус в том что пройтись можно только один раз, не применить len(), не применить индекс

#iter - так работает выражение-генератор
s = [1, 2, 3]
d = iter(s)
next(d)
...
next(d)

# yield - это отложенное исполнение при этом не требующее next и iter
#1
def semple_gen():
    print(1)
    yield 1
    print(2)
    # retunt "No more lements" - если вставить эту строку, то после return ничего читаться не будет,
    # будет брощена StopIteration: No more elements
    yield 2
    print (3)
gen = simple_gen()
x = next(gen)
print(x) --> 1
y = next(gen)
print(y) --> 2
z = next(gen) --> StopIteration

#2
from random import random
def random_generator(k):
    for i in range(k):
        yeild random()
gen = random_generator(3)
for i in gen:
    print(i)

#3
def genf():
    for i in ['a', 'b', 'c']:
        yield i
        print('s')
g = genf()
print(next(g))-->a
print(next(g))-->s \n b 
print(next(g))-->s \n с

#4
def fact(n):
    pr = 1
    for i in range (1, 1+n):
        pr = pr*i
        yield pr
for i in fact(10):
    print(i, end= ' ')


# MODULE OS

import os
import os.path

print(os.getcwd())# show used dirrectory interpritator
print(os.listdit.("Test")) # show files in derrectory "Test"
print(os.path.exists("file.py"))--> True/False # show exists(существует) file or folder
print(os.path.isfile("file.py"))--> True # is file or not
print(os.path.isdir("Test"))-->True # is dirrectory or nor
print(os.path.abspath("file.py")) # show absolutely way to file
os.chdir("2") # change dirrectory
os.chdir(r"C:\\Learning\Python\2\2.4.6\sample") # for windows  '\\' and 'r'

for current_dir, dirs, files in os.walk("."): # "." - is текущая dir
    print(current_dir, dirs, files) # show all dir and files

# MODULE SHUTIL

import shutil

shutil.copy("tests/test1.txt", "tests/test2.txt") # copy test1.txt in dir tests to test2.txt in dir tests
shutil.copytree("tests", "tests/tests") # copy folder "tests" to tests/tests


# FUNKTION map()
# map is itetable function
n, k = map(int, input().split()) #прогоняет список через нужную функцию
# same as
x = input().split()
n, k = (int(i) for i in x)

def addition(n): 
    return n + n  
numbers = (1, 2, 3, 4) 
result = map(addition, numbers) 
print(list(result))-->[2, 4, 6, 8]


numbers1 = [1, 2, 3] 
numbers2 = [4, 5, 6] 
result = map(lambda x, y: x + y, numbers1, numbers2) 
print(list(result)) --> [5, 7, 9]


def func(el1, el2): 
    return '%s|%s' % (el1, el2)
list(map(func, [1, 2], [3, 4, 5]))--> ['1|3', '2|4']

dict(map(lambda *args: args, [1, 2], [3, 4]))--> {1: 3, 2: 4} #удобное создание словаря


numbers = map(str, [1, 2, 3, 4, 5])
print(repr(" ".join(numbers)))
# FUNCTION filter

x = input().split()
xs = (int(i) for i in x)

def even(x):
    return x % 2 == 0 -->T/F

evens = filter(even, xs) # прогоняет list/cortage (xs) throw function (even), if even is True, element of xs append in evens
for i in evens:
    print(i)
# same as
evens = list(filter(even, xs)) # filter это итератор, если его поместить в list то он достанет все обьекты итератора (можно использовать если конечное число элементов и ест не много памяти)
print(evens)

# FUNKTION lambda

def identity(x):
    return x % 2 == 0
a = identity(x)
# сократим
a = lambda x: x % 2 == 0


print(lambda x: x + 1)(3)-->4


add_one = lambda x: x + 1
add_one(2) --> 3


x = input().split()
xs = (int(i) for i in x)
evens = list(filter(lambda x: x % 2 == 0, xs ))
print(evens)


x = [
    ("55555", "333", "666666"),
    ("7777777", "55555"),
    ("4444", "666666")
]
def length(name):
    return len(" ".join(name))
name_lengths = [length(name) for name in x]
print(name_lengths)
x.sort(key = length)
print(x)
# same as
x = [
    ("55555", "333", "666666"),
    ("7777777", "55555"),
    ("4444", "666666")
]
x.sort(key = lambda name: len(" ".join(name)))
print(x)

# LIB OPETATER

import operator as op

print(op.add(4, 5)) # сложение
print(op.mul(4, 5)) # умножение
print(op.contains([1, 2, 3, 4, 5], 6))-->False # проверяет наличия числа в контейнере

x = [1, 2, 3]
f = op.itemgetter(1) # выбран element with index 1 # f(x) == x[1]
print(f(x))-->2 # x[1]

x = {"123": "asfd"}
f = op.itemgetter("123")
pritn(f(x))

f = op.attrgetter("sort") #f(x) == s.sort
print(f([]))

x = [
    ("55555", "333", "Rosssum"),
    ("7777777", "curry"),
    ("4444", "backus")
]
x.sort(key = op.itemgetter(-1)) #sort by last element
print(x)


# LIB FUNCTOOLS
from functools import partial

x = int("1101", base=2)
print(x)-->13
#same as
int_2 = printab(int, base =2)
print(x) -->13


import operator as op
from functools import partial
x = [
    ("55555", "333", "Rosssum"),
    ("7777777", "curry"),
    ("4444", "backus")
]
sort_by_last = partial(list.sort, key=op.itemgetter(-1))
print(x)
#same as
sort_by_last(x) #при помощи функции partial функция sotr_by_last запоминает параметры, что их не нужно вводить снова
print(x)

y = ["abc", "cba", "abb"]
sort_by_last(y)
print(y)

# PEP8 AND DOCUMENTATION
# https://www.python.org/dev/peps/pep-0008/ - EN
# http://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html или http://defpython.ru/pep8 - RU


class my_class:
    """
    documentation of my_class
    """
    pass
print(my_class.__doc__) 


print(str.find.__doc__) # документация какой-либо функции

# MODULE RE РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ

import re


pattern = r"abc"  # r - raw значит читается как пишется
string = "abcd"
match_object = re.match(pattern, string) # проверяет начинается ли наша строка с "abc"--> (0, 3) и др параметры
print(match_object)

pattern = r"abc"
string = "babcd"
match_object = re.search(pattern, string) # проверяет имеет ли наша строка  "abc" --> (1, 4)  и др параметры
print(match_object)

pattern = r"a[abc]c" # вторым символом подходящим под шаблон может быть a, b or c (acc - подойдет)
string = "abc, acc, aac"
all_inclusions = re.findall(pattern, string) # выводит все подходящие шаблоны
print(all_inclusions)

fixed_typos = re.sub(pattern, "abc", string) # заменяет всё на "abc"
print(fixed_typos)

# pattern = r"a[a-c]c" # [a-zA-Z] -- for all simbols alphabet
# pattern = r"a.c" # for any simbols
# pattern = r"ab*a" # любое количество символа b включая 0 (aa, abba - подойдет )
# pattern = r"ab+a" # любое количество символа b от 1 
# pattern = r"ab?a" #  количество символа b от 0 до 1
# pattern = r"ab{3}a" # количество символа b 3
# pattern = r"ab{2, 4}a" # количество символа b от 2 до 4
# pattern = r"a[ab]+a" # ищит жадным способом (из abaaba - вылезит вся строка)  https://stepik.org/lesson/24470/step/4?unit=6776
# pattern = r"a[ab]+?a" # ищит наименее жадным способом (из abaaba - вылезит  aba)
# [^a-c] -- указываем что  подходит всё кроме этого
# [] - можно указывать множества подходящих символов
# . ^ $ * + ? {} [] \ | () - метасимволы
# \d ~[0-9]
# \D ~[^0-9]
# \s ~[\t\n\r\f\v]
# \S ~[^\t\n\r\f\v]
# \w ~[a-zA-Z0-9_]
# \W ~[^a-zA-Z0-9_]
# \b ~начало и конец строки включая символы короме подчеркивания # \bcat\b - находит cat во всех местах кроме обрамленных [a-zA-Z0-9_] 
# \B ~\Bcat\B - находит cat во всех местах обрамленных [a-zA-Z0-9_]
# \A ~начало строки



pattern = r" english\?" #перед знаками нужно ставить "\" иначе в pattern попадет " english" (без "?")
string = "Do you speak english?"
match = re.search(pattetn, string)
print(match)


pattern = r"(test|text)*"
string = "testtext"
match = re.match(pattern, string)
print(match) --> (0, 8)

pattern = r"abc|(test|text)*"
string = "abctest"
match = re.match(pattern, string)
print(match) --> span = (0, 3) , match = "abc" # span - координаты подходящего выражения, match - часть подошедшего выражения, берется первое подходящее


pattern = r"((abc)|(test|text)*)"
string = "testtext"
match = re.match(pattern, string)
print(match) --> span=(0, 8), match='testtext'
print(match.groups()) --> ('testtext', None, 'text')  #сперва показана группа в скобках (abc|(test|text)*, потом abc, затем test|text (показан text т.к. это последнее вхождение)
print(match.group(0)) -->testtext # по умолчанию так же 0 (print(match.group()))
print(match.group(1)) -->testtext
print(match.group(2)) -->None
print(match.group(3)) -->text


pattern = r"(\w+)-\1" # берет все символы до дефиса и сравнивает их с первой группой(тоесть с группой до дефиса, тоесть test)
string = "test-test" # если вторая часть не совпадает test-text --> None
match = re.match(pattern, string)
print(match) --> span=(0, 9), match = 'test-test'


pattern = r"(\w+)-\1" 
string = "test-test chow-chow"
duplicates = re.sub(pattern, r"\1", string) 
print(duplicates) --> test chow


pattern = r"(\w+)-\1" 
string = "test-test chow-chow"
duplicates = re.findall(pattern, string) # берет только первое слово из подошедших групп
print(duplicates) --> ['test', 'chow']


pattern = r"((\w+)-\2)"  # https://stepik.org/lesson/24470/step/5?unit=6776
string = "test-test chow-chow"
duplicates = re.findall(pattern, string)
print(duplicates) --> [('test-test', 'test'),('chow-chow', 'chow')]


x = re.match(r"text", "TEXT", re.IGNORECASE)
print(x)-->'TEXT' # и др параметры

x = re.match(r"(te)*xt", "TEXT", re.IGNORECASE | re.DEBUG)
print(x) # выводит параметры поиска


# IMPORT CSV

#first name, last name, module1, module2, module3
#students, best, 100, 100, 100
#students, good, 90, 90.2, 100  # for using ','  students, good, 90, "90,2", 100 # можно оборачивать несколько строк в кавычки (запишется вместе со '\n')
import csv

with open("example.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

#first name last name   module1 module2 module3
#students   best    100 100 100
#students   good    90  90,2    100  

with open("example.tsv") as f: #tsv format using \t instead (вместо) "," comma
    reader = csv.reader(f, delimiter="\t")
    for row in reader:
        print(row)


students = [
    ["Greg", "Dean", 70, 80, 90, "Good job, Greg"]
    ["Wirt", "Wood", 80, 80.2, 80, "Nicely done"]
]
with open("example.csv", "a") as f:
    writer = csv.writer(f) #writer = csv.writer(f, quoting=csv.QUOTE_ALL) #поместить всё внутри кавычек
    for student in students:
        writer.writerow(student)
    #same as
    writer.writerows(students)

#IMPORT JSON
# example json
[
    {
        "first name": "Greg",
        "last name": "Dean",
        "certificate": true,
        "scores": [
            70,
            80,
            90
        ],
        "description": "Good job, Greg"
    },
    {
        "first name": "Wirt",
        "last name": "Wood",
        "certificate": true,
        "scores": [
            70,
            80,
            90
        ],
        "description": "Nicely Done"
    }
] 

import json

student1 = {
    'first name': 'Greg',
    'last name': 'Dean',
    'score': [70, 80, 90],
    'description': "Good job, Greg",
    'certificate': True
}

student2 = {
    'first name': 'Wirt',
    'last name': 'Wood',
    'score': [80, 80.2, 80],
    'description': "Nicely done",
    'certificate': True
}

data = [student1, student2]
print(json.dumps(data, indent=4, sort_keys=True)) #dumps - команда для print не путать с dump для файла, indent - количество пробелов, 
# sort_keys - сортировка ключенй в каждом объекте словаря

# for writing in file
with open("students.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)


#json.loads - for working in json format as python format
data = [student1, student2]
data_json = json.dumps(data, indent=4, sort_keys=True)
data_again = json.loads(data_json)
print(sum(data_again[0]["scores"])) -->240

#json.load - for working in json format as python format in file
with open("students.json", "r") as f:
    data_again = json.load(f)
    print(sum(data_again[1]["scores"])) -->240.2

# IMPORT XML

<studentsList>
    <student id='1'>
        <firstName>Greg</firstName>
        <lastName>Dean</lastName>
        <certificate>True</certificate>
        <scores>
            <module1>70</module1>
            <module2>80</module2>
            <module3>90</module3>
        </scores>
    </student>
    <student id='2'>
        <firstName>Wirt</firstName>
        <lastName>Wood</lastName>
        <certificate>True</certificate>
        <scores>
            <module1>80</module1>
            <module2>80.2</module2>
            <module3>80</module3>
        </scores>
    </student>
</studentsList>

from xml.etree import ElementTree

tree = ElementTree.parse("example.xml")
root = tree.getroot()
# root = ElementTree.fromstring(input()) - принимать из строки
print(root) # show root(main tag)
print(root.tag, root.attrib) #attrib - show attribute selected tag's

for child in root: 
    print(child.tag, child.attrib) # show tag and atribute children

print(root[0][0].text) # show children of children

for element in root.iter("scores"): # проход по заданным тегам, передав его в итер
    print(element)

for element in root.iter("scores"):
    score_sum = 0
    for child in element:
        score_sum += float(child.text)
        print(score_sum)

# writing on xml format
from xml.etree import ElementTree

tree = ElementTree.parse("example.xml")
root = tree.getroot()

tree.write("example_copy.xml") # make copy file

greg = root[0]
module = next(greg.iter("module"))
print(module1.text)
module.text = str(float(module.text) + 30) # change value on + 30

tree.write("example_modified.xml")

certificate = greg[2]
certificate.set("typy", "with distinction") #  <certificate typy="with distintion">True</certificate>

tree.write("example_modified.xml")

description = ElementTree.Element("description") # create element
description.text = "Showed excellent skills during the course"
greg.append(description)

tree.write("example_modified.xml")

description = greg.find("description") # find element inside greg
greg.remove(description) # remove element
tree.write("example_modified.xml")

#создание xml c нуля

from xml.etree import ElementTree

root = ElementTree.Element("student")
first_name = ElementTree.SubElement(root, "firstName")
first_name.text = "Greg"
second_name = ElementTree.SubElement(root, "secondName")
second_name.text = "Dean"
scores = ElementTree.SubElement(root, "scores")

module1 = ElementTree.SubElement(scores, "module1")
module.text = "100"

tree = ElementTree.ElementTree(root)
tree.write("student.xml")

# IMPORT LXML

from lxml import etree
import requests

res = requests.get("https://docs.python.org/3/")
print(res.status_code)
print(res.headers["Content-Type"])

parset = etree.HTMLParser() # работает с плохо сформированными частями язака HTML
root = etree.fromstring(res.text, parset)

for element in root.iter("a"):
    print(element, element.attrib)

#FOR СОБЕСЕДОВАНИЯ
def something():
    try:
        return print(1)
    finally:
        return print(2)
somothing()-->2

#2
def something():
    yield print(1)
    yield print(2)
somothing()-->ничего не выведет
for i in something():
    print(i)-->1\n None \n 2\n None
#3
1 + 1/3 + 2/3 = 1,9999 # к 1 + 0,33333 + 0,666666
1/3 + 2/3 + 1 = 2# 3/3 + 1
#4
await asinh


#ALGORITM
#fibonachi
def fib3(n):
    assert n >= 0 #Если условие утверждения assert истинно, то ничего не происходит и ваша программа продолжает выпол­няться как обычно. Но если же вычисление условия дает результат ложно, то вызывается исключение AssertionError
    f0, f1 = 0, 1
    for i in range(n -1):
        f0, f1 = f1, f1+f0
    return f1
fib3(8)-->21

#измерение времени работы
import time
def timed(f, *args, n_iter=100):
    acc = float("inf") #'inf' is plus infinity , '-inf' is minus infinity
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args):
        t1 = time.perf_counter()
        acc = min(acc, t1-t0)
    return acc
timed(fib3, 800)

#построение графика
from matplotlib import pyplot as plt
def compare(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, args) for arg in args], label=f.__name__)
    plt.legand()
    plt.grid(True)
fib1 = old_fib1
compare([fib1, fib3], list(range(20)))



#Создание виртуальных сред Creating Virtual Environments https://docs.python.org/3/tutorial/venv.html
python3 -m venv tutorial-env #venv - Модуль, используемый для создания и управления виртуальными средами
#Создав виртуальную среду, вы можете активировать ее.
#В Windows запустите:
tutorial-env\Scripts\activate.bat
#В Windows wits PowerShell
Set-ExecutionPolicy -ExecutionPolicy Unrestricted #разрешает выполнение скриптов PowerShell, запускать от Админа
tutorial-env\Scripts\activate.ps1
#В Unix или MacOS запустите:
source tutorial-env/bin/activate
#далее устанавливаем необходимые библиотеки
python -m pip install --upgrade pip
python -m pip install django
>>> import django #или python -m django --version
>>> print(django.get_version())#узнать версию Django

pip freeze > requirements.txt #создание файла версий пакета
pip wheel -w wheels -r requirements.txt #Это загрузит и соберет пакеты *.whl
#wheels #загрузка пакетов установки whl
На старой машине запустите pip freeze -l > packages.txt в virtualenv.
Переместите packages.txt на новую машину.
Создайте новый virtualenv на новой машине и введите его.
Установите пакеты из txt файла: pip install -r packages.txt.
РЕДАКТИРОВАТЬ: Если у вас нет доступа в Интернет на втором компьютере, вы можете продолжить с шага 2 с помощью:

Запустите pip wheel -w wheels -r packages.txt в venv на первой машине. Это загрузит и соберет пакеты *.whl для всех необходимых вам пакетов. Обратите внимание: предполагается, что обе машины похожи по ОС и архитектуре!
Скопируйте файлы колес на новую машину.
Создайте новый virtualenv на новой машине и введите его.
Установите пакеты с колес в новый virtualenv: pip install *.whl


#POSTGRESQL
#Доступ к PostgreSQL по сети, правила файерволла
netsh advfirewall firewall add rule name="Postgre Port" dir=in action=allow protocol=TCP localport=5432 #cmd
New-NetFirewallRule -Name 'POSTGRESQL-In-TCP' -DisplayName 'PostgreSQL (TCP-In)' -Direction Inbound -Enabled True -Protocol TCP -LocalPort 5432 #powershell
CD C:\Program Files\PostgreSQL\11\bin #все запускается из данной папки
#для powershell все комманды начинаются с ".\"
psql –V # show Version
createdb -U postgres testdb #где postgres суперпользователь, testdb новая база данных
Psql -U postgres –l #Проверить список активных баз
createuser –U postgres operator #где operator -имя нового пользователя
psql –U postgres #запуск итерактивной оболочки
ALTER ROLE operator SUPERUSER CREATEROLE CREATEDB #предоставление суперпользователя для operator
\du # show all superuser
CREATE DATABASE avecoder #create db, don't foget ";"
\l # show all database
\c avecoder # connet to db
CREATE TABLE table_name (Column_name + data_type + constraints (if any)) #create table
CREATE TABLE employee ( id BIGSERIAL, #BIGSERIAL - самоувеличивающееся значение
first_name VARCHAR (50), #VARCHAR - digits and characters, 50 - количество сиволов
last_name VARCHAR (50),
gender VARCHAR (6),
email VARCHAR (150),
date_of_birth DATE);
\d #show tables list (when we in db)
#we see our table and table_id_seq - последовательность созданная BiGSERIAL 
\d table_name #show table
DROP TABLE table_name; #delete table
CREATE TABLE employee ( id BIGSERIAL NOT NULL PRIMARY KEY, first_name VARCHAR (50) NOT NULL, last_name VARCHAR (50) NOT NULL, gender VARCHAR (6) NOT NULL, email VARCHAR (150), date_of_birth DATE NOT NULL); #NOT NULL - не может быть пустым, PRIMARY KEY - число уникольно и добавить такоеже в таблицу не возможно
INSERT INTO employee (first_name, last_name, gender, email, date_of_birth) VALUES ('John', 'Doe', 'MALE', 'Jd@mail.com', '2000-01-01'); #insert table
\dt #show quantity of insert
# https://mockaroo.com/ - site with random data
\i C:/Directory/file.sql #impor to table
SELECT * FROM table_name #show table with data
SELECT first_name FROM table_name #show all first_name
SELECT first_name, last_name FROM table_name
SELECT FROM table_name #show quanitity rows
SELECT * FROM table_name ORDER BY country_of_birth ASC #sort by country_ по возрастанию
SELECT * FROM table_name ORDER BY country_of_birth DESC #sort by в обратном порядке
SELECT DISTINCT country_of_birth FROM table_name ORDER BY country_of_birth #sort without repeat
SELECT * FROM table_name WHERE gender = 'Female' #show only Femele
SELECT * FROM table_name WHERE gender = 'Female' and country_of_birth = 'Argentina'
SELECT * FROM table_name WHERE gender = 'Female' and (country_of_birth = 'Argentina' or country_of_birth = 'Poland')
SELECT * FROM table_name WHERE country_of_birth IN ('China', 'Argentina') #IN same as '(... or ...)'
SELECT * FROM table_name WHERE date_of_bitrh BETWEEN '2019-01-01' and '2020-01-01' #BETWEEN - show промежуток
SELECT * FROM table_name WHERE email LIKE '%.com' # LIKE sorteb by part of string
SELECT * FROM table_name WHERE email iLIKE '%.com' #iLIKE is ignoring case 
SELECT country_of_birth, COUNT(*) FROM table_name GROUP BY country_of_birth #COUNT is show quanitity, GROUP BY is group
SELECT country_of_birth, COUNT(*) FROM table_name GROUP BY country_of_birth HAVING COUNT(*) > 10 #HAVING is sorted who have somethink
SELECT country_of_birth, COUNT(*) FROM table_name GROUP BY country_of_birth HAVING COUNT(*) > 10 ORDER BY DESC #sort by в обратном порядке
SELECT id, first_name AS name, last_name AS surname, gender AS sex, imail, date_of_birth, country_of_birth FROM table_name #AS - alias
SELECT COALESCE(email, 'not applicable') FROM table_name #COALESCE is change nul value to somethink
SELECT * FROM table_name LIMIT 20 #show only 20 first rows
SELECT * FROM table_name OFFSER 5 LIMIT 20 #show only 20 first rows from 5-th rows
SELECT * FROM table_name OFFSER 5 FETCH FIRST 20 ROW ONLY #same as
create table holiday (id BIGSERIAL NOT NULL PRIMARY KEY, destination_country VARCHAR(100) NOT NULL, destination_city VARCHAR(100) NOT NULL,	price NUMERIC(19, 2) NOT NULL); # 19, 2 - колличыество цифр до и после запятой
SELECT MAX(price) FROM holiday # show MAX
SELECT MIN(price) FROM holiday # show MIN
SELECT AVG(price) FROM holiday # show averege
SELECT ROUND(AVG(price)) FROM holiday #ROUND - округление до целого, не отбрасывание
SELECT destination_country, destination_city, MAX(price) FROM holiday GROUP BY destination_country, destination_city
SELECT SUM(price) FROM holiday # SUM is summa
SELECT destination_country, SUM(price) FROM holiday GROUP BY destination_country
SELECT 100+2 #show 102 (+, -, /, *, ^, %, !)
SELECT NOW() #show current time
SELECT NOW()::DATE #show current time only DATE
SELECT NOW()::TIME #show current time only TIME
SELECT NOW() - INTERVAL '1 YEAR' ##show current time minus 1 year
SELECT NOW() - INTERVAL '10 MONTHs'
SELECT NOW() - INTERVAL '10 DAYS'
SELECT EXTRACT(YEAR FROM NOW()) # show only DATA
SELECT EXTRACT(DOW FROM NOW()) # show Day Of the Week, starts of sundey
SELECT fist_name, last_name, gender, country_of_birth, date_of_birth, AGE(NOW(), date_of_birth) as age FROM employee #show age 
ALTER TABLE table_name DROP CONSTRAINT table_name_pkey #delete primary key
ALTER TABLE table_name ADD PRIMARY KEY(id) #add primary key
DELETE FROM table_name WHERE id = 1 #delete all line with 'id = 1'
SELECT email, count(*) FROM table_name GROUP BY email HAVING COUNT(*) > 1; #show all email who repeat > 1
ALTER TABLE table_name ADD CONSTRAINT gender_constraint CHECK (gender = 'Male' or gender = 'Female') #add ограничение(CONSTRAINT) to add only female and mail
UPDATE table_name SET email = '123@123.rj', first_name = 'Joe' WHERE id = 3 # change email and first_name for line with id = 3, если не добавить WHERE обновиться для всеё таблицы
INSERT INTO table_name (id, first_name, last_name, gender, email, date_of_birth, country_of_birth) VALUES (3, 'John','Doe', 'Male', '123@123.ru', DATE '2019-12-10', 'Russia') # add new line
ON CONFLICT (id) DO NOTHING # don't show exception when happen conflict
ON CONFLICT (id) DO UPDATE SET email = EXCLUDED.email, first_name = EXCLUDED.first_name # when happen conflict id then udate only email and first_name
#Foreign Keys (Внешние ключи)
CREATE TABLE bicycle (
id BIGSERIAL NOT NULL PRIMARY KEY,
make VARCHAR(100) NOT NULL,
type VARCHAR(100) NOT NULL,
price NUMERIC(19, 2) NOT NULL)
ALTER TABLE table_name ADD bicycle_id BIGINT REFERENCES bicycle (id) #add столбец with link to other table (id)
ALTER TABLE table_name ADD UNIQUE(bicycle_id) # make поле unique
UPDATE table_name SET bicycle_id = 2 WHERE id = 4 # add link to other table
#INNER JOIN - show only common fields
SELECT * FROM table_name JOIN bicycle ON table_name.bicycle_id = bicycle.id # show joins tables, table_name_id - field (поле) in first table, bicycle.id - field of other table
SELECT table_name.first_name, bicycle.make, bicycle.type, bicycle.price FROM table_name JOIN bicycle ON employ # show joins tables with only needed field
#LEFT JOIN - show all fields
SELECT * FROM table_name LEFT JOIN bicycle ON bicycle.id = table_name.bicycle_id # show all fields in left table
SELECT * FROM table_name LEFT JOIN bicycle ON bicycle.id = table_name.bicycle_id WHERE bicycle_id IS NOT NULL # show only NOT NULL
#RIGHT JOIN
SELECT * FROM table_name RIGHT JOIN bicycle ON bicycle.id = table_name.bicycle_id # show all fields in right table
SELECT * FROM table_name FULL OUTER JOIN bicycle ON bicycle.id = table_name.bicycle_id # show all fields
#transfer
\copy (SELECT * FROM table_name LEFT JOIN bicycle ON bicycle.id = table_name.id WHERE bicycle_id IS NOT NULL) TO '/Users/Desktop/test' DELIMITER ',' CSV HEADER # convert to csv, DELIMITER - разделитель

SELECT * FROM pg_available_extensions; # show all extension which might install
CREATE EXTENSION IF NOT EXISTS "uuid-ossp" # IF NOT EXISTS - если не существует
\df #show command of extension
SELECT uuid_generate_v4(); # generate random uuid
CREATE TABLE passport ( passport_serial UUID NOT NULL PRIMARY KEY, issue_date DATE NOT NULL, expire DATE NOT NULL, country_of_issue VARCHAR(150) NOT NULL)
INSERT INTO passport (passport_serial, issue_date, expare_date, countru_of_issue) VALUES (uuid_generate_v4(), '2020_02_03', '2045_02_03', 'United_kindom') # table with uuid