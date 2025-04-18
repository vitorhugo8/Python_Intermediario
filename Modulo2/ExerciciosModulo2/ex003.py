# Criando uma lista com vários números e somando eles 
import math
lista = []

def inserir_na_lista():
    entrada = input("Insira 1 ou mais valores: ")
    valores = [float(valor.strip()) for valor in entrada.split(',')] # .strip converte os valores inseridos para número
    lista.extend(valores)
    
    lista_somada = math.fsum(lista)
    print("Soma da lista:", lista_somada)

inserir_na_lista()
