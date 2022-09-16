from carta import Cartas

import random

class Baralho:

    def __init__(self):
        self.container = list()
        tipo = ['Copas', 'Espada', 'Ouros', 'Paus']
        valor = ['às', 'dois', 'tres', 'quatro', 'cinco', 'seis','sete', 'oito', 'nove', 'valete', 'dama', 'rei']
        cor = ['vermelho', 'preto', 'vermelho', 'preto']

        for i in range(len(tipo)):
            for j in range(len(valor)):
                self.container.append(Cartas(tipo[i], valor[j], cor[i]))

        


    def __str__(self):
        bar_feito=''
        for i in self.container:
            bar_feito+= (i.__str__() + '\n')
        return bar_feito
    
    def __len__(self):
        return len(self.container)

    
    def embaralhar(self):
        random.shuffle(self.container)
    

 