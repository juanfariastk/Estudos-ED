class No:
    def __init__(self,dado):
        self.__dado = dado
        self.__esq = None
        self.__dir =  None
    
    @property
    def dado(self):
        return self.__dado
    @property
    def esq(self):
        return self.__esq
    @property
    def direita(self):
        return self.__dir
    
    @esq.setter
    def esq(self, novo):
        if self.__esq !=None:
            raise 'Referencia com dado válido presente!'
        self.__esq = novo
    
    def direita(self, novo):
        if self.__dir!=None:
            raise 'Referencia com dado válido presente!'
        self.__dir = novo
    
    @dado.setter
    def dado(self, novo_dado):
        self.__dado = novo_dado

if __name__ =='__main__':
    raiz_arv = No('A')
    raiz_arv.esq = No('B')
    raiz_arv.dir = No('C')
    raiz_arv.esq.esq=No('D')
    raiz_arv.esq.esq.dir= No('G')

    raiz_arv.dir.dir=No('F')
    raiz_arv.dir.esq=No('E')
    raiz_arv.dir.esq.esq =No('H')
    raiz_arv.dir.esq.dir=No('I')

    print(raiz_arv.dir.dado)
    def em_ordem(raiz):
        if raiz!=None:
            em_ordem(raiz.esq)
            print(raiz.dado, end='')
            em_ordem(raiz.dir)

    em_ordem(raiz_arv)
    

