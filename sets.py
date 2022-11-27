# my_set1 = {3, 4, 5}
# my_set2 = {5, 6, 7}

# my_set3 = my_set1 | my_set2
# print(my_set3)


# Intersection
# my_set1 = {3, 4, 5}
# my_set2 = {5, 6, 7}

# my_set3 = my_set1 & my_set2
# print(my_set3)


# Difference
# my_set1 = {3, 4, 5}
# my_set2 = {5, 6, 7}

# my_set3 = my_set1 - my_set2
# print(my_set3)

# my_set4 = my_set2 - my_set1
# print(my_set4)


# Symetric difference
# my_set1 = {3, 4, 5}
# my_set2 = {5, 6, 7}

# my_set3 = my_set1 ^ my_set2
# print(my_set3)



# Reto
# futbol = {"Daniel", "Juan", "Ana"}
# basquet = {"Daniel", "Ana", "Oscar"}

# # Union
# todos = futbol | basquet
# print(todos)

# # Intersección
# ambos = futbol & basquet
# print(ambos)

# # Diferencia
# soloFutbol = futbol - basquet
# print(soloFutbol)

# # Simetrica
# unoUOtro = futbol ^ basquet
# print(unoUOtro)


# Eliminar duplicados
def removeDuplicates(some_list):
    withoutDuplicates = []

    for element in some_list:
        if element not in withoutDuplicates: # Si el elemento no está en la lista
            withoutDuplicates.append(element)

    return withoutDuplicates


# Otra forma más rápida
def removeDuplicates2(some_list):
    return list(set(some_list))


def run():
    random_list = [1, 1, 2, 4]
    print(removeDuplicates(random_list))
    print(removeDuplicates2(random_list))


if __name__ == '__main__':
    run()