#Ler dois números inteiros, executar e mostrar o resultado das seguintes operações: adição, subtração, multiplicação e divisão

from math import comb


a= int(input())
b = int(input())
print(a*b)
print(a-b)
print(a/b)

#Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, será possível obter a distância percorrida com a fórmula DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, tempo gasto na viagem, a distância percorrida e a quantidade de litros utilizada na viagem

km_por_litro = 12
tempo_gasto = int(input('tempo gasto?'))
km_media = int(input('velocidade media?'))

distancia = tempo_gasto*km_media

combustivel = distancia/km_por_litro
print(km_media)
print(tempo_gasto)
print(distancia)
print(combustivel)

#Leia a idade do usuário e classifique-o em:
#- Criança – 0 a 12 anos
#- Adolescente – 13 a 17 anos
#- Adulto – acima de 18 anos
#-Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida

idade = int(input('digite sua idade'))

if idade>0 and idade<=12:
    print('criança')
elif idade>12 and idade<=17:
    print('adolescente')
elif idade>=18:
    print('adulto')
else:
    print('digite uma idade válida!')
    
#Calcular a média de um aluno que cursou a disciplina de Programação I, a partir da leitura das notas M1, M2 e M3; passando por um cálculo da média aritmética. Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou pegou exame
#- Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
#- Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
#- Se a média for maior do que 6.0, o aluno está aprovado
#- Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for maior do que 6.0, está aprovado, senão; está reprovado

m1 = float(input('n1'))
m2 = float(input('n2'))
m3 = float(input('n3'))

media = (m1+m2+m3)/3
media_aprovado =6.0
aprovado = False
reprova = False
exame_novo = 0
if media>media_aprovado:
    aprovado = True
    print(aprovado)

elif media>=4 and media<=media_aprovado:
    exame_novo = float(input('qual a nota do exame?'))
    if exame_novo>media_aprovado:
        aprovado=True
        print(exame_novo, 'aprovado = ',aprovado )
    else:
        reprova = True
        print('reprovado = ', reprova )

else:
    reprova = True
    print('reprovado = ', reprova)



#Para revisar o conteúdo prático visto até agora, você agora pode resolver dois exercícios. Logo em seguida você pode acessar a aula em vídeo com a solução. Implemente cada exercício utilizando tanto o for quanto o while

#Ler 5 notas e informar a média

#Imprimir a tabuada do número 3 (3 x 1 = 1 - 3 x 10 = 30)

nota_soma=0
for i in range(5):
    nota= float(input(f'notas {i+1}'))
    nota_soma+=nota

media = nota_soma/5
print(media)

contador_while = 0
nota_while = 0

while contador_while<5:
    nota=float(input(f'notas{contador_while+1}'))
    nota_while+=nota
    contador_while+=1

media_while = nota_while/5

print(media_while)

#----------#

numero = int(input('escolha um numero'))
for i in range(11):
    print(f'{numero} x {i} = {numero*i}')


numero_while = int(input('escolha um numero'))
parada = 0
while parada<=10:
    print(f'{numero_while} x {parada} = {numero_while*parada}')
    parada+=1


