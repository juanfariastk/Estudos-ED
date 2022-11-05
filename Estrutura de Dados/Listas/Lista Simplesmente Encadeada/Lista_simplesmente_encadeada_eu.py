
class ListaExcept(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class No:
    def __init__(self,dado):
        self.__dado=dado
        self.__proximo=None

    @property
    def dado(self):
        return self.__dado
        
    @property
    def proximo(self):
        return self.__proximo
    
    @dado.setter
    def dado(self, novo):
        self.__dado = novo
    
    @proximo.setter
    def proximo(self, novo):
        self.__proximo = novo

    def __str__(self):
        return str(self.__dado)

class ListaSimplesmenteEncadeada:
    def __init__(self):
        self.__cabeca = None
        self.__tamanho=0
    
    def lista_vazia(self):
        return self.__tamanho==0
    
    def lista_tamanho(self):
        return self.__tamanho
    
    def busca(self, dado):
        if self.lista_vazia():
            raise ListaExcept('A fila está vazia!')
        apontador=self.__cabeca
        cont=1
        while(apontador):
            if apontador.dado==dado:
                return cont
            cont+=1
            apontador = apontador.proximo

        raise ListaExcept(f'o dado {dado} não existena lista')
    
    def elemento(self, posicao):
        try:
            assert posicao>0

            if self.lista_vazia():
                raise ListaExcept('A fila está vazia')
                
            apontador=self.__cabeca
            cont=1

            while(apontador!= None and cont<posicao):
                apontador=apontador.proximo
                cont+=1
            
            if(apontador!=None):
                return apontador.dado
            
            raise ListaExcept('Esta posição não existe na lista')
        except TypeError:
            raise ListaExcept('O dado referente a posição precisa ser um valor inteiro')
        except AssertionError:
            raise ListaExcept('Não é possível acessar posições negativas')
        except:
            raise
    
    def inserir(self, posicao,dado):
        try:
            assert posicao>0
            if self.lista_vazia(): #adicionando na lista enquanto ela está vazia
                if(posicao!=1):
                    raise ListaExcept(f'A lista está vazia. Adicione o dado na posição inicial 1')
                self.__cabeca=No(dado)
                self.__tamanho+=1
                return

            if(posicao==1): #inserindo na primeira posição, no caso da lista não estiver vazia
                novo=No(dado)
                novo.proximo=self.__cabeca
                self.__cabeca = novo
                self.__tamanho+=1

            apontador = self.__cabeca
            cont=1

            while(cont<posicao-1 and apontador!=None): #adicionando após a primeira posição
                apontador=apontador.proximo
                cont+=1
            
            if (apontador==None): #verifica se o apontador retorna um objeto valido
                 raise ListaExcept('Posição inválida')

            novo = No(dado)
            novo.proximo = apontador.proximo
            apontador.proximo = novo
            self.__tamanho+=1

        except TypeError:
            raise ListaExcept('Informe um numero inteiro como uma posição')
        except AssertionError:
            raise ListaExcept('Informe um valor positivo')
        except:
            raise
    
    def remover(self, posicao):
        try:
            assert posicao>0
            if self.lista_vazia():
                raise ListaExcept('A lista está vazia, não foi possível remover')
            
            apontador = self.__cabeca
            cont=1

            while(cont<=posicao-1 and apontador!=None):
                anterior = apontador
                apontador = apontador.proximo
                cont+=1
            
            if apontador==None:
                raise ListaExcept('Posição inválida, pois excede a quantidade de elementos')
            
            dado = apontador.dado

            if posicao==1:
                self.__cabeca = apontador.proximo
            else:
                anterior.proximo = apontador.proximo

            self.__tamanho-=1
            return dado

        except TypeError:
            raise ListaExcept('Informe o NÚMERO da posição')
        except AssertionError:
            raise ListaExcept('Informe um valor positivo')
        except:
            raise
    
    def __str__(self):
        str = 'Elementos da lista: '
        apontador = self.__cabeca
        while(apontador):
            str+=f'{apontador.dado}'
            apontador = apontador.proximo
            if apontador:
                str+=' => '
        return str
    
    def imprimir(self):
        print(self.__str__())
    
    def modificar(self, posicao, dado):
        try:
            assert posicao>0
            if self.lista_vazia():
                raise ListaExcept('A lista está vazia!')

            apontador = self.__cabeca
            cont=1
            while( apontador!= None and cont<posicao):
                apontador=apontador.proximo
                cont+=1

            if (apontador!=None):
                apontador.dado = dado
                return
            raise ListaExcept('Posição inválida para a lista')
        
        except TypeError:
            raise ListaExcept('Informe um valor inteiro para a posição')
        except AssertionError:
            raise ListaExcept('Informe um valor positivo')
        except:
            raise

if __name__=='__main__':
    nova_lista = ListaSimplesmenteEncadeada()

    for i in range(1,11):
        nova_lista.inserir(i, i+1)
    
    nova_lista.imprimir()
    nova_lista.modificar(1,10)
    nova_lista.imprimir()
    a = nova_lista.elemento(10)
    nova_lista.inserir(20,10)
    print(a)


            
            

            


            
        

        
        