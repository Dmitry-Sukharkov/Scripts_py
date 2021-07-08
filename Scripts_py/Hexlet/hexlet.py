def binary (number):
    modulo = ''
    result = 0
    if number == 0:
        modulo = '0'
        return modulo
    elif number < 0:
        return 'Вы серьёзно? Нет.'
    else:
        while number > 0:
            result = number % 2
            modulo += str(result)
            number = number // 2
        return modulo[::-1]
    

print(binary(-1111))
