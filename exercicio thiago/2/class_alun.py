
#criando classe

class Aluno:
    #construtor
    def __init__(self, mat, nome, notas:int):
        self._mat = mat
        self._nome = nome
        self._notas = list()
        self._notas.append(notas)

    #gets

    @property
    def mat(self):
        return self._mat

    @property
    def nome(self):
        return self._nome
    
    @property
    def notas(self):
        return self._notas
    
    #sets

    @nome.setter
    def nome(self, novo):
        self._nome = novo

    #metodos
    def adc_notas(self, nota) ->int:
        self._notas.append(nota)
    
    def media_notas(self):
        media = 0
        for i in range(len(self._notas)):
            media+=self._notas[i]
        
        media = media/len(self.notas)

        return f'{media:.2f}'

    def __str__(self):
        nota_fim =''
        for i in range(len(self._notas)):
            nota_fim+=f'{self._notas[i]} '
        return f'aluno {self._nome}, matricula {self._mat}, com notas:{nota_fim}'
    


