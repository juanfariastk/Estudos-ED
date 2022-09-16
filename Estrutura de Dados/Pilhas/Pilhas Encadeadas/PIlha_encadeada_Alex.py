from argparse import _AppendConstAction


class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class No_Pilha:
    def __init__(self, dado):
        self._proximo= None
        self._dado = dado

class Pilha:
    def __init__(self):
        self._topo = None
        self._tamanho=0
    
    def pilha_vazia(self):
        return len(self)==0
    
    def __len__(self):
        return self._tamanho
    
    def empilhar(self, dado):
        novo_no = No_Pilha(dado)
        novo_no._proximo = self._topo
        self._topo = novo_no
        self._tamanho+=1
    
    def desempilhar(self):
        self._topo = self._topo._proximo
        self._tamanho-=1
    
    def elemento_topo(self):
        topo = self._topo._dado
        return f' o elemento do topo é {topo}'
    
    def buscar_item(self, item):
        apontador = self._topo
        contador=0
        while(apontador):
            if apontador._dado==item:
                return f'{item} foi encontrado na posição {self._tamanho-contador}'
            apontador=apontador._proximo
    '''
    def modificar_item(self, item, novo_item):
        apontador = self._topo
        while(apontador):
            if apontador._dado == item:
                apontador._dado = novo_item
                return f' {item} foi modificado para {novo_item}'
            apontador = apontador._proximo
    '''
    def modificar_item(self, posicao, novo_item):
        apontador = self._topo
        cont = self._tamanho
        try:
            assert posicao>0 and posicao<=self._tamanho
            while (apontador):
                if cont == posicao:
                    apontador._dado = novo_item
                    return f'A posição {posicao} teve seu item alterado!'

                apontador = apontador._proximo
                cont-=1

        except AssertionError:
            raise PilhaException(f'Posição inválida! ')
    
    def __str__(self):
        dados = ''
        aponta = self._topo
        while(aponta):
            dados+=str(aponta._dado) + ' '
            aponta = aponta._proximo
        return dados
    


        
        
    
if __name__=='__main__':
    nova_pilha = Pilha()

    nova_pilha.empilhar(5)
    nova_pilha.empilhar(4)
    nova_pilha.empilhar(3)
    nova_pilha.empilhar(2)
    nova_pilha.empilhar(1)

    print(nova_pilha)

    print(nova_pilha.buscar_item(1))
    #print(nova_pilha.modificar_item(4, 10))

    #nova_pilha.modificar_item(1,13)
    #nova_pilha.modificar_item(2,12)
    #nova_pilha.modificar_item(3,11)
    #nova_pilha.modificar_item(5,9)
    print(nova_pilha.modificar_item(5,10))
    print(nova_pilha.modificar_item(4,11))
    print(nova_pilha.modificar_item(3,12))
    print(nova_pilha.modificar_item(2,11))
    print(nova_pilha.modificar_item(1,10))

    print(nova_pilha)

   