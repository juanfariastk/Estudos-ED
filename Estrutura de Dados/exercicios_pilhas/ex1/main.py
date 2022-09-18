from Banco_dados import *
from Pilha import *
import os

banco_de_dados = BancoDeDados()
pilha_atual=0
pilha_para_concatenar=0
elemento_topo=0

while True:



    print('Controle de pilhas v1','|----------------------|',f' Pilha atual: {pilha_atual+1} de {banco_de_dados.tamanho_banco()}', f' Topo = [{elemento_topo}]','|----------------------|', '(e) empilhar', '(d) desempilhar', '(t) tamanho', '(o) obter elemento do topo', '(r) criar pilha', '(n) inverter elementos da pilha', '(z) esvaziar pilha' , '(c) concatenar duas pilhas', '(m) escolher outra pilha', '(s) sair', '|----------------------|', sep='\n' )
    
    acao = input('o que deseja fazer ?').lower()

    try:
        if acao=='e':
            banco_de_dados.preenche_pilha(pilha_atual)
        elif acao=='d':
            banco_de_dados.excluir_item(pilha_atual)
            elemento_topo= banco_de_dados.elemento_do_topo(pilha_atual)
        elif acao=='t':
            print('o tamanho desta pilha é:', banco_de_dados.tamanho_pilha(pilha_atual))
        elif acao=='o':
            elemento_topo = banco_de_dados.elemento_do_topo(pilha_atual)
        elif acao=='r':
            banco_de_dados.cria_pilha()
        elif acao=='n':
            banco_de_dados.inverter(pilha_atual)
        elif acao=='z':
            banco_de_dados.esvaziar_pilha(pilha_atual)
            elemento_topo=0
        elif acao=='c':
            pilha_para_concatenar=int(input('digite uma pilha para ser concatenada à pilha atual'))
            banco_de_dados.concatenar_pilhas(pilha_atual, pilha_para_concatenar)
        elif acao=='m':
            pilha_atual = int(input('escolha uma pilha'))
            pilha_atual = pilha_atual-1
            elemento_topo=banco_de_dados.elemento_do_topo(pilha_atual)
        elif acao=='s':
            break
        else:
            print('escolha uma ação válida!')
    
        os.system('clear')

    except BancoDeDadosException as bdde:
        print(bdde)  


        

    
    
