
#introdução ao paradigma orientado a objetos

class Aluno:

    #criando metodo construtor (ação construtora)

    def __init__(self, nome, idade, matricula):
        
        #criando os atributos e adicionando a valores recebidos

        self.nome = nome
        self.idade = idade
        self.matricula = matricula


#teste da classe

aluno = Aluno('juan', 17, '20221370021')

print('nome aluno ', aluno.nome)
print('idade aluno ', aluno.idade)
print('matricula aluno ', aluno.matricula)



#USO DE METODOS (AÇÃO/COMPORTAMENTOS)

#criando classe Ponto

class Ponto:
    
    #criando metodo construtor

    def __init__(self, x,y):
        
        #atribuindo valores aos atributos

        self.x = x
        self.y = y
    
    #definindo qual o quadrante que se encontra x e y, por meio do metodo quadrante()

    def quadrante(self):

        #criando comparador

        if self.x>0 and self.y>0:
            return '1º quadrante'

        elif self.x<0 and self.y>0:
            return '2º quadrante'
        
        elif self.x<0 and self.y<0:
            return '3º quadrante'
        
        elif self.x>0 and self.y<0:
            return '4º quadrante'
        
        else:
            return 'indefinido'


#teste da classe e do metodo

p1 = Ponto(2,5)
p2 = Ponto(-3,9)

print(p1.quadrante())
print(p2.quadrante())



#encapsulamento de objeto

#criando uma classe com o encapsulamento com underline

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    #metodo get
    def get_idade(self):
        return self._idade
    
    def get_nome(self):
        return self._nome
    
    #metodo set
    def set_idade(self, nova_idade):
        self._idade = nova_idade
    

pes1 = Pessoa('joao', 28)
print(pes1.get_idade())


#encapsulamento com property

class Pessoa2:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    #metodo get
    @property
    def idade(self):
        return self._idade
        
    @property
    def nome(self):
        return self._nome
    
    #metodo set
    @idade.setter
    def idade(self, nova_idade):
        self._idade = nova_idade

ps2 = Pessoa2('joaozito', 28)
ps2.idade = 38
print(ps2.idade)