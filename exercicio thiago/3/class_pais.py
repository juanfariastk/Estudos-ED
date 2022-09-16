
#criando classe

class Pais:
    #construtor
    def __init__(self,nome:str, capital:str, dimensao:int,fronteira:str):
        self._nome = nome
        self._capital = capital
        self._dimensao = dimensao
        self._fronteira = list()
        self._fronteira.append(fronteira)
    
    #gets
    @property
    def nome(self):
        return self._nome
    
    @property
    def capital(self):
        return self._capital
    
    @property
    def dimensao(self):
        return self._dimensao
    
    @property
    def fronteira(self):
        front = ''
        for i in range(len(self._fronteira)):
            front+=f'{self._fronteira[i]} '
        return front
    
    #metodos
    def adiciona_fronteira(self, front_nov):
        if front_nov not in self._fronteira:
            self._fronteira.append(front_nov)
            return 'adicionado com sucesso!'
    
        else:
            return 'já foi adicionado'
    #fim
    def __str__(self):
        fronteira_fim =''
        for i in range(len(self._fronteira)):
            fronteira_fim+=f'{self._fronteira[i]}, '
        return f'o País {self._nome} tem dimensão {self._dimensao} e faz fronteira com {fronteira_fim}.' 
