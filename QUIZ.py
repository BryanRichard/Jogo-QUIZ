"""JOGO DE QUIZ"""
import random

print('')
print('  / __ \     ) )  ( (   (_   _)  (____  )  ')
print(' / /  \ \   ( (    ) )    | |        / /   ')
print('( (    ) )   ) )  ( (     | |    ___/ /_   ')
print('( (  /\) )  ( (    ) )    | |   /__  ___)  ')
print(' \ \_\ \/    ) \__/ (    _| |__   / /____  ')
print('  \___\ \_   \______/   /_____(  (_______) ')
print('       \__)                                ')
print('')

print('Inicio')
print('')

score = 0
adivinhar = 0
"""INICIO"""
print('A cada aceto você recebera 100 pontos.')
print('Antes de pular para a proxima pergunta você tera a chance de adivinhar o número rodado de um dado.')
print('Se conseguir adivinhar a onde caiu o dado recebera uma dica na questão')
print('')

print('As questões vão de 1..4 é importante responder com o número que deseja.')
print('')
print('Qual o maior país do mundo ?')
print('')
print('1. Brasil')
print('2. China')
print('3. EUA')
print('4. Russia')

print('')
resposta = int(input('Digite a resposta : '))


"""ENQUANTO A RESPOSTA FOR FALSA"""
while resposta < 1 or resposta > 4:
    resposta = int(input('Digite uma resposta correta : '))

print('')


"""ACERTO OU ERRO DA QUESTÃO"""
if resposta == 4:

    print('Você acertou a questão.')
    score += 100

    print('Sua pontuação: %i'%score)

else:

    print('Você não acerto a questão.')
    print('Sua pontuação: %i'%score)


"""GIRAR O DADO"""
for i in range(1,7):
    dado = random.randint(1,6)
print('')
print('DADO')
print('')


"""RESPOSTA DO DADO"""
resposta = int(input('Digite um número entre 1 e 6 : '))


"""ENQUANTO A RESPOSTA DO DADO FOR FALSA"""
while resposta < 1 or resposta > 6:
    resposta = int(input('O dado se encontra entre 1 e 6 digite uma resposta correta : '))


"""SE ACERTO OU ERRO O DADO"""
if resposta == dado:
    print('Você adivinhou a onde o dado caiu')
    adivinhar += 1
else:
    print('Você não adivinhou o dado.')


"""OUTRA PERGUNTA"""
print('')
print('Qual o menor estado do Brasil ? ')
print('')
print('1. Roraima')
print('2. Sergipe')
print('3. Acre')
print('4. Espirito Santo')

print('')


"""SE TIVER DICAS"""
if adivinhar >= 1:

    print('Quantidade de dicas que você tem %i'%adivinhar)
    print('')
    dica = str(input('Deseja utilizar sua dica Sim ou Nao ? '))
    newresp = dica.upper()
    while newresp != 'SIM' and newresp != 'NAO':
        dica = str(input('Digite Sim ou Não: '))
        newresp = dica.upper()
    if newresp == 'SIM':
        print('É um estado que se encontra no Nordeste.')
        adivinhar -= 1
"""FIM DAS DICAS"""


print('')

resposta = int(input('Digite sua resposta : '))


"""ENQUANTO A RESPOSTA FOR FALSA"""
while resposta < 1 or resposta > 4:
    resposta = int(input('Digite sua resposta : '))
print('')


"""SE ACERTOU OU ERROU"""
if resposta == 2:
    print('Você acertou a questão.')
    score += 100
    print('Sua pontuação %i'%score)
else:
    print('Você não acertou a questão')
    print('Sua pontuação %i'%score)
print('')


"""GIRO DO DADO"""
for a in range(1,7):
    dado = random.randint(1,6)

resposta = int(input('Tente adivinhar o dado novamente 1 .. 6 : '))


"""ENQUANTO RETORNAR FALSO"""
while resposta < 1 or resposta > 6:
    resposta = int(input('O dado esta entre 1 e 6 : '))

if resposta == dado:
    print('Você adivinhou o dado')
    adivinhar += 1
else:
    print('Você não adivinhou a onde caiu o dado.')


"""OUTRA PERGUNTA"""
print('')
print('Quem ganhou o Nobel de 1965 ?')
print('1. Richard Feynman')
print('2. Albert Aisten')
print('3. Nicola Tesla')
print('4. Stephen Hawking')
print('')


"""SE TIVER DICAS"""
if adivinhar >= 1:

    print('Quantidade de dicas que você tem %i'%adivinhar)
    print('')
    dica = str(input('Deseja utilizar sua dica Sim ou Nao ? '))
    newresp = dica.upper()
    while newresp != 'SIM' and newresp != 'NAO':
        dica = str(input('Digite Sim ou Não: '))
        newresp = dica.upper()
    if newresp == 'SIM':
        print('Foi um dos pioneiros da eletrodinâmica quantica.')
        adivinhar -= 1
"""FIM DAS DICAS"""


print('')
resposta = int(input('Digite sua resposta : '))


"""ENQUANTO A RESPOSTA RETORNAR FALSA"""
while resposta < 1 or resposta > 4:
    resposta = int(input('Digite sua resposta : '))
print('')


"""SE ACERTOU OU ERROU"""
if resposta == 1:
    print('Você acertou')
    score += 100
    print('Sua pontuação %i'%score)
else:
    print('Você não acertou')
    print('Sua pontuação %i'%score)


"""FIM DE JOGO"""
print('')
print('O JOGO TERMINOU')