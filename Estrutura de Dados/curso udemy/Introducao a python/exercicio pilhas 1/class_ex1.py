
#criando a pilha
from xml.etree.ElementTree import PI


class PilhaException(Exception):
    def __init__(self,msg):
        super().__init__(msg)
class Pilha:
    def __init__(self):
        self.__dados=[]
    
    def esta_vazia(self):
        return len(self)==0
    
    def tamanho_pilha(self):
        return len(self)
    
    def empilhar(self,item):
        self.__dados.insert(0,item)
    
    def desempilhar(self):
        if self.esta_vazia():
            raise PilhaException('pilha não tem itens para desempilhar')
        self.__dados.pop(0)
    
    def topo_pilha(self):
        if self.esta_vazia():
            raise PilhaException('Pilha está vazia!')
    
    def __len__(self):
        return len(self.__dados)
    
    def __str__(self):
        dados =''
        for i in self.__dados:
            dados+=f'{i} '
        return dados
    

#pilha1= Pilha()
#print(pilha1.esta_vazia())
