#Napisz funkcję, która dla zadanej listy elementów pobierze od użytkownika liczbę k i zwróci k-ty element od końca listy. 
#Uwaga: załóż, że użytkownik podaje poprawne wartości (tzn. 0 < k <= długość listy).


def kth(n):
    k = int(input("Enter the number: "))
    elemens = list(range(1, n+1))
    return elemens[-k]

print(kth(10))


