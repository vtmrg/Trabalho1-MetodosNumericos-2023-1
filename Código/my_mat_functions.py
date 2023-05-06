# modulo my_mat_functions
# funcoes de apoio para manipulação e aritmética matricial
# cria e retorna uma matriz (linhas x colunas) com conteúdo celula (ou zero por default)

"""funcoes pelo Professor em Aula:
"""


def criar_matriz(linhas, colunas, celula=0):
    m = [0] * linhas
    for i in range(len(m)):
        m[i] = [celula] * colunas
    return m


# cria e retorna uma matriz identidade
def criar_identidade(dimensao):
    m = criar_matriz(dimensao, dimensao)
    # for para colocar 1 na diagonal principal
    for linha in range(dimensao):
        m[linha][linha] = 1
    return m


# multiplica duas matrizes e retorna uma matriz resultado
def multiplica_matrizes(ma, mb):
    la = len(ma)
    ca = len(ma[0])
    cb = len(mb[0])
    mr = criar_matriz(la, cb)
    for i in range(la):
        for j in range(cb):
            for k in range(ca):
                mr[i][j] = mr[i][j] + ma[i][k] * mb[k][j]
    return mr


'''funcoes criadas por mim:
'''


def encontrar_maior_valor(matrizes):
    """
        Retorna o maior valor presente em uma matriz.

        Argumentos:
        matriz: list[list]

        Retorna:
        int ou float: o maior valor presente na matriz.
        """
    max_valor = float('-inf')
    for linha in matrizes:
        for valor in linha:
            if valor > max_valor:
                max_valor = valor
    return max_valor


def encontrar_menor_valor(matrizes):
    """
    Retorna o menor valor presente em uma matriz.

    Argumentos:
    matriz: list[list]

    Retorna:
    int ou float: o menor valor presente na matriz.
    """
    min_valor = float('inf')
    for linha in matrizes:
        for valor in linha:
            if valor < min_valor:
                min_valor = valor
    return min_valor


def somar_dois_valores(matriz, linha1, coluna1, linha2, coluna2):
    dimensoes = (len(matriz), len(matriz[0]))

    try:
        if not (0 <= linha1 < dimensoes[0] and 0 <= coluna1 < dimensoes[1]):
            raise ValueError(
                f"Valor inválido para a posição (linha, coluna) da primeira matriz: ({linha1}, {coluna1}), a dimensão da matriz é: ({dimensoes[0]}, {dimensoes[1]})")

        if not (0 <= linha2 < dimensoes[0] and 0 <= coluna2 < dimensoes[1]):
            raise ValueError(
                f"Valor inválido para a posição (linha, coluna) da segunda matriz: ({linha2}, {coluna2}), a dimensão da matriz é: ({dimensoes[0]}, {dimensoes[1]})")

        valor1 = matriz[linha1][coluna1]
        valor2 = matriz[linha2][coluna2]
        soma = valor1 + valor2
        return soma
    except ValueError as err:
        print(f"Erro: {err}")


def soma_todos(matriz):
    """
    Retorna a soma de todos os elementos de uma matriz.

    Argumentos:
    matriz: list[list]

    Retorna:
    int ou float: soma de todos os elementos da matriz.
    """
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    return soma


def matriz_identidade(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    if linhas != colunas:
        raise ValueError("A matriz não é quadrada.")

    identidade = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)
        identidade.append(linha)

    return identidade


def multiplicacao_escalar(matriz):
    """
    Lê um número do usuário e multiplica cada elemento de uma matriz por esse número,
    e retorna a matriz resultante.
    """
    n = ler_numero()
    # Inicializa a matriz resultante com zeros
    matrizC = [[0 for _ in range(len(matriz[0]))] for _ in range(len(matriz))]

    # Multiplica cada elemento da matriz pelo número
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matrizC[i][j] = matriz[i][j] * float(n)

    return matrizC


def transposta(matriz):
    """
    Retorna a matriz transposta de uma matriz dada.
    """
    # Inicializa a matriz transposta com zeros, trocando as dimensões da matriz original
    matrizT = [[0 for _ in range(len(matriz))] for _ in range(len(matriz[0]))]

    # Preenche a matriz transposta com os elementos da matriz original trocando as posições das linhas e colunas
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matrizT[j][i] = matriz[i][j]

    return matrizT


def determinante_3x3(matriz):
    """
    Retorna o determinante de uma matriz 3x3 dada.
    """
    # Verifica se a matriz é 3x3
    if len(matriz) != 3 or len(matriz[0]) != 3:
        raise ValueError("A matriz deve ser 3x3.")

    # Calcula o determinante usando a fórmula de Sarrus
    det = matriz[0][0] * matriz[1][1] * matriz[2][2] + matriz[1][0] * matriz[2][1] * matriz[0][2] + matriz[2][0] * \
          matriz[0][1] * matriz[1][2] - matriz[2][0] * matriz[1][1] * matriz[0][2] - matriz[0][0] * matriz[2][1] * \
          matriz[1][2] - matriz[1][0] * matriz[0][1] * matriz[2][2]

    return det


'''
def determinante_2x2(matriz):
    """
    Retorna o determinante de uma matriz 2x2.
    """
    if len(matriz) != 2 or len(matriz[0]) != 2:
        raise ValueError("A matriz deve ser 2x2.")
    det=matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    return det
'''


def determinante_4x4(matrix):
    """
    Retorna o determinante de uma matriz 4x4 dada.
    """
    # Verifica se a matriz é 4x4
    if len(matrix) != 4 or len(matrix[0]) != 4:
        raise ValueError("A matriz deve ser 4x4.")

    # Calcula o determinante usando a regra de Sarrus para as primeiras três colunas
    sub_det_1 = matrix[0][0] * matrix[1][1] * matrix[2][2] * matrix[3][3] + matrix[0][1] * matrix[1][2] * matrix[2][3] * \
                matrix[3][0] + matrix[0][2] * matrix[1][3] * matrix[2][0] * matrix[3][1] + matrix[0][3] * matrix[1][0] * \
                matrix[2][1] * matrix[3][2] - matrix[0][3] * matrix[1][2] * matrix[2][1] * matrix[3][0] - matrix[0][2] * \
                matrix[1][1] * matrix[2][3] * matrix[3][0] - matrix[0][1] * matrix[1][0] * matrix[2][2] * matrix[3][3] - \
                matrix[0][0] * matrix[1][3] * matrix[2][1] * matrix[3][2]

    # Calcula o determinante usando a expansão por cofatores da primeira coluna
    sub_det_2 = matrix[1][0] * ((matrix[2][1] * matrix[3][2] * matrix[0][3] + matrix[3][1] * matrix[0][2] * matrix[2][
        3] + matrix[0][1] * matrix[2][2] * matrix[3][3]) - (
                                        matrix[2][3] * matrix[3][2] * matrix[0][1] + matrix[3][3] * matrix[0][2] *
                                        matrix[2][1] + matrix[0][3] * matrix[2][2] * matrix[3][1]))
    sub_det_3 = matrix[2][0] * ((matrix[0][1] * matrix[1][2] * matrix[3][3] + matrix[1][1] * matrix[3][2] * matrix[0][
        3] + matrix[3][1] * matrix[0][2] * matrix[1][3]) - (
                                        matrix[0][3] * matrix[1][2] * matrix[3][1] + matrix[1][3] * matrix[3][2] *
                                        matrix[0][1] + matrix[3][3] * matrix[0][2] * matrix[1][1]))
    sub_det_4 = matrix[3][0] * ((matrix[0][1] * matrix[2][2] * matrix[1][3] + matrix[1][1] * matrix[0][2] * matrix[2][
        3] + matrix[2][1] * matrix[1][2] * matrix[0][3]) - (
                                        matrix[0][3] * matrix[2][2] * matrix[1][1] + matrix[1][3] * matrix[0][2] *
                                        matrix[2][1] + matrix[2][3] * matrix[1][2] * matrix[0][1]))

    # Soma os determinantes parciais
    det = sub_det_1 - sub_det_2 + sub_det_3 - sub_det_4

    return det


def multiplicacao_aux(matriz, number):
    """
    Multiplica cada elemento de uma matriz por um número e retorna a matriz resultante.
    """
    # Inicializa a matriz resultante com zeros
    matrizC = [[0 for _ in range(len(matriz[0]))] for _ in range(len(matriz))]

    # Multiplica cada elemento da matriz pelo número
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matrizC[i][j] = matriz[i][j] * number

    return matrizC


def determinante_2x2(matriz):
    """
    Retorna o determinante de uma matriz 2x2.
    """
    if len(matriz) != 2 or len(matriz[0]) != 2:
        raise ValueError("A matriz deve ser 2x2.")

    return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]


def adjunta(matriz):
    """
    Retorna a adjunta da matriz passada como argumento.
    """
    n_linhas = len(matriz)
    n_colunas = len(matriz[0])

    if n_linhas != n_colunas:
        raise ValueError("A matriz deve ser quadrada.")

    if n_linhas == 2:
        return [[matriz[1][1], -matriz[0][1]], [-matriz[1][0], matriz[0][0]]]

    adj = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            submatriz = []
            for k in range(n_linhas):
                if k != i:
                    sublinha = []
                    for l1 in range(n_colunas):
                        if l1 != j:
                            sublinha.append(matriz[k][l1])  # Corrigir aqui
                    submatriz.append(sublinha)
            linha.append(determinante_2x2(submatriz))
        adj.append(linha)

    for i in range(n_linhas):
        for j in range(n_colunas):
            adj[i][j] *= (-1) ** (i + j)

    return adj


def cofatores(matriz):
    linhas, colunas = len(matriz), len(matriz[0])
    if linhas != colunas:
        raise ValueError("A matriz de entrada deve ser quadrada.")
    if linhas == 2:
        a, b = matriz[0]
        c, d = matriz[1]
        return [[d, -b], [-c, a]]
    if linhas == 3:
        a, b, c = matriz[0]
        d, e, f = matriz[1]
        g, h, i = matriz[2]
        cofatores = [
            [e*i - f*h, -(d*i - f*g), d*h - e*g],
            [-(b*i - c*h), a*i - c*g, -(a*h - b*g)],
            [b*f - c*e, -(a*f - c*d), a*e - b*d]
        ]
        return cofatores
    raise ValueError("A matriz de entrada deve ser 2x2 ou 3x3.")


def inversa(matriz):
    """
    Retorna a matriz inversa de uma matriz dada.
    """
    try:
        # Verifica o tamanho da matriz
        if len(matriz) == 3:
            # Calcula o determinante da matriz
            det = determinante_3x3(matriz)
            if det == 0:
                return None

            # Calcula a matriz adjunta
            adj = adjunta(matriz)

            # Calcula a matriz inversa
            inv = multiplicacao_aux(adj, 1 / det)

        elif len(matriz) == 4:
            # Calcula o determinante da matriz
            det = determinante_4x4(matriz)
            if det == 0:
                return None

            # Calcula a matriz adjunta
            adj = adjunta(matriz)

            # Calcula a matriz inversa
            inv = multiplicacao_aux(adj, 1 / det)

        else:
            raise ValueError("A matriz deve ser 3x3 ou 4x4.")

        return inv

    except ValueError as error:
        print(f"Ocorreu um erro. {error}")
        return None


def ler_numero():
    while True:
        try:
            number = float(input("\nDigite um número para multiplicar a matriz: "))
            return number
        except ValueError:
            print("Digite um número válido.")



