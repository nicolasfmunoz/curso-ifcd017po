class Calculadora(object):

    def __init__(self, operando_1, operando_2) -> None:
        self.operando_1 = operando_1
        self.operando_2 = operando_2
        self.result = 0

    def __str__(self) -> str:
        return f'''
Operando 1 = {self.operando_1}
Operando 2 = {self.operando_2}
        '''

    def sumar(self):
        self.result = self.operando_1 + self.operando_2
        return self.result

    def restar(self):
        self.result = self.operando_1 - self.operando_2
        return self.result

    def dividir(self):
        self.result = self.operando_1 / self.operando_2
        return self.result

    def multiplicar(self):
        self.result = self.operando_1 * self.operando_2
        return self.result

class CalculadoraCientifica(Calculadora):
    def __init__(self, operando_1, operando_2) -> None:
        super().__init__(operando_1, operando_2)

