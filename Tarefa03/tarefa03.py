import numpy as np
import matplotlib.pyplot as plt
from Funcoes.VanDerPol import resolve_VanDerPol
from Funcoes.predator_prey import resolve_predator_prey

# Define as equações diferenciais do sistema presa-predadorS
# O sistema predador-presa representa a relação entre as espécies em uma lógica de presa-predador
# Nesse caso as variáveis são dependentes uma das outras


def tarefa_completa():
    print("Essa funcao tem alguns modos para cada um dos metodos que vamos utilizar, primeiramente:\n"
          "Defina o método que deseja estudar, digitando:")
    escolha = input("\n 0: Método dos Trapézios para o sistema presa-predador"
                    "\n 1: Método dos Trapézios para resolver um sistema bidimensional de Van Der Pol, caso não suave\n"
                    "\n Selecione o valor: "
                    )
    if (escolha == "0"):
        print("\n\nEscreva sua função predador-presa e os valores necessários para executar o método dos trapézios:\n"
              "a: taxa de crescimento das presas na usência de predadores\n"
              "b: taxa de mortalidade das presas devido à predação\n"
              "c: taxa de mortalidade dos predadores na ausência de presas\n"
              "d: taxa de crescimento dos predadores de vido à predação\n"
              "x: população de presas\n"
              "y: população de predadores\n"
              "t0: tempo iniciail"
              "tf: tempo final"
              "dt: particoes do tempo que deseja iterar"
              )
        print("Para facilitar os testes temos um exemplo de input, copie com crtc+crtv que sera possivel usar: \n"
              "1\n"
              "0.1\n"
              "1.5\n"
              "0.075\n"
              "10\n"
              "5\n"
              "0\n"
              "50\n"
              "0.01"
              )
        valores = [float(input()) for i in range(9)]
        resolve_predator_prey(
            valores[0], valores[1], valores[2], valores[3], valores[4],
            valores[5], valores[6], valores[7], valores[8]
        )
    elif (escolha == "1"):
        resolve_VanDerPol()


tarefa_completa()
