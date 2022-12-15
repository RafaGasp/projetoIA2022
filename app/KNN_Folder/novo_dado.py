from typing import List

class NovoDado:
    def __init__(self, atributos: List[float]):
        self.__atributos__ = atributos
        self.__classe__ = None

    def get_atributos(self):
        return self.__atributos__

    def get_classe(self):
        return self.__classe__

    def set_classe(self, classe: str):
        self.__classe__ = classe
