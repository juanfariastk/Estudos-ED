
class Cartas:

    def __init__(self, tipo, valor, cor):
        self.tipo= tipo
        self.valor= valor
        self.cor = cor
    
    def retorno_naipe(self):
        return self.tipo
    def retorno_valor(self):
        return self.valor
    def retorno_cor(self):
        return self.cor
    
    def __str__(self):
        return f'{self.valor} de {self.tipo}'

   
    