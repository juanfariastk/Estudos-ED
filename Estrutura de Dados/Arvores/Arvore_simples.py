#arvore simples

class No:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None

    def __str__(self):
        return str(self.dado)

class Arvore:
    def __init__(self, dado):
        novo_no = No(dado)
        self.raiz = novo_no
    

if __name__ == "__main__":
    arvore = Arvore(1)
    arvore.raiz.esq = No(2)
    arvore.raiz.dir = No(3)

    print(arvore.raiz.dir)

