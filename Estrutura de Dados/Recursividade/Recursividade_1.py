#criando um print sem recursão
for i in range(5):
    print('não recursivo')

#criando de modo recursivo
# a recursão vai empilhando as suas chamadas, uma por cima da outra
# quando a chamada terminar, a função desempilha as chamadas feitas

def print_recursivo(quantidade=0):

    print('recursivo')

    quantidade+=1
    if quantidade ==5:
        return
    else:
        print_recursivo(quantidade)

print()

print_recursivo(2)

print()


#soma não recursiva

def soma_sem_recursao(numero=0):
    soma=0
    for i in range(numero+1):
        soma+=i
    return print(soma)

soma_sem_recursao(5)

#soma recursiva

def soma_recursao(numero=0):
    if numero==0:
        return 0
    return numero + soma_recursao(numero-1)

print(soma_recursao(5))


 



