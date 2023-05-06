from my_mat_util import imprimir_matriz, entrada_1_matriz, ler_matriz, ler_dimensao
from my_mat_functions import multiplica_matrizes, encontrar_maior_valor, encontrar_menor_valor, matriz_identidade, \
    determinante_4x4, determinante_3x3, somar_dois_valores, transposta, multiplicacao_aux, inversa, soma_todos, \
    ler_numero


def log():
    print(
        '\nEscolha uma opção (0 a 8): \n0-sair \n1-identidade \n2-multiplicacao de matrizes \n3-transposta \n4-multiplicacao por escalar \n5-Mostrar maior, menor ou/e soma \n6-determinante(3x3) \n7-determinante(4x4) \n8-matriz inversa(3x3 ou 4x4)')
    user = input()
    try:
        user = int(user)
        return user
    except ValueError:
        if user.strip() == '':
            print('\nNenhuma entrada fornecida. Saindo do programa.')
            return 0
        else:
            print('\nEntrada inválida')
            resposta = input('\nEscolha: 1-Voltar para o menu principal Qualquer outra tecla-Sair do Programa')
            if resposta == '1':
                return log()
            else:
                return 0


def func(digito):
    usuario = int(digito)
    if usuario == 0:
        print('\nO programa foi encerrado :)')
        return

    elif int(usuario) in (1, 2, 3, 4, 5, 6, 7, 8):

        if int(usuario) == 1:
            matriza = entrada_1_matriz()
            identidade = matriz_identidade(matriza)
            print('\nmatriz Identidade:')
            imprimir_matriz(identidade)

        elif int(usuario) == 2:
            print('\nPreencha a dimensao da primeira matriz:')
            dimensao_a = ler_dimensao('matriza')
            print('\nPreencha a dimensao da segunda matriz:')
            dimensao_b = ler_dimensao('matrizb')
            ca = dimensao_a[1]
            lb = dimensao_b[0]
            if ca != lb:
                print("As matrizes não são multiplicáveis.")
                resposta = input('\nEscolha: 1-Voltar para o menu principal Qualquer outra tecla-Sair do Programa')
                if int(resposta) == 1:
                    func(log())
                else:
                    print('\nO programa foi encerrado :)')
                    return

            else:

                print('\nDigite os valores matriz 1:')
                matriza = ler_matriz('matriz', dimensao_a[0], dimensao_a[1])
                print('\nmatriz digitada:')
                imprimir_matriz(matriza)
                print('\nDigite os valores matriz 2:')
                matrizb = ler_matriz('matriz', dimensao_b[0], dimensao_b[1])
                print('\nmatriz digitada:')
                imprimir_matriz(matrizb)
                mr = multiplica_matrizes(matriza, matrizb)
                print('\nmatriz resultante:')
                imprimir_matriz(mr)



        elif int(usuario) == 3:
            matriza = entrada_1_matriz()
            matrizr = transposta(matriza)
            print('\nmatriz Transposta:')
            imprimir_matriz(matrizr)


        elif int(usuario) == 4:
            matriza = entrada_1_matriz()
            x = ler_numero()
            matrizr = multiplicacao_aux(matriza, x)
            print('\nmatriz Resultante:')
            imprimir_matriz(matrizr)



        elif int(usuario) == 5:

            matriza = entrada_1_matriz()

            print(
                '\nEscolha uma opção: 1-Mostrar maior valor, 2-Mostrar menor valor ,3-somar dois valores, 4-somar todos os valores e 5- executar todos os anteriores.')
            opcao = int(input())

            if opcao == 1:
                maior_valor = encontrar_maior_valor(matriza)
                print(f'\nO maior valor é: {maior_valor}')

            elif opcao == 2:
                menor_valor = encontrar_menor_valor(matriza)
                print(f'\nO menor valor é: {menor_valor}')

            elif opcao == 3:
                print('\nEscolha as posições (linha e coluna) para somar em cada matriz:')
                linha1 = int(input('\nDigite a linha da primeira matriz:'))
                coluna1 = int(input('\nDigite a coluna da primeira matriz: '))
                linha2 = int(input('\nDigite a linha da segunda matriz:'))
                coluna2 = int(input('\nDigite a coluna da segunda matriz: '))
                soma = somar_dois_valores(matriza, linha1, coluna1, linha2, coluna2)
                print(f'\nA soma dos valores é: {soma}')
            elif opcao == 4:
                soma = soma_todos(matriza)
                print(f'\nA soma de todos os elementos é: {soma}')
            elif opcao == 5:
                maior_valor = encontrar_maior_valor(matriza)
                menor_valor = encontrar_menor_valor(matriza)
                print('\nEscolha as posições (linha e coluna) para somar em cada matriz:')
                linha1 = int(input('\nDigite a linha da primeira matriz:'))
                coluna1 = int(input('\nDigite a coluna da primeira matriz:'))
                linha2 = int(input('\nDigite a linha da segunda matriz:'))
                coluna2 = int(input('\nDigite a coluna da segunda matriz: '))
                soma1 = somar_dois_valores(matriza, linha1, coluna1, linha2, coluna2)
                soma2 = soma_todos(matriza)
                print(f'\nA soma de todos os elementos é: {soma2}')
                print(f'\nO maior valor é: {maior_valor}')
                print(f'\nO menor valor é: {menor_valor}')
                print(f'\nA soma dos dois valores é: {soma1}')
                print(f'\nA soma de todos os elementos é: {soma2}')

            else:
                print('\nOpção inválida!')
                print('\nResposta Inválida :(')
                resposta = input('\nEscolha: 1-Voltar para o menu principal -Sair do programa(qualquer outra tecla)')
                if int(resposta) == 1:
                    func(3)
                else:
                    print('\nO programa foi encerrado :)')
                    return




        elif int(usuario) == 6:
            print('\nDigite os valores matriz:')
            matriza = ler_matriz('matriz', int(3), int(3))
            print('\nmatriz digitada:')
            imprimir_matriz(matriza)
            determinante = determinante_3x3(matriza)
            print(f'\nDeterminante= {determinante}')



        elif int(usuario) == 7:
            print('\nDigite os valores matriz:')
            matriza = ler_matriz('matriz', int(4), int(4))
            print('\nmatriz digitada:')
            imprimir_matriz(matriza)
            determinante = determinante_4x4(matriza)
            print(f'\nDeterminante= {determinante}')

        elif int(usuario) == 8:
            matriza = entrada_1_matriz()
            matriz_i = inversa(matriza)
            if matriz_i is None:
                print("A matriz não é invertível.")
            else:
                print('\nMatriz Inversa:')
                imprimir_matriz(matriz_i)
            input("Pressione enter para continuar...")
            log()


        else:
            print('\nEntrada inválida')
            resposta = input('\nEscolha: 1-Voltar para o menu principal Qualquer outra tecla-Sair do Programa')
            if int(resposta) == 1:
                func(log())
            else:
                print('\nO programa foi encerrado :)')
                return
