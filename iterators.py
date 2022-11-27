import time

class FiboIter():

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self # Retorna al objeto en si mismo

    def __next__(self):
        if self.counter == 0:
            self.counter+= 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            self.aux = self.n1 + self.n2
            # self.n1 = self.n2
            # self.n2 = self.aux
            self.n1, self.n2 = self.n2, self.aux # Es lo mismo de arriba pero de forma resumida, se hace un swapping
            self.counter += 1
            return self.aux


if __name__ == '__main__':
    # Se instancia la clase
    # Instanciar es el acto de convertir a partir de los planos de una clase a un objeto
    fibonacci = FiboIter()
    for element in fibonacci:
        print(element)
        time.sleep(0.05)