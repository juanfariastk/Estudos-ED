from typing import List


class ListaExcept(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class No:
    def __init__(self,dado) :
        self.__item=dado
        self.__proximo=None
    
    @property
    def item(self):
        return self.__item
    
    @property
    def proximo(self):
        return self.__proximo
    
    @item.setter
    def item(self,novo):
        self.__item=novo
    
    @proximo.setter
    def proximo(self,novo):
        self.__proximo=novo
    
    def __str__(self):
        return str(self.__item)


class lista_simplesmente_encadeada:
    def __init__(self):
        self.__cabeca = None
        self.__tamanho=0
    
    def vazia(self):
        return self.__tamanho==0

    def __len__(self):
        return self.__tamanho
    
    def tamanho(self):
        return len(self)
    
    def inserir(self, posicao, item):
        try:
            assert posicao>0
            if self.vazia():
                if (posicao!=1):
                    raise ListaExcept('Adicione primeiro na posição 1')
                self.__cabeca=No(item)
                self.__tamanho+=1
                return
            
            if (posicao==1):
                novo = No(item)
                novo.proximo=self.__cabeca
                self.__cabeca=novo
                self.__tamanho+=1
                
            
            apontador = self.__cabeca
            cont=1
            while(apontador!=None and cont<posicao-1):
                apontador=apontador.proximo
                cont+=1

            if (apontador!=None):
                raise ListaExcept('Posição inválida')

            novo=No(item)
            novo.proximo=apontador.proximo
            apontador.proximo=novo
            self.__tamanho+=1

        except AssertionError:
            raise ListaExcept('Escolha posições positivas')
        except:
            raise
try:
    lista = lista_simplesmente_encadeada()
    lista.inserir(1,10)
    lista.inserir(3,10)
except ListaExcept as le:
    print(le)
        

