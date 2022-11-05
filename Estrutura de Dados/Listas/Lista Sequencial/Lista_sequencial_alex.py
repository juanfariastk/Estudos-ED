from multiprocessing.sharedctypes import Value
from os import sep
from turtle import pos
from typing import List


class ListaExcept(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class ListaSequencial:
    def __init__(self):
        self.__dados = []
    
    def vazia(self):
        return len(self.__dados)==0
    
    #def cheia(self):

    def tamanho(self):
        return len(self.__dados)
    
    def busca(self, dado): #retorna a posição do dado encontrado
        try:
            for i in len(self.__dados):
                if self.__dados[i]==dado:
                    return i+1
        except ValueError:
            raise ListaExcept(f'O dado {dado} não se encontra na lista!')
        except:
            raise
        #outro metodo é self.__dados.index(dado)+1
    
    def elemento(self, posicao): #retorna o elemento de uma posição encontrada
        try:
            assert posicao>0
            return self.__dados[posicao-1]
        except TypeError:
            raise ListaExcept(f'Posição não é um tipo inteiro')
        except IndexError:
            raise ListaExcept(f'Posição inválida!')
        except AssertionError:
            raise ListaExcept(f'Posição negativa!')
        except:
            raise
    
    def inserir(self, posicao, dado): #recebe uma posição e um dado, lembrando que tem deslocamento 
        try:
            assert posicao>0
            self.__dados.insert(posicao-1, dado)
        except AssertionError:
            raise ListaExcept(f'Posição negativa detectada!')
        except IndexError:
            raise ListaExcept(f'Posição inválida detectada!')
        except TypeError:
            raise ListaExcept(f'Posição não é do tipo inteiro!') 
        except:
            raise

    def remover(self, posicao): #recebe uma posição e vai retornar o dado removido, lembrando que o deslocamento já é feito automaticamente
        if self.vazia():
            raise ListaExcept(f'Lista está vazia!')
        try:
            assert posicao>0
            dado = self.__dados[posicao-1]
            del self.__dados[posicao-1]
            return dado
        except AssertionError:
            raise ListaExcept(f'Posição irregular!')
        except IndexError:
            raise ListaExcept(f'Posição inexistente')
        except TypeError:
            raise ListaExcept(f'Tipo de dado da posição não é válido')
        except:
            raise
    
    def imprimir(self): #imprime o conteúdo da lista
        print(self.__str__())
    
    def modificar(self, posicao, novo_dado): #modifica o elemento em uma posicao
        if self.vazia():
            raise ListaExcept(f'Não foi posivel modificar! A lista está vazia.')
        try:
            assert posicao>0
            self.__dados[posicao-1]=novo_dado
            return False
        except AssertionError:
            raise ListaExcept(f'Índice de posição negativo!')
        except IndexError:
            raise ListaExcept(f'Índice de posição inválido!')
        except TypeError:
            raise ListaExcept(f'O tipo de dado do índici é inválido')

    def __str__(self):
        if self.vazia():
            raise ListaExcept(f'Lista está vazia!')
        return self.__dados.__str__()
    

if __name__=='__main__':
    print('Inicio do programa')
    print()

    lista1 = ListaSequencial()

    print('Retornos básicos')
    print(lista1.vazia())
    print(lista1.tamanho())

    for i in range(1,11):
        lista1.inserir(1, i*10)
    
    
    print('Retornos intermediários:')
    print(lista1)
    valor_removido = lista1.remover(3)
    print(valor_removido)
    print(lista1)

    print()
    print('Modificar:')
    lista1.modificar(9,1000)
    lista1.imprimir()

    #tratamento de exceções
    try:
        lista2 = ListaSequencial()
        print(lista2)
        print(lista1)
    except ListaExcept as li:
        print(li)
    
    
            

    