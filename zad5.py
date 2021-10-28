def f(slowo):
    slownik = {}                    #tworze pusty slownik o nazwie slowniki potem moge dodawać elemnty do tego slownika
    for litera in slowo:
        if litera in slownik:       # litera - jeden znak w slownik
            slownik[litera] += 1    
        else:
            slownik[litera] = 1
    return slownik

# dla zainteresowanych defaultdict
#jak będziesz miał for i in range(1, n+1) to dla każdego elementu od 1 do n


print(f("kukułka"))


# def count_unique_letter(sentence):
#     dict = {}
#     for letter in set(sentence):
#         if not letter == ' ':
#             dict[letter] = sentence.count(letter)
#     return dict


# print(count_unique_letter("kukułka"))
