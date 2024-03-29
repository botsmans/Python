'''Вспомним нашего приятеля с предыдущих уроков: класс Vector. 
Ваша задача создать класс Vector, который хранит в себе вектор целых чисел.  У класса Vector есть:
конструктор __init__, принимающий произвольное количество аргументов. Среди всех переданных аргументов необходимо оставить только целые числа и сохранить их в атрибут values в виде списка. Причем значения должны хранится в порядке неубывания; 
переопределить метод __str__ так, чтобы экземпляр класса Vector выводился следующим образом: 
"Вектор(<value1>, <value2>, <value3>, ...)", если вектор не пустой. При этом значения должны быть упорядочены по возрастанию;
"Пустой вектор", если наш вектор не хранит в себе значения
переопределить метод __add__ так, чтобы экземпляр класса Vector мог складываться
с целым числом, в результате должен получиться новый Vector, у которого каждый элемент атрибута values увеличен на число
с другим вектором такой же длины. В результате должен получиться новый Vector, состоящий из суммы элементов, расположенных на одинаковых местах. Если длины векторов различаются, выведите сообщение "Сложение векторов разной длины недопустимо";
В случае, если вектор складывается с другим типом(не числом и не вектором), нужны вывести сообщение "Вектор нельзя сложить с <значением>"
переопределить метод __mul__ так, чтобы экземпляр класса Vector мог умножаться
на целое число. В результате должен получиться новый Vector, у которого каждый элемент атрибута values умножен на переданное число;
на другой вектор такой же длины. В результате должен получиться новый Vector, состоящий из произведения элементов, расположенных на одинаковых местах. Если длины векторов различаются, выведите сообщение "Умножение векторов разной длины недопустимо";
В случае, если вектор умножается с другим типом(не числом и не вектором), нужны вывести сообщение "Вектор нельзя умножать с <значением>";
v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"'''
class Vector:
    def __init__(self, *args):
        self.values = []
        for i in args:
            if isinstance(i, int):
                self.values.append(i)
        self.values.sort()
    def __str__(self):
        if self.values:
            self.str_value = 'Вектор(' + str(self.values[0])
            for i in range(1, len(self.values)):
                self.str_value = self.str_value + ', ' + str(self.values[i])
            self.str_value += ')'
            return self.str_value
        else: return 'Пустой вектор'
    def __add__(self, other):
        if isinstance(other, (int, float)):
            self.new_values = []
            for i in range(len(self.values)):
                self.new_values.append(other + self.values[i])
            return Vector(*self.new_values)
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                self.new_values = []
                for i in range(len(self.values)):
                    self.new_values.append(self.values[i] + other.values[i])
                return Vector(*self.new_values)
            else: print('Сложение векторов разной длины недопустимо')
        else: print(f'Вектор нельзя сложить с {other}')
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            self.new_values = []
            for i in range(len(self.values)):
                self.new_values.append(other * self.values[i])
            return Vector(*self.new_values)
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                self.new_values = []
                for i in range(len(self.values)):
                    self.new_values.append(self.values[i] * other.values[i])
                return Vector(*self.new_values)
            else: print('Умножение векторов разной длины недопустимо')
        else: print(f'Вектор нельзя умножать с {other}')
v1 = Vector(1,2,3)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4) # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
v5 + 'hi' # печатает "Вектор нельзя сложить с hi"
v5 * 'hi'
v6 = v5 * v1
print(v6)
