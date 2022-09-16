from pilha_1 import *

class Banco_pilha:
    def __init__(self):
        self.__pilhas=[] #programa inicia sem pilha nenhuma!
    
    def banco_vazio(self):
        return len(self.__pilhas)==0

    def pilha_vazia(self, posicao):
        return len(self.__pilhas[posicao])==0
    
    def tamanho_pilhas(self):
        return len(self.__pilhas)

    def criar_pilha(self):
        self.__pilhas.append(Pilha())
    
    def remover_pilha(self):
        self.__pilhas.pop(self.tamanho_pilhas()-1)
    
    def empilhar_pilha(self,pilha):
        pilha_indice= pilha-1
        self.__pilhas[pilha_indice].empilhar(random.randint(2,9))
    
    def desempilhar_pilha(self, pilha):
        pilha_indice=pilha-1
        self.__pilhas[pilha_indice].desempilha()
    
    def elemento_topo(self, pilha):
        return self.__pilhas[pilha-1].pilha_topo()
        

    def buscar(self, pilha, item):
        return self.__pilhas[pilha-1].pesquisar_elemento(item)
    
    def modificar(self, pilha, posicao, item):
        return self.__pilhas[pilha-1].modifica_elemento(posicao, item)
    
    def __str__(self):
        dados=''
        for i in range(len(self.__pilhas)):
            dados=''
            for j in self.__pilhas:
                dados+=f'[{j}] '
            return dados
    
    def apagar_conteudo(self, pilha):
        self.__pilhas[pilha].esvaziar_tudo()

def escolhe_pilha():
    troca = input('deseja trocar a pilha? S/N').lower()
    if troca=='s':
        pilhaA=int(input(('escolha uma pilha')))
        return pilhaA

def menu(pilha, pilha_atual):
    while True:
        acao = input('digite uma ação: ').lower()
        try:
            if acao == 'vv':
                print(pilha.banco_vazio())
            elif acao=='pv':
                print(pilha.pilha_vazia(pilha_atual))
            elif acao=='tp':
                print(pilha.tamanho_pilhas())
            elif acao=='c':
                pilha.criar_pilha()
            elif acao=='r':
                pilha.remover_pilha()
            elif acao=='e':
                pilha.empilhar_pilha(pilha_atual)
            elif acao=='d':
                pilha.desempilhar_pilha(pilha_atual)
            elif acao=='et':
                print(pilha.elemento_topo(pilha_atual))
            elif acao=='b':
                item =int(input('que item quer buscar?'))
                print(pilha.buscar(pilha_atual, item))
            elif acao=='m':
                item = int(input('que item quer colocar?'))
                posicao= int(input('qual a posicao?'))
                pilha.modificar(pilha_atual, posicao, item)
            elif acao=='troca':
                break
            elif acao=='mostrar':
                print(pilha)
            elif acao=='parar':
                print(pilha)
                print('quebrando o loop!')
                break
        except PilhaException as error:
            print(error)
            

if __name__=='__main__':
    banco_pilhas = Banco_pilha()
    banco_pilhas.criar_pilha()
    banco_pilhas.empilhar_pilha(1)
    banco_pilhas.empilhar_pilha(1)
    banco_pilhas.empilhar_pilha(1)
    banco_pilhas.empilhar_pilha(1)

    banco_pilhas.criar_pilha()
    banco_pilhas.empilhar_pilha(2)
    banco_pilhas.empilhar_pilha(2)
    banco_pilhas.empilhar_pilha(2)
    banco_pilhas.empilhar_pilha(2)

    banco_pilhas.criar_pilha()
    banco_pilhas.criar_pilha()
    banco_pilhas.criar_pilha()
    banco_pilhas.criar_pilha()

    banco_pilhas.modificar(1,4,7)
    banco_pilhas.modificar(2,4,11)

    print(banco_pilhas)
    print()
    print(banco_pilhas.elemento_topo(1))
    print(banco_pilhas.elemento_topo(2))