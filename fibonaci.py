def fibonacci(n):
    # base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # recursive case
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# example usage
num = int(input("masukan bilangan"))
for i in range(num):
    print(fibonacci(i))
