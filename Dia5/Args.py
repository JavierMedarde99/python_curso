def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(5,4,4))
