# Hola 3 -> HolaHolaHola
# Oscar 2 -> OscarOscar
# Platzi 4 -> PlatziPlatziPlatziPlatzi

def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Solo puedes utilizar cadenas"
        return string * n
    return repeater


# Ejercicio
def make_division_by(n):
    def division(x):
        assert (type(x) == int or type(x) == float) and x != 0, "Solo puedes mandar numeros mayores a 0"
        return x / n
    return division



def run():
    # repeat_5 = make_repeater_of(5)
    # print(repeat_5("Buenas"))

    # repeat_10 = make_repeater_of(10)
    # print(repeat_10("xd"))
    div_5 = make_division_by(5)
    print(div_5(0))
    



if __name__ == '__main__':
    run()