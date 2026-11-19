def sistema_triangular(A, b):
    n = len(A)
    x = [0] * n

    # Substituição retroativa
    for k in range(n - 1, -1, -1):
        if abs(A[k][k]) < 1e-12:
            raise ValueError("O sistema não possui solução única.")

        s = 0

        for j in range(k + 1, n):
            s += A[k][j] * x[j]

        x[k] = (b[k] - s) / A[k][k]

    return x


def gauss(A, b):
    n = len(A)

    # Cria cópias para não modificar as matrizes originais
    A = [linha[:] for linha in A]
    b = b[:]

    # Eliminação de Gauss
    for k in range(n - 1):

        # Pivoteamento parcial
        p = max(range(k, n), key=lambda i: abs(A[i][k]))

        # Troca as linhas, se necessário
        A[k], A[p] = A[p], A[k]
        b[k], b[p] = b[p], b[k]

        if abs(A[k][k]) < 1e-12:
            raise ValueError("O sistema não possui solução única.")

        for i in range(k + 1, n):
            m = A[i][k] / A[k][k]

            A[i][k] = 0

            for j in range(k + 1, n):
                A[i][j] -= m * A[k][j]

            b[i] -= m * b[k]

    return A, b