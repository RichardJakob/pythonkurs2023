import random

def terning(kast):
    resultat_array = []
    for i in range(0, kast):
        resultat_array.append(random.randrange(1,7))
    print("antall prosent som er 6: ", (resultat_array.count(6) / kast) * 100)
    return resultat_array

print(kast(10))
print(kast(100))
print(kast(1000))

