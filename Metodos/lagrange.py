import numpy as np

def interpolacao_lagrange(x, y, ponto):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if len(x) != len(y) or len(np.unique(x)) != len(x):
        raise ValueError("Os pontos x devem ser distintos e ter o mesmo tamanho de y.")

    resultado = 0.0

    for i in range(len(x)):
        termo = y[i]

        for j in range(len(x)):
            if i != j:
                termo *= (ponto - x[j]) / (x[i] - x[j])

        resultado += termo

    return float(resultado)