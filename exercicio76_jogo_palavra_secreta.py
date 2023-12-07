"""
Curso de Python 3 - Udemy
Exercício 76 - Jogo da palavra secreta
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade
para o usuário digitar apenas uma letra.
- Qual o usuário digitar uma letra, você vai conferir se a letra digitada
está na palavra secreta.
- Se a letra digitada estiver na palavra secreta; exiba a letra;
- Se a letra digitada não estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.
"""
from time import sleep
from random import randint

# Listas, Constantes e variáveis
lista_palavras = ['ferrugem', 'banana', 'mostarda', 'perfume', 'presente',
                  'leitura', 'caloria', 'essencial', 'excelente', 'vermelho',
                  'biblioteca', 'misterioso', 'anatomia', 'carruagem',
                  'costureira', 'adesivo', 'natureza', 'bicarbonato',
                  'microfone', 'chaleira', 'morango', 'girafa', 'marinheiro',
                  'casamento', 'galinha', 'cachorro', 'felicidade', 'vendedor',
                  'guloseima', 'interestadual', 'palpite', 'longitude',
                  'produtividade', 'transporte', 'absoluto', 'bailarina',
                  'narrador', 'churrasqueira', 'biscoito', 'elefante',
                  'ventilador', 'nacionalidade', 'ferramenta', 'instrumento']
print(lista_palavras)
rand = randint(0, 43)
PALAVRA_SECRETA = lista_palavras[rand]
lista_secreta = ['*',] * len(PALAVRA_SECRETA)
palavra_formatada = ''.join(lista_secreta)
letra = ''
incorretas = ''
contador = 0

print('\033[44m JOGO DA PALAVRA SECRETA \033[m')
sleep(1)

print('\nTente adivinhar, letra por letra, qual a palavra secreta.\n')
sleep(2)

print(f'Palavra Secreta: {palavra_formatada} {len(palavra_formatada)} letras')
sleep(1)

# Código
while True:

    letra = input('\nDigite uma letra: ').lower()  # Input Letra

    if letra.isnumeric():  # Tratando input numéricos
        print('Não digite números!')
        continue

    if not letra.isalpha():  # Tratando input símbolos
        print('Não digite símbolos!')
        continue

    if len(letra) > 1:  # Tratando input com mais de uma letra
        print('Digite apenas uma letra!')
        continue

    if letra in PALAVRA_SECRETA:  # Letras Corretas
        indice = 0
        for i in PALAVRA_SECRETA:
            if letra == i:
                lista_secreta[indice] = i
                palavra_formatada = ''.join(lista_secreta)
            indice += 1
    else:
        if letra not in incorretas:  # Letras incorretas
            incorretas += letra + ' '
            contador += 1

    print('Palavra Secreta:', palavra_formatada)
    print('Tentativas incorretas:', contador)  # Print de tentativas
    print(f'Faltam {10 - contador} tentativas')
    print('Letras incorretas:', incorretas)

    if '*' not in palavra_formatada:  # Jogador venceu
        print('\n --- VOCÊ VENCEU ---')
        print(f'A palavra secreta era: {PALAVRA_SECRETA}')
        break

    if contador == 10:  # Game Over
        print('\n --- GAME OVER ---')
        print('Você não adivinhou a palavra.')
        print('Tente novamente.')
        break
