# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь,
#    ключи — первые буквы имён, значения — списки, содержащие имена,
#    начинающиеся с соответствующей буквы.

def create_dict(*arg):
    name = {}
    for i in sorted(arg):
        letter = i[0]
        if letter not in name: 
            name[letter] = [i]
    name[letter] += [i]   
    return name     


print(create_dict("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"))