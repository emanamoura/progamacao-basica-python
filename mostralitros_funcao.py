# -*- coding: utf-8 -*-
"""mostraLitros_funcao.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ycoPCFU0OD4IJf5sN9Vucm_sBGkNqRWS
"""

def lerDados():
  lista = []
  tempoGasto = float(input("Digite o tempo gasto na viagem (em horas): "))
  velocidadeMedia = float(input("Digite a velocidade média da viagem (em Km): "))
  lista.append(tempoGasto)
  lista.append(velocidadeMedia)
  return lista

def calculaDistancia(tempo, velocidade):
  return tempo * velocidade

def calculaLitros(distancia):
  return distancia / 12

def mostraResultados(tempo, velocidade, distancia, litros):
  print(f"O tempo total de viagem foi: {tempo}h")
  print(f"A velocidade média foi de: {velocidade} Km/h")
  print(f"A distância percorrida foi de: {distancia} Km")
  print("A quantidade de litros gastos foi de : {:.2f}".format(litros))

dados = lerDados()
tempo = dados[0]
velocidade = dados[1]
distancia = calculaDistancia(tempo, velocidade)
litrosGastos = calculaLitros(distancia)
mostraResultados(tempo, velocidade, distancia, litrosGastos)