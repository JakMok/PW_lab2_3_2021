def fibb(n):
    if n < 0:
        return print("N must be > 0.")
    if n == 0:
        return 0
    if n == 1:
        return 1
        
    return fibb(n-1) + fibb(n-2)

print(fibb(5))

# def fibonacci(N):
#     if N <= 1:
#         return 1
#     return fibonacci(N-1) + fibonacci(N-2)
# print(fibonacci(0))