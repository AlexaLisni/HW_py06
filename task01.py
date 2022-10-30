# 1. Представлен список чисел. Необходимо вывести элементы
#    исходного списка, значения которых больше предыдущего элемента.
#    Use comprehension.

from random import sample
from random import randint

def new_list(num):
    my_list = sample(range(num * 3), num)
    print(my_list)
    return [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]

def check_list(num):
    my_list = [randint(0, 1000) for _ in range(num)]
    print(my_list)
    return [num for i, num in enumerate(my_list[1:]) if num > my_list[i]]


print(new_list(int(input())))
print(check_list(int(input())))