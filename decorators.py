from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs): 
        initial_time = datetime.now() # Devuelve fecha y hora del momento que se ejecuta
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos') # Se obtienen la cantidad de segundos con el método total_seconds() 
    return wrapper

# Aquí se procede a decorar
@execution_time
def random_func():
    for _ in range(1,100000):
        pass


@execution_time
def suma(a: int, b: int) -> int: 
    return a + b


@execution_time
def saludo(nombre="Oscar"):
    print(f"Hola {nombre}")


random_func()
suma(5,5)
saludo("Daniel")


# Reto

def saludo(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("Hola, estoy colando este mensaje y estoy decorando")
    return wrapper

@saludo
def llamadaNombre(name="Anonimo"):
    print(f"Hola {name}, espero que no se cole el mensaje del decorador")

llamadaNombre("Jose")
print("Ay no, si se coló")