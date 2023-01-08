Задание1

# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

с = [1, 5, 2, 5, 6, 1, 7]
print(с)
sum = 0
for i in range(1, len(с), 2):
    if i % 2 == 1:
        sum += с[i]
print(f"{с} -> сумма элементов на нечётных позициях: {sum}")

Задание2

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint
number = int(input('Введите размер списка '))
list = []
list2 = []

for i in range(number):
    list.append(randint(0, 9))

for i in range(len(list)):
    while i < len(list)/2 and number > len(list)/2:
        number = number - 1
        a = list[i] * list[number]
        list2.append(a)
        i += 1

print(list)
print(list2)

Задание 3
# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
a = [1.1, 1.2, 3.1, 5.10, 10.01]
def MaxMin(list):
    for i in range(len(list)):
        list[i] = list[i] % 1
    Result = round(max(list) - min(list), 3)
    return f"Разница между остатком дробей {round(max(list),3)} и {round(min(list),3)} = {Result}"

print(MaxMin(a))

Задание 4
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
def ConvertToBinary (number):
    list = []
    while number != 1:
        list.insert(0, number % 2)
        number //=  2
    if number <= 1: list.insert(0, number)
    print(*list)

userNumber = int(input('Введите число: '))

ConvertToBinary(userNumber)

Задание 5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def Fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def NegaFibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

list = [0]
userNumber = int(input('Введите число: '))
for e in range(1, userNumber + 1):
    list.append(Fibonacci(e))
    list.insert(0, NegaFibonacci(e))
print(list)
