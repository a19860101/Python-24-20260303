
# 遞迴

def foo(n):
    if n == 1:
        return 1
    else:
        return n * foo(n-1)

# foo(0) 0
# foo(1) 1
# foo(2) 2*1
# foo(3) 3*(2*1)
# foo(4) 4*(3*(2*1))


# 0 1 2 3 4 5 6 7  8  9  10
# 0 1 1 2 3 5 8 13 21 34 55

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# fib(9) = fib(8) + fib(7)
# fib(8) = fib(7) + fib(6)
# fib(7) = fib(6) + fib(5)
# fib(6) = fib(5) + fib(4)
# fib(5) = fib(4) + fib(3)
# fib(4) = fib(3) + fib(2)
# fib(3) = fib(2) + fib(1)

print(fib(35))