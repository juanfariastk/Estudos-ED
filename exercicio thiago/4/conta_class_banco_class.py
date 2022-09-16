#definindo o controle dos erros

class OperacaoInvalidException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class Banco:

    def __init__(self) :
        self._contas = dict()
        self._saldotot = 0
    
    def saque_conta(self, numero, valor):
        try:
            assert valor>0
            conta = self._contas[numero]
            if conta.saldo - valor >= 0:
                conta.saldo -= valor
            else:
                raise OperacaoInvalidException(f' Conta {numero}: Saldo insuficiente para saque')
        except AssertionError:
            raise OperacaoInvalidException('Quantia a retirar não pode ser negativa')
        except KeyError:
            raise OperacaoInvalidException(f' Conta {numero} não está cadastrada ou inexistente')

    @property
    def contas_banco(self):
        contas_print=''
        for i in self._contas.keys():
            contas_print+=f'{i}: titular {self._contas[i].nome}, saldo =  {self._contas[i].saldo}\n'
        return contas_print


        return contas_print

    def depositar(self, numero, valor):
        self._contas[numero].saldo+=valor
    
    def adc_conta(self, numero, saldo, titular):
        if numero not in self._contas.keys():
            self._contas[numero]=ContaCorrente(numero, saldo, titular)
        else:
            raise OperacaoInvalidException(f'Conta de numero {numero} já está cadastrada')
        
    def __str__(self) -> str:
        conta_fim=''
        contador = 1
        for i in self._contas.keys():
            conta_fim+=f'{contador:02}:{i}, titular {self._contas[i].nome}, saldo =  {self._contas[i].saldo}\n'
            contador +=1
        return conta_fim


class ContaCorrente:

    def __init__(self, conta: int, saldo: float, nome: str):
        self._conta = conta
        self._saldo = saldo
        self._nome = nome

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @property
    def nome(self):
        return self._nome

    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor

    #metodo saque
    def saque(self, valor):
        sucesso = False
        if self._saldo >= valor:
            sucesso = True
            self._saldo = self._saldo - valor
            return sucesso

        else:
            return sucesso  #'não tem saldo'

    def deposito(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'conta:{self._conta}, seu saldo é {self._saldo}, sendo o titular{self._nome}'




