#Rozbuduj funkcję z poprzedniego zadania tak, aby sprawdzała, czy liczba k podana przez użytkownika mieści się we 
#właściwym przedziale i w razie błędu wypisz na ekran stosowny komunikat. Pamiętaj o obsłużeniu sytuacji, 
#w której wartość podana przez użytkownika w ogóle nie jest liczbą całkowitą. Wskazówka: użyj funkcji isdigit().



def is_k_correct(k, size):
    if not k.isdigit():
        return False
    k = int(k)
    return k > 0 and k <= size

def kth(elemens):
    k = input("Enter the number: ")
    if not is_k_correct(k, len(elemens)):
        return
    return elemens[-int(k)]
    

print(kth([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# Mr Grochowski's code:
# def is_k_correct(k, size):
#     if not k.isdigit():
#         return False
#     k = int(k)
#     return k > 0 and k <= size


# def get_kth_elem(elems):
#     k = input("K: ")
#     if not is_k_correct(k, len(elems)):
#         return
#     return elems[-int(k)]


# print(get_kth_elem([1, 2, 3, 4, 5, 6, 7, 8]))
