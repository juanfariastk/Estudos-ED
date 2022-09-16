class PilhaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Pilha:
    def __init__(self):
        self._dados=[]
    
    def verifica_vazia(self):
        return len(self._dados)==0
    
    def elemento_topo(self):
        if self.verifica_vazia():
            raise PilhaException('esta pilha não tem elementos!')
        return self._dados[0]
    
    def tamanho_pilha(self):
        return len(self._dados)
    
    def empilhar(self, item):
        self._dados.insert(0, item)
    
    def desempilha(self):
        self._dados.pop(0)
    
    def inverte_pilha(self):
        if self.verifica_vazia():
            raise PilhaException('esta pilha não tem elementos para inverter!')
        self._dados.reverse()
    
    def limpar_pilha(self):
        self._dados.clear()
        
    def __str__(self) -> str:
        dados= ''
        for i in self._dados:
            dados+=f'{i} '
        return dados

   

if __name__=='__main__':
    pilha_nova = Pilha()

    try:
        
        for i in range(1,10):
            pilha_nova.empilhar(i+2)
        print(pilha_nova)
        
        
    except PilhaException as pe:
        print(pe)

        