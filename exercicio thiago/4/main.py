from conta_class_banco_class import *

try:
    banco1 = Banco()
    banco1.adc_conta(1234,3000,'juan')
    banco1.adc_conta(12345,3000,'zezinho')
    banco1.adc_conta(12343,3000,'loirinho')
    banco1.saque_conta(12343,20000)
    banco1.depositar(12343, 1000)

except OperacaoInvalidException as m:
    print(m)

print(banco1)
print(banco1.contas_banco)
