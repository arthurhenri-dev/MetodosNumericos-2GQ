import numpy as np
from metodos.gauss import gauss, sistema_triangular


def ajuste_polinomial_minimos_quadrados(x, y, grau=2):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if x.ndim != 1 or y.ndim != 1 or len(x) != len(y):
        raise ValueError("x e y devem ser vetores unidimensionais de mesmo tamanho.")

    if grau < 0 or len(x) < grau + 1:
        raise ValueError("Quantidade de dados insuficiente para o grau solicitado.")

    V = np.vander(x, N=grau + 1, increasing=True)

    # Montagem das equações normais
    A = V.T @ V
    b = V.T @ y

    # Resolução pelo método de Gauss
    A_triangular, b_modificado = gauss(A, b)
    coeficientes = sistema_triangular(A_triangular, b_modificado)

    return coeficientes