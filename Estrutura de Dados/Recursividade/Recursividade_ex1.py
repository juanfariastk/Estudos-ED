""" 
1- O fatorial de um número inteiro m não negativo, é indicado por m! (lê-se "m fatorial") e é definido pela relação:

m!=m⋅(m-1)⋅(m-2)⋅(m-3)...3⋅2⋅1, para m ≥ 2.

Algumas definições são:

- 1! = 1 (fatorial de 1) - critério de parada

- 0! = 1 (fatorial de 0)

Exemplos:

- 3! = 3 . 2 . 1 = 6

- 4! = 4 . 3 . 2 . 1 = 24

- 6! = 6 . 5 . 4 . 3 . 2 . 1 = 720



2- Crie uma função recursiva que calcule o valor de a (base) elevado a b (expoente)

- Se o expoente for zero, a potência é igual 1 (critério de parada)

- Não considere exponenciação de números negativos"""


def fatorial_recursivo(numero):
    if numero==0:
        return 1
    
    return numero * fatorial_recursivo(numero-1)

print(fatorial_recursivo(6))


def potencia_recursiva(base, expoente):
    if expoente == 0:
        return 1
    
    return base*potencia_recursiva(base, expoente-1)

print(potencia_recursiva(3,2))

def fibonacci(numero):
    if numero==1 or numero==0:
        return numero
    return (fibonacci(numero-1) + fibonacci(numero-2))

print(fibonacci(10))


def teste (numero):
    if numero==0:
        return 0
    return (numero%10 + teste(int(numero/10)))

print(teste(35))