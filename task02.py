# 2. Для чисел в пределах от 20 до n найти числа,
#    кратные 20 или 21. Use comprehension.


count = int(input())
crt_list = [i for i in range(20, count + 1)]
print(crt_list)

def check_list(num):
    if num % 20 == 0 or num % 21 == 0:
        return True
    else:
        return False

print(list(filter(check_list, crt_list)))   
