"""
Curso de Python 3 - Udemy
Exercício 90 - Crie uma lista de compas com listas
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar, e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexixtentes na lista
"""
import os
from time import sleep

MENU = ['[1] Listar Itens', '[2] Inserir Itens', '[3] Apagar Itens']
lista = []
lista_enumerada = list(enumerate(lista, start=1))

opcao_int = 0


while True:
    os.system('cls')
    print('---LISTA DE COMPRAS---')
    for i in MENU:
        print(i)

    opcao = input('Digite a sua opção: ')

    if len(opcao) != 1 or not opcao.isnumeric():
        print('Digite apenas um número de opção do Menu')
        sleep(1.5)
        continue
    opcao_int = int(opcao)

    if opcao_int not in range(1, 4):
        print('Menu Inválido')
        sleep(1.5)
        continue

    if opcao_int == 1:
        os.system('cls')
        if lista:
            print('ITENS:')
            for indice, item in lista_enumerada:
                print(indice, item)
            print('\n')
            os.system('pause')
            continue

        print('Lista Vazia')
        sleep(1.5)
        continue

    if opcao_int == 2:
        inserir = ''
        while inserir != 'v':
            os.system('cls')
            print('Digite os itens que deseja adicionar')
            print('Ou [v] para voltar:')
            lista_enumerada = list(enumerate(lista, start=1))
            for indice, item in lista_enumerada:
                print(indice, item)
            inserir = input('Novo Item: ')
            if inserir == 'v':
                continue
            if inserir not in lista:
                lista.append(inserir)

            else:
                print('Item já adicionado')
                continue

    if opcao_int == 3:
        deletar = ''
        os.system('cls')
        while deletar != 'v':
            os.system('cls')
            print('Digite o índice do item que deseja remover')
            print('Ou [v] para voltar:')
            lista_enumerada = list(enumerate(lista, start=1))
            for indice, item in lista_enumerada:
                print(indice, item)
            if lista:
                deletar = input('Remover Item: ')
                if deletar == 'v':
                    continue
                try:
                    if deletar.isnumeric():
                        deletar_int = int(deletar)
                        lista.pop(deletar_int - 1)

                except IndexError:
                    print('Item não encontrado')
                    sleep(1.5)
            else:
                os.system('cls')
                print('Lista Vazia')
                sleep(1.5)
                deletar = 'v'
