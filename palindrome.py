def main():
    print(is_palindrome(1000))


def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower() # Borrando espacios y poniendo todo en minusculas
    return string == string[::-1] # Se revisa si el slice es igual al slice en reversa, con el [::-1] se le da 'vuelta' al iterable


if __name__ == '__main__':
    main()