
#criando uma classe motor

class Motor:

    #construtor
    def __init__(self, motorizacao, combustivel ='flex'):
        self._motorizacao = motorizacao
        self._combustivel = combustivel
    
    #get(acesso)
    @property
    def motorizacao(self):
        return self._motorizacao
    
    @property
    def combustivel(self):
        return self._combustivel
    
    #set(atribuição de valores aos atributos)

    @motorizacao.setter
    def motorizacao(self, mot_nov):
        self._motorizacao = mot_nov

    @combustivel.setter
    def combustivel(self, comb_nov):
        self._motorizacao = comb_nov

    #retorno dos valores
    def __str__(self):
        return f'motor {self._motorizacao}L, tendo combustivel {self._combustivel}'
    
#mot1 = Motor(2.0)

#print(mot1)