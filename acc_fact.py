def acc_fact(n):
    if n == 1:
        return [1]
    prev = acc_fact(n - 1)
    return prev + [prev[-1] * n]

print(acc_fact(10))
