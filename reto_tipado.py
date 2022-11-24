def main():
    x = is_prime(104729)
    if x:
        print("Es primo")
    else: 
        print("No es primo")


def is_prime(numero: int) -> bool:
    counter: int = 0
    for num in range(1, numero + 1):
        if numero % num == 0:
            counter += 1
    if counter > 2:
        return False
    else: 
        return True

if __name__ == '__main__':
    main()