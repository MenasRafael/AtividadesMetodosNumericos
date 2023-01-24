# Importacao das bibliotecas que serao utilizadas no projeto
import matplotlib.pyplot as plt
import numpy as np

#QUESTAO 1
def quest1():
    # Valores possiveis para o eixo x 
    # O primeiro valor do paretense representa o valor minimo do grafico
    # O segundo o valor maximo
    # O terceiro representa a definicao do grafico, sendo zero a maior definicao possivel
    x = np.arange(-np.pi, np.pi, 0.0005)

    # Parametros que diferenciam cada uma das funcoes: w, y e z
    m1 = 1
    m2 = 2
    m3 = 3

    # Valores que correspondem as funcoes que serao tracadas
    w = np.cos(m1*x)
    y = np.cos(m2*x)
    z = np.cos(m3*x)
    
    # Tracando o grafico de tres funcoes e colocando as marcacoes que vao diferenciar cada uma delas, incluindo o formato das linhas
    plt.plot(x, w, 'k--', label='m = 1')
    plt.plot(x, y, 'k:', label='m = 2')
    plt.plot(x, z, 'k-.', label='m = 3')

    # Nome do eixo x
    plt.xlabel('x')
    # Nome do eixo y
    plt.ylabel('y')
    
    # Colocando um titulo no gráfico que sera gerado
    plt.title('Gráfico adimensional de y(t) = cos(m*t) para m = 1, 2 e 3')

    # Criando uma legenda para o gráfico e posicionando ela no canto superior esquerdo
    plt.legend(loc='upper left')
    
    # Mostrando o grafico do resultado final
    plt.show()

#QUESTAO 2.1
def quest2_1():
    printFile = 'tabelas/T2.1-Tabela.txt'
    fig, ax = plt.subplots() 

    # Definindo o número de passos minimo
    n = [64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    h = np.zeros(len(n))
    erros = np.zeros(len(n))
    ordemP = np.zeros(len(n))
    
    # Definindo o intervalo a ser utilizado, sendo o modelo do intervalo igual a [a,b]
    a = 0
    b = 1/2
    
    # Definindo o tamanho do passo
    for i in range(len(n)):
        h[i] = (b-a)/n[i]
        
    # Derivada associada a solução exata, solução exata escolhida: y(t) = sin(2π*t)*e^(−0.2)*t
    
    y_inicial = 0 # Valor de y'(t0,y0)
    n_sub = 0
    
    # Aplicação do método de Euler para todos os valores de n 
    for i in range(len(n)):
    # O laço externo serve para alternar entre os diferentes valores de n propostos
        # Reiniciando os valores para um novo valor de tamanho de passo
        t_inicial = 0 # Valor inicial do passo no eixo das abcissas
        y_numerico = y_inicial # Valor inicial do y_numerico na extremidade inferior [a, ...]
        # plt.ylim(0, 0.6)
        # plt.xlim(0, 0.06)
        # Laço interno para calcular o valor do y númerico para cada valor de n
        for j in range(n[i]):
            # y_linha é a derivada obtida pela equação diferencial
            y_linha = 2*np.pi*np.cos(2*np.pi*t_inicial)*np.exp(-0.2*t_inicial)-0.2*(np.sin(2*np.pi*t_inicial)*np.exp(-0.2*t_inicial))
            y_numerico += h[i] * y_linha
            t_inicial += h[i]
            # print(f'dale'+f'{j}')
            if(n[i]==64):
                ax.plot(t_inicial, y_numerico, 'b.')  
            elif(n[i]==256):
                ax.plot(t_inicial, y_numerico, 'k+')  
            elif(n[i]==1024):
                ax.plot(t_inicial, y_numerico, 'g:')  
            elif(n[i]==4096):
                ax.plot(t_inicial, y_numerico, 'r--')  
        t_final = t_inicial
        y_real = np.sin(2*np.pi*t_final)*np.exp(-0.2*t_final)
        erros[i] = np.absolute(y_real - y_numerico)
        
            
    for i in range(len(n)-1):
        ordemP[i+1] = np.log2(erros[i] / erros[i+1]) / np.log2(h[i] / h[i+1])
        
    # Gerando a tabela de convergência númerica para ser utilizada no Latex
    conteudoPrintado = imprimirTabela(n, h, erros, ordemP, printFile)   

    ax.set(xlabel='t(unidade) - variavel independete', ylabel='y(unidade) - variavel de estado', title='Convergência da aproximação')
    plt.title('Aproximação numérica da variável y usando Euler')
    plt.legend(['. n = 64', '+ n = 256', ': n = 1024', '-- n = 4096'],loc='upper left')
    plt.show()                            

#QUESTAO 2.2
def quest2_2():
    printFile = 'tabelas/T2.2-Tabela.txt'

    fig, ax = plt.subplots() 

    # Definindo o número de passos minimo
    n = [64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    h = np.zeros(len(n))
    erros = np.zeros(len(n))
    ordemP = np.zeros(len(n))
    
    # Definindo os valores t para o intervalo a ser utilizado, sendo o modelo do intervalo igual a [a,b]
    a = 0
    b = 1
    
    # Definindo o tamanho do passo
    for i in range(len(n)):
        h[i] = (b-a)/n[i]
        
    # dx/dt = xy
    # dy/dt = y - x^2
    # soluções exatas = x(t) = e^(-t^2/2) e y(t) = t * e^(-t^2/2)
    
    y_inicial = 1 # Valor de y'(t0,y0)
    x_inicial = 1 # Valor de x'(t0,y0)
    
    # Aplicação do método de Euler para todos os valores de n 
    for i in range(len(n)):
    # O laço externo serve para alternar entre os diferentes valores de n propostos
        # Reiniciando os valores para um novo valor de tamanho de passo
        t_inicial = 0 # Valor inicial do passo no eixo das abcissas
        y_numerico = y_inicial # Valor inicial do y_numerico na extremidade inferior [a, ...]
        x_numerico = x_inicial # Valor inicial do x_numerico na extremidade inferior [a, ...]
        
        # Laço interno para calcular o valor do y númerico para cada valor de n
        for j in range(n[i]):
            # y_linha é a derivada obtida pela equação diferencial
            y_linha = -x_numerico
            
            # x_linha é a derivada obtida pela equação diferencial
            x_linha = y_numerico
            
            y_numerico += h[i] * y_linha
            x_numerico += h[i] * x_linha
            
            t_inicial += h[i]

            if(n[i]==64):
                ax.plot(t_inicial, y_numerico, 'b.')  
            elif(n[i]==256):
                ax.plot(t_inicial, y_numerico, 'k+')  
            elif(n[i]==1024):
                ax.plot(t_inicial, y_numerico, 'g:')  
            elif(n[i]==4096):
                ax.plot(t_inicial, y_numerico, 'r--')  
        t_final = t_inicial
        y_real = np.cos(t_final) - np.sin(t_final)
        x_real = np.sin(t_final) + np.cos(t_final)
        
        # Aplicando a norma do máximo para apresentar o erro encontrado
        erros[i] = max(np.absolute(y_real - y_numerico), np.absolute(x_real - x_numerico))
            
    for i in range(len(n)-1):
        ordemP[i+1] = np.log2(erros[i] / erros[i+1]) / np.log2(h[i] / h[i+1])
        
    # Gerando a tabela de convergência númerica para ser utilizada no Latex
    imprimirTabela(n, h, erros, ordemP, printFile)
    ax.set(xlabel='t(unidade) - variavel independete', ylabel='y(unidade) - variavel de estado', title='Convergência da aproximação')
    plt.title('Aproximação numérica da variável y usando Euler')
    plt.legend(['. n = 64', '+ n = 256', ': n = 1024', '-- n = 4096'],loc='upper left')
    plt.show()  

#QUESTAO 2.3
def quest2_3():
    printFile = 'tabelas/T2.3-Tabela.txt'
    fig, ax = plt.subplots() 

     # Definindo o número de passos minimo
    n = [64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    h = np.zeros(len(n))
    erros = np.zeros(len(n))
    ordemP = np.zeros(len(n))
    
    # Definindo os valores t para o intervalo a ser utilizado, sendo o modelo do intervalo igual a [a,b]
    a = 0
    b = 1
    
    # Definindo o tamanho do passo
    for i in range(len(n)):
        h[i] = (b-a)/n[i]
        
    # dx/dt = 3 * x(t) - 4 * y(t)
    # dy/dt = x(t) - y(t)
    # soluções exatas = x(t) = 2*t*e^(t) + e^(t) e y(t) = t*e^(t)
    
    y_inicial = 0 # Valor de y'(t0,y0)
    x_inicial = 1 # Valor de x'(t0,y0)
    
    # Aplicação do método de Euler para todos os valores de n 
    for i in range(len(n)):
    # O laço externo serve para alternar entre os diferentes valores de n propostos
        # Reiniciando os valores para um novo valor de tamanho de passo
        t_inicial = 0 # Valor inicial do passo no eixo das abcissas
        y_numerico = y_inicial # Valor inicial do y_numerico na extremidade inferior [a, ...]
        x_numerico = x_inicial # Valor inicial do x_numerico na extremidade inferior [a, ...]
        
        # Laço interno para calcular o valor do y númerico para cada valor de n
        for j in range(n[i]):
            # y_linha é a derivada obtida pela equação diferencial
            y_linha = x_numerico - y_numerico
            
            # x_linha é a derivada obtida pela equação diferencial
            x_linha = 3 * x_numerico - 4 * y_numerico
            
            y_numerico += h[i] * y_linha
            x_numerico += h[i] * x_linha
            
            t_inicial += h[i]
            if(n[i]==64):
                ax.plot(t_inicial, y_numerico, 'b.')  
            elif(n[i]==256):
                ax.plot(t_inicial, y_numerico, 'k+')  
            elif(n[i]==1024):
                ax.plot(t_inicial, y_numerico, 'g:')  
            elif(n[i]==4096):
                ax.plot(t_inicial, y_numerico, 'r--')  
        
        t_final = t_inicial
        y_real = t_final*np.exp(t_final)
        x_real = 2*t_final*np.exp(t_final) + np.exp(t_final)
        
        # Aplicando a norma do máximo para apresentar o erro encontrado
        erros[i] = np.sqrt((x_real - x_numerico) ** 2 + (y_real - y_numerico) ** 2)
            
    for i in range(len(n)-1):
        ordemP[i+1] = np.log2(erros[i] / erros[i+1]) / np.log2(h[i] / h[i+1])
        
    # Gerando a tabela de convergência númerica para ser utilizada no Latex
    imprimirTabela(n, h, erros, ordemP, printFile)
    ax.set(xlabel='t(unidade) - variavel independete', ylabel='y(unidade) - variavel de estado', title='Convergência da aproximação')
    plt.title('Aproximação numérica da variável y usando Euler')
    plt.legend(['. n = 64', '+ n = 256', ': n = 1024', '-- n = 4096'],loc='upper left')
    plt.show()  

# Funcao usada para criar as tabelas e colocar nos arquivos pedidos        
def imprimirTabela(n, h, erros, ordemP, caminho):
    print(f"n \t &&& \t h_n \t\t &&& \t |e(T,h_n)| \t &&& \t ordem P")

    value = ''
    
    for i in range(len(n)):
        if i == 0:
            print(f"{n[i]}\t&&&\t{h[i]:.4e}\t&&&\t{erros[i]:.4e}\t&&&\t------\t\\\\")
            value += f'{n[i]}\t&&&\t{h[i]:.4e}\t&&&\t{erros[i]:.4e}\t&&&\t------\t\\\\ \n'
        else:
            print(f"{n[i]}\t&&&\t{h[i]:.4e}\t&&&\t{erros[i]:.4e}\t&&&\t{ordemP[i]:.5}\t\\\\")
            value += f'{n[i]}\t&&&\t{h[i]:.4e}\t&&&\t{erros[i]:.4e}\t&&&\t{ordemP[i]:.5}\t\\\\ \n'

    with open(caminho, 'w') as file:
        file.write(value)
        file.close()   

#Function main utilizada para unir o fluxo de dados da resolução das questões para o usuário.
def main():

    control = '1'

    while control == '1':
        print("""
            1. Gráfico para y(t) = cos(mt), -pi <= t <= pi, m = 1, 2 e 3.\n
            2. Solução manufaturada pelo Método de Euler com uma variável de estado.\n 
            3. Solução manufaturada pelo Método de Euler com duas variáveis de estado, utilizando a norma da máxima.\n 
            4. Solução manufatura pelo Método de Euler com duas variáveis de estado, utilizando a norma euclidiana.\n\n
            """)
        
        opt = input('Opção selecionada: ')
        
        if(opt == '1'):
            quest1()
        elif(opt == '2'):
            quest2_1()
        elif(opt == '3'):
            quest2_2()
        elif(opt == '4'):
            quest2_3()
        
        print('Voce deseja testar outra das funcionalidades? Digite: 1 para sim e 0 para nao!')
        
        control = input('Opção selecionada:')
    
    
        
main()
