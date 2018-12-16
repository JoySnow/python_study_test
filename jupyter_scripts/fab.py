#def fibonacci(n):
#    i, a, b = 0, 0, 1
#    while i < n:
#        yield b
#        a, b = b, a + b
#        i += 1


def fibonacci(n):
    fib_list = [0, 1]
    if n <= 0:
        return []
    elif n == 1:
        return fib_list

    i = 2
    while i <= n:
        fib_list.append(fib_list[i-1]+fib_list[i-2])
        i += 1
    return fib_list

print fibonacci(11)
