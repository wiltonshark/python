"""
Continuando os exercícios 98 - Gerar o primeiro dígito de um CPF
e 100 - Gerar o segundo dígito de um CPF
Faça um programa que gere um CPF válido
e que analize se o CPF digitado pelo usuário é válido.
"""
from random import randint
import re

MENU = '[1] Validar CPF\n[2] Gerar CPF válido\n[3] Sair'

while True:
    print(MENU)
    opcao = input('Digite a opção desejada: ')

    if opcao not in ('1', '2', '3'):
        print('Opção inválida')
        continue

    if opcao == '1':
        entrada = input('Digite os 11 dígitos do CPF: ')
        cpf = re.sub(
            r'[^0-9]',
            '',
            entrada
        )

        if len(cpf) != 11:
            print('CPF incorreto')
            continue

        if cpf == cpf[0] * len(cpf):
            print('CPF inválido - dados sequenciais')
            continue

        resultado_digito_1 = 0
        resultado_digito_2 = 0

        contador_regressivo = 10
        for digito_1 in cpf[:9]:  # Cálculo do primeiro dígito
            resultado_digito_1 += int(digito_1) * contador_regressivo
            contador_regressivo -= 1
        digito_1 = resultado_digito_1 * 10 % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        contador_regressivo = 11
        for digito_2 in cpf[:10]:  # Cálculo do segundo dígito
            resultado_digito_2 += int(digito_2) * contador_regressivo
            contador_regressivo -= 1
        digito_2 = resultado_digito_2 * 10 % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        cpf_calculo = f'{cpf[:9]}{digito_1}{digito_2}'
        if cpf == cpf_calculo:
            print('O CPF é válido')
        else:
            print('CPF inválido')

    if opcao == '2':
        # Gera os 9 primeiros dígitos de um CPF
        cpf_random = randint(000000000, 999999999)
        cpf_gerado = str(cpf_random)

        resultado_digito_1 = 0
        resultado_digito_2 = 0

        contador_regressivo = 10
        for digito_1 in cpf_gerado:  # Cálculo do primeiro dígito
            resultado_digito_1 += int(digito_1) * contador_regressivo
            contador_regressivo -= 1
        digito_1 = resultado_digito_1 * 10 % 11
        digito_1 = digito_1 if digito_1 <= 9 else 0

        cpf_gerado += str(digito_1)

        contador_regressivo = 11
        for digito_2 in cpf_gerado:  # Cálculo do segundo dígito
            resultado_digito_2 += int(digito_2) * contador_regressivo
            contador_regressivo -= 1
        digito_2 = resultado_digito_2 * 10 % 11
        digito_2 = digito_2 if digito_2 <= 9 else 0

        cpf_gerado += str(digito_2)

        print('CPF gerado: '  # Imprimindo CPF gerado com pontos e traço
              f'{cpf_gerado[:3]}.'
              f'{cpf_gerado[3:6]}.'
              f'{cpf_gerado[6:9]}-'
              f'{cpf_gerado[9:]}')

    if opcao == '3':
        break
