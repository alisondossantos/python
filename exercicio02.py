#escreva um algoritmo que leia o nome completo de uma pessoa
#mostre o nome com todas as letras maiusculas e todas as letras minusculas
#quantas letras tem o nome completo
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome: ')).strip(' ') #strip() funcao que elimina os espacos fazios
print('Seu nome com letras maiusculas: {}'.format(nome.upper()))#.upper() funcao que escreve todas as letras maiusculas
print('Seu nome com letras minusculas {}'.format(nome.lower()))#lowe() funcao que escreve todas as letras sem minusculas
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))#len() funcao que conta o total de caracteres
separa = nome.split()#funcao cadeia de caracteres em blocos menoresS
print('Seu primeiro nome {} tem {} letras'.format(separa[0], len(separa[0])))