class ListaSequencial:
    def __init__(self):
        self.__dados=[]

    def lista_vazia(self):
        return len(self.__dados)==0

    def __len__(self):
        return len(self.__dados)

    def inserir(self, posicao, dado):
        self.__dados.insert(posicao-1, dado)

    def remove(self, posicao):
        dado_removido =self.__dados[posicao-1]
        del self.__dados[posicao-1]
        return dado_removido

    def elemento(self, posicao):
        return self.__dados[posicao-1]

    def busca(self, dado):
        cont=1
        for i in self.__dados:
            if i==dado:
                return cont
            cont+=1
            
    def modificar(self, dado, dado_novo):
        for i in range(len(self)):
            if self.__dados[i]==dado:
                self.__dados[i]=dado_novo
            
                
    def modificar_posicao(self, posicao, dado_novo):
        self.__dados[posicao-1]=dado_novo
    
    
    def __str__(self):
        return self.__dados.__str__()



lista1= ListaSequencial()
for i in range(1,11):
    lista1.inserir(i,i+1)

print(lista1)
lista1.remove(3)
print(lista1)
lista1.modificar(2,1)
lista1.modificar_posicao(2,2)
print(lista1)
