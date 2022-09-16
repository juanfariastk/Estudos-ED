#definindo a mensagem das exceções 
class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Pilha:
    def __init__(self) -> None:
        self._dados = []
    
    
    def verifica_pilha(self):
        return len(self._dados)==0

    def tamanho_pilha(self):
        return len(self._dados)
    
    def escolhe_elemento(self, posicao):
        try:
            self._dados[posicao-1]
        except IndexError:
            raise PilhaException(f'houve um erro ao acessar o elemento da posição {posicao}, a pilha tem o tamanho {len(self._dados)}, tente outra posição')
    
    def busca_elemento(self, elemento):
        for i in range(len(self._dados)):
            if self._dados[i] == elemento:
                return self._dados[i]
        raise PilhaException(f' o valor {elemento} não está na pilha!')

    def modifica_elemento(self, posicao, elemento):
        try:
            self._dados[posicao-1] = elemento
        except IndexError:
            raise PilhaException(f' a posição {posicao} não é valida!')

    def insere_dado(self, dado):
        self._dados.append(dado)
    
    def remove_dado(self):
        if self.verifica_pilha():
            raise PilhaException('a pilha está vazia!')
        self._dados.pop()
    
    def remover_tudo(self):
        self._dados.clear()
    
    def __str__(self):
        dados = ''
        for i in self._dados:
            dados+=f' {i}'
        return dados

if __name__=='__main__':
    pilha_sequencial = Pilha()
    try:
        for i in range(1,9):
            pilha_sequencial.insere_dado(i)
        
        print(pilha_sequencial)
        pilha_sequencial.insere_dado(10)
        print(pilha_sequencial)
        pilha_sequencial.modifica_elemento(3, 4)
        print(pilha_sequencial)
        print(pilha_sequencial.busca_elemento(10))
        pilha_sequencial.remover_tudo()
        print(pilha_sequencial)
        print('final')
    except PilhaException as pE:
        print(pE)

    

 