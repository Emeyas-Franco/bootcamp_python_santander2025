#  Crie um programa que imprima três mensagens de boas-vindas diferentes, usando print(), seguindo o estilo de 01-primeiro_programa.py 
 
print('Olá Mundo!')
print('Seja bem vindo ao Python!')
print('Parabéns por aprender Python é uma ótima linguagem de programação!')

#Escreva um script que: Some dois números inteiros. Multiplique um número float por outro float. Imprima o resultado de uma expressão booleana (por exemplo, 5 > 3). Baseie-se em 02-tipods_de_dados.py 

print(5 + 83)
print(8.3 * 9.74)
print(9 * 8.75 /2 > 100)

#Defina variáveis para nome, idade e uma constante PROFISSAO. Atribua a elas valores à sua escolha. Utilize uma f-string para exibir:

nome = 'Emeyas'
idade = 39
PROFISSAO = 'programador'

print(f'Meu nome é {nome}, tenho {idade} e sou {PROFISSAO}.')

#Crie uma lista chamada estados, contendo ao menos 5 siglas de estados brasileiros. Imprima o terceiro item da lista (índice 2) e, em seguida, adicione mais um estado e imprima todo o conteúdo da lista. Veja o exemplo em 03-variaveis_constantes.py.

ESTADOS = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE']

print(ESTADOS[2])
ESTADOS.append('TO')
print(ESTADOS)

#Faça um programa que: Receba uma string representando um número (por exemplo, "25"). Converta essa string para inteiro e some 5 a ela.Converta o resultado de volta para string e exiba com print(). Use como referência 04-convertendo_tipos.py.
numero = '25'
numero = int(numero)
numero = numero + 5
print(str(numero))

#Entrada de dados do usuário Desenvolva um script que: Peça ao usuário que informe seu nome e sua idade (duas entradas com input()). Exiba uma mensagem formatada dizendo “Olá, <nome>, você tem <idade> anos!”. Baseie-se em 05-print_input.py. 
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')

print(f'Olá, {nome}, você tem {idade} anos!')

#Calculadora simples Combine input() e conversão de tipos para criar uma mini-calculadora que: Pergunte ao usuário por dois números (podem ser floats). Calcule e mostre soma, subtração, multiplicação e divisão inteira dos valores. Explore conceitos de 02-tipods_de_dados.py e 04-convertendo_tipos.py.
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')
operador = input('Digite um operador +, -, * ou /: ')
resultado = numero_1 + operador + numero_2

print(f'O resultado da operação é {resultado}.')



#Desafio extra: cadastro de usuários Crie um programa que: Pergunte quantos usuários serão cadastrados. Para cada usuário, receba nome e idade. Armazene cada par (nome, idade) em uma lista de tuplas. Ao final, percorra a lista e imprima: Combine tudo o que aprendeu: input(), listas, tuplas, laços e f-strings.
