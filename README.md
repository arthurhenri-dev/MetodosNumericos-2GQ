# Métodos Numéricos — Planejamento de Capacidade de Servidores

> Projeto desenvolvido para a disciplina de **Métodos Numéricos**.

Este projeto tem como objetivo analisar o crescimento do armazenamento de dados de uma infraestrutura de servidores, utilizando métodos numéricos para ajustar uma função matemática, estimar valores intermediários e prever quando a capacidade disponível será ultrapassada.

Foram implementados e utilizados três métodos numéricos:

- 🔹 Eliminação de Gauss com pivoteamento parcial
- 🔹 Ajuste Polinomial pelo Método dos Mínimos Quadrados
- 🔹 Interpolação de Lagrange

O objetivo é utilizar os dados históricos de armazenamento para construir um modelo de crescimento, realizar previsões e auxiliar no planejamento de futuras expansões da infraestrutura.

---

# 1. Objetivo do projeto

Analisar a evolução do armazenamento utilizado em uma infraestrutura de servidores ao longo de 12 meses e utilizar métodos numéricos para estimar seu crescimento futuro.

A partir dos dados disponíveis, o projeto busca:

- Identificar o comportamento do crescimento do armazenamento.
- Construir um modelo matemático que represente os dados observados.
- Estimar o armazenamento em períodos intermediários.
- Prever quando a capacidade atual será ultrapassada.
- Comparar diferentes cenários de expansão de capacidade.

---

# 2. Descrição do problema

Uma infraestrutura de servidores possui capacidade atual de armazenamento de **600 TB**.

Durante 12 meses, foram registrados os seguintes valores de utilização:

| Mês | Armazenamento (TB) |
|---:|---:|
| 1 | 137,99 |
| 2 | 150,45 |
| 3 | 172,59 |
| 4 | 199,09 |
| 5 | 219,06 |
| 6 | 250,06 |
| 7 | 292,32 |
| 8 | 328,07 |
| 9 | 366,12 |
| 10 | 417,17 |
| 11 | 464,15 |
| 12 | 519,14 |

Com base nesses registros, o problema consiste em analisar o crescimento da utilização e estimar em quais meses a infraestrutura precisará de uma expansão.

Foram consideradas três possibilidades:

| Plano | Expansão | Capacidade total |
|---|---:|---:|
| Plano A | +100 TB | 700 TB |
| Plano B | +200 TB | 800 TB |
| Plano C | +300 TB | 900 TB |

O objetivo é comparar esses cenários e identificar qual deles oferece maior capacidade para atender à demanda futura.

---

# 3. Métodos numéricos utilizados

## 3.1 Eliminação de Gauss

O método da Eliminação de Gauss é utilizado para resolver sistemas de equações lineares.

O procedimento consiste em transformar a matriz do sistema em uma matriz triangular superior, utilizando operações elementares entre linhas.

Depois da triangularização, é possível encontrar as incógnitas por meio da substituição retroativa.

Neste projeto, foi implementado o pivoteamento parcial, que seleciona o maior elemento em módulo da coluna atual para ser utilizado como pivô.

### Etapas do método

1. Selecionar o pivô da coluna atual.
2. Realizar a troca de linhas, quando necessário.
3. Eliminar os elementos abaixo do pivô.
4. Repetir o procedimento até obter uma matriz triangular superior.
5. Aplicar a substituição retroativa para encontrar a solução.

### ✅ Vantagens

- Permite resolver sistemas de equações lineares.
- O pivoteamento parcial melhora a estabilidade numérica.
- Pode ser utilizado como etapa auxiliar de outros métodos.

### ❌ Desvantagem

- Pode apresentar dificuldades quando o sistema é singular ou possui pivôs muito próximos de zero.

### Aplicação no projeto

A Eliminação de Gauss foi utilizada internamente pelo método dos Mínimos Quadrados para resolver o sistema de equações normais gerado durante o ajuste polinomial.

---

## 3.2 Método dos Mínimos Quadrados

O Método dos Mínimos Quadrados é utilizado para encontrar uma função que represente, da melhor maneira possível, um conjunto de dados observados.

Neste projeto, foi escolhido um polinômio de segundo grau para representar o crescimento do armazenamento:

$$
P(m) = am^2+bm+c
$$

Onde:

- \(m\) representa o mês.
- \(a\), \(b\) e \(c\) são os coeficientes do polinômio.

A ideia é encontrar os coeficientes que produzam a menor soma dos quadrados das diferenças entre os valores reais e os valores estimados pela função.

Para isso, são montadas as equações normais:

\[
(A^T A)c=A^T y
\]

O sistema resultante é resolvido utilizando a Eliminação de Gauss implementada pela equipe.

### Resultado do ajuste

O polinômio encontrado foi:

$$
p(m)=125,14568182+9,92926823m+1,90765984m^2
$$

O coeficiente de determinação obtido foi aproximadamente:

\[
R^2=0,999574
\]

Esse resultado indica que o polinômio apresenta um ajuste muito próximo dos dados observados.

### ✅ Vantagens

- Permite representar tendências de crescimento.
- Utiliza todos os pontos disponíveis no ajuste.
- Pode ser utilizado para realizar estimativas futuras.

### ❌ Desvantagem

- A escolha inadequada do grau do polinômio pode produzir um ajuste pouco representativo.
- Previsões muito distantes dos dados observados podem apresentar erros.

---

## 3.3 Interpolação de Lagrange

A Interpolação de Lagrange permite encontrar um polinômio que passa exatamente pelos pontos fornecidos.

Diferentemente dos Mínimos Quadrados, que busca o melhor ajuste geral, a interpolação utiliza os pontos selecionados para construir uma função que reproduz exatamente seus valores.

A expressão geral é:

\[
P(x)=\sum_{i=0}^{n}y_iL_i(x)
\]

Onde cada \(L_i(x)\) representa um polinômio fundamental de Lagrange.

### Aplicação no projeto

Foi utilizada a interpolação com os dados dos meses 4, 5 e 6 para estimar o armazenamento no mês 5,5.

Os valores utilizados foram:

| Mês | Armazenamento (TB) |
|---:|---:|
| 4 | 199,09 |
| 5 | 219,06 |
| 6 | 250,06 |

O resultado obtido foi aproximadamente:

\[
\boxed{P(5,5)\approx233,18\text{ TB}}
\]

### ✅ Vantagens

- Passa exatamente pelos pontos selecionados.
- Permite estimar valores entre os dados conhecidos.
- Não exige que os pontos sigam uma função previamente definida.

### ❌ Desvantagem

- A escolha dos pontos influencia diretamente o resultado.
- A interpolação pode apresentar resultados pouco representativos fora do intervalo dos pontos utilizados.

---

# 4. Análise estatística dos dados

Antes da aplicação dos métodos numéricos, foram realizadas análises estatísticas para compreender o comportamento dos dados.

| Indicador | Resultado |
|---|---:|
| Média | 293,02 TB |
| Desvio padrão | 126,99 TB |
| Mínimo | 137,99 TB |
| Mediana | 271,19 TB |
| Máximo | 519,14 TB |
| Crescimento total | 381,15 TB |
| Crescimento percentual | 276,22% |

Os dados demonstram um crescimento contínuo da utilização do armazenamento durante os 12 meses analisados.

O aumento de aproximadamente 276,22% em relação ao primeiro mês evidencia a necessidade de planejamento para futuras expansões.

---

# 5. Previsão do crescimento

Após a obtenção do polinômio pelo Método dos Mínimos Quadrados, foi possível estimar o armazenamento para os meses seguintes.

O modelo encontrado foi:

\[
p(m)=125,14568182+9,92926823m+1,90765984m^2
\]

A primeira previsão foi realizada para o mês 13:

\[
\boxed{p(13)\approx576,62\text{ TB}}
\]

Esse resultado indica que a utilização continuará crescendo e se aproximará da capacidade atual de 600 TB.

De acordo com o modelo, a capacidade atual será ultrapassada no mês 14, quando a previsão é de aproximadamente 638,06 TB.

---

# 6. Comparação dos planos de expansão

Utilizando o polinômio obtido pelo Método dos Mínimos Quadrados, foram analisados os três cenários de expansão.

| Cenário | Capacidade total | Primeiro mês acima da capacidade | Armazenamento previsto |
|---|---:|---:|---:|
| Atual | 600 TB | 14 | 638,06 TB |
| Plano A | 700 TB | 15 | 703,31 TB |
| Plano B | 800 TB | 17 | 845,26 TB |
| Plano C | 900 TB | 18 | 921,95 TB |

### Análise dos resultados

- **Capacidade atual (600 TB):** será ultrapassada no mês 14.
- **Plano A (700 TB):** será ultrapassado no mês 15.
- **Plano B (800 TB):** será ultrapassado no mês 17.
- **Plano C (900 TB):** será ultrapassado no mês 18.

Os resultados demonstram que os planos de expansão aumentam o tempo disponível antes de a infraestrutura atingir novamente seu limite.

Entretanto, mesmo a maior expansão analisada não impede que a capacidade seja ultrapassada posteriormente, considerando a continuidade do crescimento estimado pelo modelo.

---

# 7. Implementação computacional

O projeto foi desenvolvido em Python, utilizando módulos separados para organizar os métodos numéricos implementados pela equipe.

A estrutura permite reutilizar os métodos em diferentes partes do projeto, mantendo a organização do código.

## 7.1 Eliminação de Gauss

Trecho da implementação:

```python
def gauss(A, b):
    n = len(A)

    A = [linha[:] for linha in A]
    b = b[:]

    for k in range(n - 1):
        p = max(range(k, n), key=lambda i: abs(A[i][k]))

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
```

A função realiza a triangularização do sistema utilizando pivoteamento parcial.

A solução é obtida posteriormente pela função de substituição retroativa.

## 7.2 Método dos Mínimos Quadrados

Trecho da implementação:

```python
def ajuste_polinomial_minimos_quadrados(x, y, grau=2):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    V = np.vander(x, N=grau + 1, increasing=True)

    # Montagem das equações normais
    A = V.T @ V
    b = V.T @ y

    # Resolução pelo método de Gauss
    A_triangular, b_modificado = gauss(A, b)
    coeficientes = sistema_triangular(
        A_triangular, b_modificado
    )

    return coeficientes
```

A função monta a matriz de Vandermonde, constrói as equações normais e utiliza a Eliminação de Gauss para encontrar os coeficientes do polinômio.

## 7.3 Interpolação de Lagrange

Trecho da implementação:

```python
def interpolacao_lagrange(x, y, ponto):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    resultado = 0.0

    for i in range(len(x)):
        termo = y[i]

        for j in range(len(x)):
            if i != j:
                termo *= (
                    (ponto - x[j]) / (x[i] - x[j])
                )

        resultado += termo

    return float(resultado)
```

A função calcula o polinômio interpolador utilizando os pontos fornecidos e retorna o valor estimado para o ponto solicitado.

---

# 8. Estrutura do projeto

O projeto foi organizado em diretórios para separar os métodos numéricos, os dados e o notebook utilizado na análise.

```text
metodos_numericos/
│
├── metodos/
│   ├── __init__.py
│   ├── gauss.py
│   ├── min_quadrados.py
│   └── lagrange.py
│
├── dados/
│   └── armazenamento.csv
│
├── notebook/
│   └── problema3.ipynb
│
├── pyproject.toml
└── README.md
```

### Descrição dos arquivos

| Arquivo | Responsabilidade |
|---|---|
| `gauss.py` | Implementação da Eliminação de Gauss e substituição retroativa. |
| `min_quadrados.py` | Implementação do ajuste polinomial pelos Mínimos Quadrados. |
| `lagrange.py` | Implementação da Interpolação de Lagrange. |
| `armazenamento.csv` | Dados históricos de utilização do armazenamento. |
| `problema3.ipynb` | Análises, gráficos, cálculos e apresentação dos resultados. |
| `pyproject.toml` | Configuração do projeto e declaração das dependências. |

---

# 9. Bibliotecas utilizadas

| Biblioteca | Utilidade |
|---|---|
| `NumPy` | Operações matemáticas e manipulação de vetores e matrizes. |
| `Pandas` | Leitura, organização e análise dos dados. |
| `Matplotlib` | Construção de gráficos e visualização dos resultados. |
| `Jupyter Notebook` | Execução documentada do código e apresentação das análises. |

---

# 10. Pré-requisitos

Para executar o projeto, são necessários:

- Python 3.10 ou superior.
- Git.
- Jupyter Notebook.
- Bibliotecas NumPy, Pandas e Matplotlib.

---

# 11. Instalação e execução

## Clonando o repositório

No terminal, execute:

```bash
git clone https://github.com/arthurhenri-dev/MetodosNumericos-2GQ.git
```

Entre na pasta do projeto:

```bash
cd MetodosNumericos-2GQ
```

## Instalando as dependências

Com o Python e o pip instalados, execute:

```bash
pip install -e ".[dev]"
```

Esse comando instala o projeto em modo editável e também as dependências adicionais de desenvolvimento declaradas no `pyproject.toml`.

## Executando o notebook

Inicie o Jupyter Notebook:

```bash
jupyter notebook
```

Abra o arquivo `notebook/problema3.ipynb` e execute as células em sequência.

---

# 12. Conclusão

A aplicação dos métodos numéricos permitiu analisar o crescimento do armazenamento e construir estimativas para auxiliar no planejamento da capacidade dos servidores.

O Método dos Mínimos Quadrados foi utilizado para construir um modelo polinomial de segundo grau, apresentando um coeficiente de determinação de aproximadamente 0,999574.

A Interpolação de Lagrange permitiu estimar valores intermediários entre os meses analisados, enquanto a Eliminação de Gauss foi utilizada para resolver o sistema de equações normais necessário ao ajuste polinomial.

A partir das previsões, observou-se que:

- A capacidade atual de 600 TB será ultrapassada no mês 14.
- O Plano A, com 700 TB, será ultrapassado no mês 15.
- O Plano B, com 800 TB, será ultrapassado no mês 17.
- O Plano C, com 900 TB, será ultrapassado no mês 18.

Dessa forma, o projeto demonstra como os métodos numéricos podem ser aplicados a um problema prático de planejamento de infraestrutura, permitindo analisar tendências, realizar previsões e comparar cenários de expansão.

É importante destacar que as previsões dependem do comportamento representado pelos dados históricos e não garantem que o crescimento real seguirá exatamente o modelo matemático encontrado.

---

# 13. Equipe de alunos

- Anderson Rodrigues
- Arthur Henrique
- José Everton
- Kelly Acioli
- Ronald Chaves

---

# 14. Professor

**Paulo Rocha**

### Disciplina

**Métodos Numéricos**

---

# 15. Referências

RUGGIERO, Márcia A. Gomes; LOPES, Vera Lúcia da Rocha. *Cálculo numérico: aspectos teóricos e computacionais*. 2. ed. São Paulo: Pearson Makron Books, 1996.

Métodos numéricos e computacionais na prática de engenharias e ciências / Reyolando M. L. R. F. Brasil, José Manoel Balthazar, Wesley Góis. – São Paulo: Blucher, 2015. 

Material didático da disciplina de Métodos Numéricos disponibilizado pelo professor.
