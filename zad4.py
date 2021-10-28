def is_k_correct(k, size):
    if not k.isdigit():
        return False
    k = int(k)
    return k > 0 and k <= size

def kth(elemens):
    inupt_is_correct = False
    while not inupt_is_correct:
        k = input("Enter the number: ")
        inupt_is_correct = is_k_correct(k, len(elemens))
    return elemens[-int(k)]
    

print(kth([1, 2, 3, 4, 5, 6, 7, 8, 9]))