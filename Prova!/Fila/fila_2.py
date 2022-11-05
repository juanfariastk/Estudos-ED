
class FilaExcept(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class NoC:
    def __init__(self):
        self.inicio=None
        self.final=None
        self.tamanho=0

class No:
    def __init__(self,item):
        self.item = item
        self.proximo=None

class Fila:
    def __init__(self):
        self._cabeca = NoC() 
    
    def __len__(self):
        return self._cabeca.tamanho
    
    def tamanho_fila(self):
        return self._cabeca.tamanho
    
    def fila_vazia(self):
        return self._cabeca.tamanho==0
    
    def enfileirar(self, dado):
        novo_no=No(dado)
        
        if self.fila_vazia():
            self._cabeca.inicio=novo_no
            self._cabeca.final = novo_no
        else:
            self._cabeca.final.proximo = novo_no
            self._cabeca.final= novo_no
        self._cabeca.tamanho+=1
    
    def desenfileirar(self):
        dado = self._cabeca.inicio.item
        self._cabeca.inicio = self._cabeca.inicio.proximo
        self._cabeca.tamanho-=1
        return dado
    
    def elemento(self, pos):
        apontador = self._cabeca.inicio
        cont=1
        while(cont!=pos):
            apontador=apontador.proximo
            cont+=1
        return apontador.item
    
    def busca(self, item):
        apontador = self._cabeca.inicio
        contador=1
        while(apontador):
            if apontador.item ==item:
                return contador
            apontador= apontador.proximo
            contador+=1
    
    def concatenar(self, fila2:object):
        while(not fila2.fila_vazia()):
            self.enfileirar(fila2.desenfileirar())

    @classmethod
    def concatenar_alternado(cls,fila1:object, fila2:object, fila3:object):
        tamanho_filas = fila2.tamanho_fila()+fila3.tamanho_fila()
        aux1=Fila()
        aux2=Fila()

        while(not fila2.fila_vazia()):
            aux1.enfileirar(fila2.desenfileirar())
        while(not fila3.fila_vazia()):
            aux2.enfileirar(fila3.desenfileirar())

        cont=0

        for i in range(tamanho_filas):
            if cont%2==0:
                fila1.enfileirar(aux1.desenfileirar())
            else:
                fila1.enfileirar(aux2.desenfileirar())
            cont+=1

        return True
    
    
    def __str__(self):
        dados=''
        apontador = self._cabeca.inicio
        while(apontador):
            dados+=str(apontador.item)+ ' -> '
            apontador= apontador.proximo
        return dados
    
    def esvaziar(self):
        self._cabeca.inicio=None
        self._cabeca.final = None
        self._cabeca.tamanho = 0
    
if __name__=='__main__':
    fila = Fila()
    fila2 = Fila()
    fila3=Fila()
    for i in range(1,12):
        fila.enfileirar(i)
        fila2.enfileirar(i+1)
        fila3.enfileirar(i+3)
    print(fila)
    for i in range(1,4):
        print(fila.desenfileirar())
    print(fila)

    print(fila2)

   
    
    Fila.concatenar_alternado(fila3, fila2,fila)
    print(fila3)

            

    
    