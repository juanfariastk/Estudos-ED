#criando classe peças



class Pecas:
    def __init__(self, idi, nome):
        self._id = idi
        self._nome = nome 
    
    @property
    def idi(self):
        return self._id
    
    @property 
    def nome(self):
        return self._nome
    
    @idi.setter
    def id(self, novo_id):
        self._id = novo_id

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
    
    def __str__(self):
        return f'id da peça {self._id} sendo o nome: {self._nome},'
    
    


#criando classe carro

class Carro:
    def __init__(self, cor, placa, pecas =[]):
        self._cor = cor
        self._placa = placa
        self._pecas = pecas

    
    #gets
    @property
    def cor(self):
        return self._cor
    
    @property
    def placa(self):
        return self._placa
    
    @property
    def pecas(self):
        return self._pecas
    
    #sets
    @cor.setter
    def cor(self, nova_cor):
        self._cor = nova_cor
    
    @pecas.setter
    def pecas(self, nova_pecas):
        self._pecas = nova_pecas
    
    #metodos
    def adiciona_pec(self, nova_peca):
        self._pecas.append(nova_peca)


    #retorno final
    def __str__(self):
        final =''
        for i in range(len(self._pecas)):
            final+=f'{self._pecas[i]} '
        return f'este carro tem a cor {self.cor}, de placa {self._placa} e o peças {final}'

if __name__ =='__main__':
    pec=[]
    p1 = Pecas('1', 'chassi')
    p2 = Pecas('33', 'volante')
    p3 = Pecas('45', 'som auto')
    pec.append(p1)
    pec.append(p2)
    pec.append(p3)
    car1 = Carro('preto', 'SDK-3458', pec)
    print(car1)