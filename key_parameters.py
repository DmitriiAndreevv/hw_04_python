# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
#   где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
#   используйте его строковое представление.

def func_key(**kwargs):
    temp_dict = {}
    temp_dict = kwargs
    print(temp_dict)
    res = {}
    for i in range(len(temp_dict)):
        for item, value in temp_dict.items():
            if hash(value):
                value
            else:
                value = ','.join(value)

            res[value] = item
    print(res)

print(func_key(arg1 = "Helloo", arg2 = 2, arg3 = "123", arg4 = True))
