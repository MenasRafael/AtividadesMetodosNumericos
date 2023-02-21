import numpy as np
import matplotlib.pyplot as plt


def f(t, x, y, mu, omega):
    return y, mu * (1 - x ** 2) * y - omega ** 2 * x


def resolve_VanDerPol():
    # Define as constantes do sistema
    mu = 1.5
    omega = 1

    # Define as condições iniciais
    x0 = 1
    y0 = 0

    # Define os parâmetros do método do trapézio
    t0 = 0
    tf = 20
    h = 0.1
    n = int((tf - t0) / h) + 1

    # Define as funções que descrevem o sistema

    # Inicializa os arrays de solução
    t = np.linspace(t0, tf, n)
    x = np.zeros(n)
    y = np.zeros(n)

    # Define as condições iniciais
    x[0] = x0
    y[0] = y0

    # Usa o método do trapézio para calcular a solução
    for i in range(1, n):
        # Define os valores intermediários
        x_inter = x[i-1] + h/2 * f(t[i-1], x[i-1], y[i-1], mu, omega)[0]
        y_inter = y[i-1] + h/2 * f(t[i-1], x[i-1], y[i-1], mu, omega)[1]

        # Define os valores de x e y no próximo passo
        x[i] = x[i-1] + h * f(t[i-1] + h/2, x_inter, y_inter, mu, omega)[0]
        y[i] = y[i-1] + h * f(t[i-1] + h/2, x_inter, y_inter, mu, omega)[1]

    # Plota a solução
    fig, ax = plt.subplots()
    ax.plot(t, x, label='x')
    ax.plot(t, y, label='y')
    ax.set_xlabel('Tempo')
    ax.set_ylabel('Posição')
    ax.legend()
    plt.show()

    construct_table(n, x, h, mu, t)


def construct_table(n, x, h, mu, t):
    # Calcula a ordem de convergência e a estimativa do erro
    erro = np.zeros(n)
    for i in range(2, n):
        erro[i] = abs((x[i] - x[i-1]) / (1 - 0.5 * h * mu * (1 - x[i-1] ** 2)))
    erro[0:2] = np.nan

    ordem_conv = np.zeros(n)
    for i in range(3, n):
        ordem_conv[i] = np.log2(abs((x[i] - x[i-1]) / (x[i-1] - x[i-2])))
    ordem_conv[0:3] = np.nan

    # Imprime a tabela
    print("Tabela de convergência do método do trapézio para o oscilador de Van Der Pol")
    print("------------------------------------------------------------------------")
    print("{:^10} | {:^10} | {:^10}".format(
        "Tempo", "Ordem de Convergência", "Estimativa do Erro"))
    print("{:-^10} |       {:-^10}      | {:-^10}".format("", "", ""))
    for i in range(n):
        print("{:^10.2f} |       {:^10.6f}      | {:^10.6f}".format(
            t[i], ordem_conv[i], erro[i]))