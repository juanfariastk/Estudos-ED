
#criando pilha...

class Pilha:
    def __init__(self):
        self.itens = [] #inicialmente vazio
    
    
    #criando a função push (método que adiciona item ao final da pilha)
    def push(self, item):
        self.itens.append(item)
    
    #criando função size (retorna o tamanho da pilha)
    def size(self):
        return len(self.itens)

    #criando função pop (metodo que remove e retorna este valor)
    def pop(self):
        #primeiro verificar se não está com a pilha vazia
        if self.size()==0:
            return None
        else:
            return self.itens.pop()
    
    #função de retorno da pilha para testes
    def __str__(self):
        return f'{self.itens}'


#instânciando a nossa pilha

nova_pilha = Pilha()

nova_pilha.push('item1')
nova_pilha.push('item2')
#ultimo a entrar
nova_pilha.push('item3')

print(nova_pilha.size())
print(nova_pilha)
#primeiro a sair será 'item3' 
nova_pilha.pop()

print(nova_pilha)