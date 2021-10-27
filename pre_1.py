# my code:

# x = 0
# while x < 100:
#     x += 1

#     if x % 3 == 0 and x % 15 != 0:
#         print('fizz')

#     elif x % 5 == 0 and x % 15 != 0:
#         print("buzz")
#     elif x % 15 == 0:
#         print('fizzbuzz')
#     else:
#         print(x)

# Mr Grochowski's code:


def fizzbuzz(N):
    if N <= 0:
        return
    fizzbuzz(N-1)
    if N % 15 == 0:
        print("fizzbuzz")
    elif N % 3 == 0:
        print("fizz")
    elif N % 5 == 0:
        print("buzz")
    else:
        print(str(N))


print(fizzbuzz(100))
