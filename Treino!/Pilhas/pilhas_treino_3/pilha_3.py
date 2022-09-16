class PilhaExcept(Exception):
    def __init__(self, msg):
        super().__init__(msg)
    
class No:
    def __init__(self, item):
        self._proximo = None
        self._dado = item

class Pilha:
    def __init__(self):
        self._topo = None
        self._tamanho = 0

    def vazia(self):
        return len(self)==0
    
    def __len__(self):
        return self._tamanho
    
    def empilhar(self, item):
        no = No(item)
        no._proximo = self._topo
        self._topo = no
        self._tamanho+=1
    
    def desempilhar(self):
        self._topo = self._topo._proximo
        self._tamanho -=1
    
    def buscar(self, item):
        aponta = self._topo
        num = 0
        while(aponta):
            if aponta._dado == item:
                return f' o item {item} foi encontrado em {self._tamanho-num}'
            aponta = aponta._proximo
            num+=1
    
    def modificar_iguais(self, item, novo_item):
        aponta = self._topo
        while(aponta):
            if aponta._dado == item:
                aponta._dado = novo_item
            aponta = aponta._proximo
    
    def modificar_posicao(self, posicao, item):
        aponta = self._topo
        contador = self._tamanho
        while(aponta):
            if contador ==posicao:
                aponta._dado = item
            contador-=1
            aponta = aponta._proximo

    def __str__(self):
        dados=''
        aponta= self._topo
        while(aponta):
            dados+=str(aponta._dado)+' '
            aponta = aponta._proximo 
        return dados

    def esvaziar(self):
        self._topo = None
        self._tamanho = 0

if __name__=='__main__':
    pilha_nova = Pilha()
    pilha_nova.empilhar(1)
    print(pilha_nova)


        
        