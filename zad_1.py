def fuzz(n):
    elems = list(range(1, n+1))
    elems[2::3] = ['fuzz'] * (n // 3)           # -> w tym wypadku, aby pomnożyć stringa musisz wziąć go jako lista
    return elems


print(fuzz(20))

# my_list = [1, 2, 3, 4, 5, 6]
# my_list[2:5] = '*'  -> musisz pomnożyć przez tyle ile chcesz zastąpień
# print(my_list) # rezultat:
