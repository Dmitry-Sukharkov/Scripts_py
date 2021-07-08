def mathematical_series(variable1, variable2):
    i = variable1
    result = ''
    if variable1 < variable2:
        for i in range(variable1, variable2 + 1):
            result += str(i)
            i = i + 1
        return result
    elif variable1 > variable2:
        for i in range(variable1, variable2 - 1, -1):
            result += str(i)
            i -= 1
        return result

mathematical_series(3, -3)


# Сумма чисел из ручной ввод в консоли (input)
def sum_of_variables_input():
    result = 0
    for i in range(10):
        the_number = int(input())
        result += the_number
    return result
    

print(sum_of_variables_input())


# Сумма N чисел 

def sum_of_N_numbers():
    amount_of_numbers = int(input())
    result = 0
    
    for i in range(amount_of_numbers):
        the_number = int(input())
        result += the_number
    return result

print(sum_of_N_numbers())


#Сумма кубов

def sum_of_cubes():
    number = int(input())
    result = 0

    for i in range(1, number + 1):
        result += i ** 3
    return result

print(sum_of_cubes())


#Факториал

def factorial():
    number = int(input())
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

print(factorial())


#Сумма факториалов

def sum_of_factorials():
    variable = int(input())
    result_factorial = 1
    result_sum = 0

    for i in range(1, variable + 1):
        result_factorial *= i
        print(result_factorial)
        result_sum += result_factorial
        print(result_sum)
    return result_sum

print(sum_of_factorials())


#Количество нулей

def count_zeros():
    amount_of_numbers = int(input())
    result_count_zeros = 0

    for i in range(amount_of_numbers):
        the_number = int(input())
        if the_number == 0:
            result_count_zeros += 1
    return result_count_zeros

print('Итого: ' + str(count_zeros()))


#Лесенка ебучая

def stairs():
    number_of_steps = int(input())
    result = ''
    if 0 < number_of_steps < 10:
        for i in range(1, number_of_steps + 1):
            print(result)
            result += str(i)
        return result

    elif 0 >= number_of_steps >= 10:
        return print('Error: You are seriosly? No!')

print(stairs())