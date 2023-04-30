'''
На складе лежат разные фрукты в разном количестве.
Нужно написать функцию на Python, которая на вход принимает любое количество
названий фруктов и их количество,
а возвращает общее количество фруктов на складе
'''


def count_fruits(**fruits):
    total = 0
    for fruit, quantity in fruits.items():
        total += quantity
    return total
print(count_fruits(apples=10, bananas=5, oranges=15))