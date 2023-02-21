import numpy as np
import matplotlib.pyplot as plt


def resolve_predator_prey(a, b, c, d, x0, y0, t0, tf, dt):
    # Define as funções que descrevem o sistema
    def f(t, x, y):
        return a*x - b*x*y, d*x*y - c*y

    # Define os parâmetros do método do trapézio
    n = int((tf - t0) / dt) + 1

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
        x_inter = x[i-1] + dt/2 * f(t[i-1], x[i-1], y[i-1])[0]
        y_inter = y[i-1] + dt/2 * f(t[i-1], x[i-1], y[i-1])[1]

        # Define os valores de x e y no próximo passo
        x[i] = x[i-1] + dt * f(t[i-1] + dt/2, x_inter, y_inter)[0]
        y[i] = y[i-1] + dt * f(t[i-1] + dt/2, x_inter, y_inter)[1]

    # Plota a solução
    fig, ax = plt.subplots()
    ax.plot(t, x, label='Presas')
    ax.plot(t, y, label='Predadores')
    ax.set_xlabel('Tempo')
    ax.set_ylabel('População')
    ax.legend()
    plt.show()

    # Calcula a ordem de convergência e a estimativa do erro
    erro = []
    ordem = []
    for i in range(-1, n-1):
        h = t[i+1] - t[i]
        x1 = x[i-1]
        x2 = x[i]
        x3 = x[i+1]
        y1 = y[i-1]
        y2 = y[i]
        y3 = y[i+1]
        ordem.append(np.log((x3 - x2)/(x2 - x1))/np.log(h))
        erro.append((x3 - x2)/(2**ordem[-1] - 1))

    print("Tabela de convergência do método do trapézio para o oscilador de Van Der Pol")
    print("------------------------------------------------------------------------")
    print("{:^10} | {:^10} | {:^10}".format(
        "Tempo", "Ordem de Convergência", "Estimativa do Erro"))
    print("{:-^10} |       {:-^10}      | {:-^10}".format("", "", ""))
    for i in range(n):
        print("{:^10.2f} |       {:^10.6f}      | {:^10.6f}".format(
            t[i], ordem[i], erro[i]))


