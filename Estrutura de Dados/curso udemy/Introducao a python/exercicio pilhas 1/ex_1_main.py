import random
from class_ex1 import *

pilha_teste = Pilha()

string_teste = input('insira uma expressão')

for i in string_teste:

    if i=='{' or i=='[' or i=='(':
        pilha_teste.empilhar(i)

    elif i=='}' or i==']' or i==')':
        string_checagem = str(pilha_teste.desempilhar())
        if (i=='}' and string_checagem!='{') or (i==']' and string_checagem!='[') or (i==')' and string_checagem!='('):    
            print('deu erro na posição ai')
            break
        else:
            print('kkkk deu erro dnv')


print(pilha_teste)