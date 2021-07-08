# Кортеджи

def sort_pair(cortej):
    a = cortej[0]
    b = cortej[1]

    if a > b:
        return (b, a)
    elif a < b:
        return (a, b)
    elif a == b:
        return (a, b)

print(sort_pair((1, 2)))