
#criando classe data


class Data:
    #criando construtor
    def __init__(self, dia:int, mes:int, ano:int):
        self._dia = dia
        self._mes = mes
        self._ano = ano
    
    #get
    @property
    def dia(self):
        return self._dia
    
    @property
    def mes(self):
        return self._mes
    
    @property
    def ano(self):
        return self._ano
    

    #sets

    @dia.setter
    def dia(self, novo):
        self._dia = novo
    
    @mes.setter
    def mes(self, novo):
        self._mes = novo
    
    @ano.setter
    def ano(self, novo):
        self._ano = novo
    
    def __str__(self):
        return f'a data definida é {self._dia}/{self._mes}/{self._ano}'
    


        