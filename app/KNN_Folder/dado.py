from typing import List
class Dado:
    def __init__(self, atributos: List[float], classe: str):
        self.__atributos__ = atributos
        self.__classe__ = classe
        self.__distancia__: float = 0

    def get_atributos(self):
        return self.__atributos__

    def get_classe(self):
        return self.__classe__

    def get_distancia(self):
        return self.__distancia__

    def set_distancia(self, distancia:float):
        self.__distancia__ = distancia
