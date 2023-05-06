# modulo my_mat_util
# funcoes de apoio para interacao com usuário

# imprime matriz com jeitão de matriz
'''funcoes Pelo Professor em aula:
'''
def imprimir_matriz(m):
    for i in range(len(m)):  # total de linhas
        for j in range(len(m[i])):  # total de colunas
            print(f"{m[i][j]} ", end=" ")
        print()

# cria e retorna uma matriz (linhas x colunas) com conteúdo celula (ou zero por default)
def criar_matriz(linhas, colunas, celula=0):
    m = [0] * linhas
    for i in range(len(m)):
        m[i] = [celula] * colunas
    return m

# criar e depois lê uma matriz (linhas x colunas)
def ler_matriz(nome, linhas, colunas):
    print(f"Dados da matriz {nome}:")
    m = criar_matriz(linhas, colunas)
    for i in range(len(m)):
        for j in range(len(m[i])):
            while True:
                try:
                    m[i][j] = float(input(f"   - célula [{i}][{j}]: "))
                    break
                except ValueError:
                    print("Erro: o valor digitado não é um número válido. Tente novamente.")
    return m


# le as dimensões (linha e coluna) e retorna como tupla
def ler_dimensao(nome):
    print(f"Para a {nome}, qual a dimensão?")
    lin = int(input("   - quantidade de linhas: "))
    col = int(input("   - quantidade de colunas: "))
    return lin, col  # retorna uma tupla


'''funcoes criadas por mim:
'''

def entrada_1_matriz():
    dimensao_a = ler_dimensao('matriz')
    print('\nDigite os valores matriz:')
    matriz = ler_matriz('matriz', dimensao_a[0], dimensao_a[1])
    print('\nmatriz digitada:')
    imprimir_matriz(matriz)
    return matriz

def ler_numero():
    while True:
        try:
            number = float(input("\nDigite um número para multiplicar a matriz: "))
            return number
        except ValueError:
            print("Digite um número válido.")





