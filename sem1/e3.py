'''Дан список с затратами на рекламу. Но в данных есть ошибки, 
некоторые затраты имеют отрицательную величину. 
Удалите такие значения из списка и посчитайте суммарные затраты
[100, 125, -90, 345, 655, -1, 0, 200]
Используйте list comprehensions'''

expenses = [100, 125, -90, 345, 655, -1, 0, 200]
expenses = [expense for expense in expenses if expense >= 0]
total_expenses = sum(expenses)
print(total_expenses)
