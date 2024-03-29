class multifilter:
    def judge_half(pos, neg):
        if pos >= neg: return True
        else: False
        #return pos >= neg #сокращеная форма

        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)

    def judge_any(pos, neg):
        if pos >= 1: return True
        else: return False
        #return pos > 0 #сокращеная форма
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)

    def judge_all(pos, neg):
        if neg == 0: return True
        else: False
        #return neg == 0 #сокращеная форма
        # допускает элемент, если его допускают все функции (neg == 0)

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        # iterable - исходная последовательность
        # funcs - допускающие функции
        # judge - решающая функция
    def __iter__(self):
        for i in self.iterable:
            self.pos = 0
            self.neg = 0
            for j in self.funcs:
                if j(i): self.pos += 1
                else: self.neg += 1
            if self.judge(self.pos, self.neg):
                yield i
            else: continue
        # возвращает итератор по результирующей последовательности

    # решение with iterator
    # def __init__(self, iterable, *funcs, judge=judge_any):
    #     self.iterator = iter(iterable)
    #     self.funcs = funcs
    #     self.judge = judge

    # def __iter__(self):
    #     return self

    # def __next__(self):
    #     while (True):
    #         elem = next(self.iterator)
    #         pos, neg = 0, 0
    #         for func in self.funcs:
    #             if func(elem):
    #                 pos += 1
    #             else:
    #                 neg += 1

    #         if self.judge(pos, neg):
    #             return elem


    
        



# проверка        
def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5))) 
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half))) 
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all))) 
# [0, 30]