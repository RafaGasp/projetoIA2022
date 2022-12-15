from typing import List
from KNN_Folder.dado import Dado
from KNN_Folder.novo_dado import NovoDado
import math


class KNN:
    # Receber um dado não classificado (z),
    # o conjunto de dados classificados (X)
    # e o número de vizinhos (k);
    def __init__(self, k: int, conjunto_dados: List[Dado]):
        self.__k__ = k
        self.__conjunto_dados__ = conjunto_dados

    def __distancia_eucliana__(self, atributos_novo_dado: List[float], atributos_dado_classificado: List[float]):
        somatorio: float = 0
        for atributo_dado_classificado, atributo_novo_dado in zip(atributos_dado_classificado, atributos_novo_dado):
            somatorio += math.pow((atributo_dado_classificado - atributo_novo_dado), 2)
        return math.sqrt(somatorio)

    def __encontrar_mais_proximos__(self):
        conjunto_ordenado: List[Dado] = sorted(self.__conjunto_dados__, key=Dado.get_distancia)
        return conjunto_ordenado[:self.__k__]

    def __classe_mais_recorrente__(self, dados_mais_proximos: List[Dado]):
        dicionario_classes = {}
        for dado_proximo in dados_mais_proximos:
            if dado_proximo.get_classe() in dicionario_classes:
                dicionario_classes[dado_proximo.get_classe()] += 1
            else:
                dicionario_classes[dado_proximo.get_classe()] = 1
        return max(dicionario_classes, key=dicionario_classes.get)

    def executar(self, novo_dado: NovoDado):
        # Medir a distância de z para cada dado
        # que já está classificado;
        for dado_classificado in self.__conjunto_dados__:
            distancia = self.__distancia_eucliana__(novo_dado.get_atributos(), dado_classificado.get_atributos())
            dado_classificado.set_distancia(distancia)
        # Obter as k menores distâncias
        dados_mais_proximos: List[Dado] = self.__encontrar_mais_proximos__()
        # Verificar a classe de cada um dos k dados de menor distância
        # e contar a quantidade de vezes que cada classe que aparece
        # Receber como resultado a classe mais recorrente
        classe = self.__classe_mais_recorrente__(dados_mais_proximos)
        # Classificar o novo dado com a classe mais recorrente
        novo_dado.set_classe(classe)