from datetime import datetime

def execution_time(func):
    def wrapper():
        initial_time = datetime.now() # Devuelve fecha y hora del momento que se ejecuta
        func()
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos') # Se obtienen la cantidad de segundos con el método total_seconds() 
    return wrapper

# Aquí se procede a decorar
@execution_time
def random_func():
    for _ in range(1,1000000):
        pass

random_func()