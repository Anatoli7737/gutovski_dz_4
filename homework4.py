#Anatoli Gutovski
#Homework-4
#18.03.2024
#Grodno-IT-Academy-Python 3.11.7

# теперь тесты написаны с использованием библиотеки pytest
# нам нужно ее установить: pip install pytest
# и запустить как обычный файл: pytest test_Homework4.py
# Теперь вы будете знакомы со вторым инструментом для тестирования


#Выведите n-ое число Фибоначчи, используя только временные переменные, циклические операторы и условные операторы. n - вводится.

# Функция для вычисления n-го числа Фибоначчи
def fibonacci(n):
    if n == 1:
        # Возвращаем 0, если n равно 1
        return 0  
    elif n == 2:
        # Возвращаем 1, если n равно 2
        return 1
    # Инициализируем первое число Фибоначчи  
    fib1 = 0  
    # Инициализируем второе число Фибоначчи
    fib2 = 1  
    # Инициализируем переменную для хранения текущего числа Фибоначчи
    fib = 0   
    for i in range(0, n - 2):
        # Вычисляем следующее число Фибоначчи как сумму двух предыдущих
        fib = fib1 + fib2  
        # Обновляем первое число для следующей итерации
        fib1 = fib2     
        # Обновляем второе число для следующей итерации   
        fib2 = fib  
    # Возвращаем найденное число Фибоначчи       
    return fib  



#Определите, является ли число палиндромом (читается слева направо и справа налево одинаково). Число положительное целое, произвольной длины. Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще).


# Функция для определения, является ли число палиндромом
def palindrome(n):
    # Пропишем условие, отрицательные числа не могут быть палиндромами
    if n < 0:
        return False 
    # Создадим переменную reversed_n, которая будет использоваться для хранения перевернутого числа 
    reversed_n = 0
    # Создадим переменную origa_n, в которой сохраняется исходное значение числа n
    origa_n = n
    # Цикл while, который будет выполняться до тех пор, пока число n больше нуля
    while n > 0:
        # Здесь находим последнюю цифру числа n, вычисляя остаток от деления на 10
        digit = n % 10
        # Эта строка обновляет переменную reversed_n, умножая ее на 10 и добавляя к ней найденную цифру digit.
        reversed_n = reversed_n * 10 + digit
        # Здесь обновляется значение числа n, удаляя последнюю цифру путем целочисленного деления на 10
        n = n // 10
    # Возвращаем True, если число является палиндромом
    if origa_n == reversed_n:  
        return True
    # Иначе, возвращаем False
    else:
        return False



#Напишите генератор, который возвращает цифры от S до N, но вместо чисел, кратных 3 пишет Fizz, вместо чисел кратный 5 пишет Buzz, а вместо чисел одновременно кратных и 3 и 5 - FizzBuzz.

def fizz_buzz(S, N):
    # Проверка условия, если S меньше N, то выполняется следующий блок кода
    if S < N:
        for i in range(S, N+1):
            # Проверка, если число делится и на 3, и на 5 без остатка
            if i % 3 == 0 and i % 5 == 0:
                # Возврат строки "FizzBuzz" через генератор
                yield "FizzBuzz"
            # Если число делится на 3 без остатка
            elif i % 3 == 0:
                yield "Fizz"
            # Если число делится на 5 без остатка
            elif i % 5 == 0:
                yield "Buzz"
            # Если число не делится ни на 3, ни на 5 без остатка
            else:
                # Возврат числа в виде строки через генератор
                yield str(i)
    # Проверка условия, если S больше N, то выполняется следующий блок кода
    if S > N:
        # Обмен значений переменных S и N
        S, N = N, S
        for i in range(N, S-1, -1):
            # Проверка, если число делится и на 3, и на 5 без остатка
            if i % 3 == 0 and i % 5 == 0:
                # Возврат строки "FizzBuzz" через генератор
                yield "FizzBuzz"
            # Если число делится на 3 без остатка
            elif i % 3 == 0:
                yield "Fizz"
            # Если число делится на 5 без остатка
            elif i % 5 == 0:
                yield "Buzz"
            # Если число не делится ни на 3, ни на 5 без остатка
            else:
                # Возврат числа в виде строки через генератор
                yield str(i)
