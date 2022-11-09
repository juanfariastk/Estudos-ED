
#ex1 quantidade de caracteres da string

def tamanho_string(frase,cont=0):
    if(frase==''):
        return cont
    cont+=1
    return tamanho_string(frase[1::], cont)

print(tamanho_string('slameuirmao'))

#ex2 imprime uma string de modo recursivo, cada caractere

def imprimir_recursivo(frase):
    if(frase==''):
        return
    print(frase[0])
    imprimir_recursivo(frase[1::])

imprimir_recursivo('slameuirmao')

#ex3 print recursivo invertido

def imprimir_recursivo_invertido(frase):
    if(frase==''):
        return
 
    imprimir_recursivo_invertido(frase[1::])
    print(frase[0], end='')

imprimir_recursivo_invertido('slameuirmao')


#ex4 comparador de duas strings

#ta dando erro

#ex5 palindromos

def palindromo(frase):
    if len(frase)<2:
        return True
    if frase[0]!=frase[-1]:
        return False
    return palindromo(frase[1:-1:])

print()

print(palindromo('1001001'))


    
    
