from Pilha import *
import random

class BancoDeDadosException(Exception): 
    def __init__(self, msg):
        super().__init__(msg)

class BancoDeDados:
    def __init__(self) -> None:
        self._pilhas = [Pilha()] #programa inicia com uma pilha
    
    def verifica_vazia(self, indice):
        try:
            return self._pilhas[indice].tamanho_pilha()==0
        except IndexError:
            raise BancoDeDadosException(f'erro ao acessar o indice {indice}, o tamanho do banco de dados é {len(self._pilhas)-1}')

    def tamanho_banco(self):
        return f'{len(self._pilhas)}'

    def preenche_pilha(self, indice_pilha):
        try:
            self._pilhas[indice_pilha].empilhar(random.randint(1,8))
        except IndexError:
            raise BancoDeDadosException(f'erro ao acessar a pilha {indice_pilha}, os indices do banco de dados é {len(self._pilhas)-1}')
    
    def excluir_item(self, indice_pilha):
        try:
            self._pilhas[indice_pilha].desempilha()
        except IndexError:
            raise BancoDeDadosException(f'erro ao acessar a pilha {indice_pilha}, os indices do banco de dados é {len(self._pilhas)-1}')

    def cria_pilha(self):
        self._pilhas.append(Pilha())
    
    def verifica_pilha(self, indice):
        try:
            return self._pilhas[indice]
        except IndexError:
            raise BancoDeDadosException(f'erro ao acessar a pilha {indice}, os indices do banco de dados é {len(self._pilhas)-1}')

    def tamanho_pilha(self, indice):
        try:
            return self._pilhas[indice].tamanho_pilha()
        except IndexError:
            raise BancoDeDadosException(f'erro ao acessar a pilha {indice}, os indices do banco de dados é {len(self._pilhas)-1}')
    
    def elemento_do_topo(self, indice):
        try:
            return self._pilhas[indice].elemento_topo()
        except:
            raise BancoDeDadosException(f'erro ao acessar a pilha {indice}')

    def inverter(self, indice):
        try:
            self._pilhas[indice].inverte_pilha()
        except:
            raise BancoDeDadosException(f'erro ao acessar a pilha {indice}')
    
    def concatenar_pilhas(self, pilha1, pilha2):
        self._pilhas[pilha1].empilhar(self._pilhas[pilha2])
        
    def esvaziar_pilha(self, indice_pilha):
        self._pilhas[indice_pilha].limpar_pilha()

    
    def __str__(self):
        dados =''
        for i in self._pilhas:
            dados+=str(i)
        return dados

    def imprime_pilha(self)->str:
        print(self.__str__())

if __name__=='__main__':
    try:
        banco_dados = BancoDeDados()
        
       

        banco_dados.cria_pilha()
        print(banco_dados.tamanho_banco())
        banco_dados.cria_pilha()
        banco_dados.cria_pilha()
        banco_dados.cria_pilha()

        banco_dados.preenche_pilha(1)
        banco_dados.preenche_pilha(1)
        banco_dados.preenche_pilha(1)

        
        banco_dados.preenche_pilha(2)
        banco_dados.preenche_pilha(2)
        banco_dados.preenche_pilha(2)
        
        print(banco_dados)
        
        #banco_dados.imprime_pilha()
        
        print(banco_dados.verifica_pilha(1))

        banco_dados.inverter(1)

        print(banco_dados.verifica_pilha(1))
        print(banco_dados.verifica_pilha(2))

        banco_dados.concatenar_pilhas(1,2)
        

        print(banco_dados.verifica_pilha(1))
        print(banco_dados.verifica_pilha(2))
        banco_dados.esvaziar_pilha(2)
        print(banco_dados.verifica_pilha(2))
        
        print(banco_dados.verifica_vazia(5))

    except BancoDeDadosException as bdde:
        print(bdde)





