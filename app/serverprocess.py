from KNN_Folder.dado import Dado
from KNN_Folder.novo_dado import NovoDado
from KNN_Folder.k_nearest_neighbors import KNN
from typing import List
import matplotlib.pyplot as plt
from sklearn import metrics


def processar(filename, dado):
    conjunto_dados: List[Dado] = []
    with open(filename) as arquivo:
        for linha in arquivo.readlines(): 
            atributos = linha.rstrip().split(',')
            classe = atributos[-1]
            atributos = list(map(float, atributos[:-1]))
            dado_arquivo: Dado = Dado(atributos, classe)
            conjunto_dados.append(dado_arquivo)
    arquivo.close()
    kvizinhos = KNN(3, conjunto_dados)
    dado_teste: NovoDado = NovoDado([dado])
    kvizinhos.executar(dado_teste)
    print(dado_teste.get_classe())
    # color = 'white'
    # confusion_matrix = metrics.confusion_matrix(conjunto_dados, dado_teste)
    # matrix = metrics.ConfusionMatrixDisplay(confusion_matrix=confusion_matrix, display_labels=['False','True'])
    # matrix.ax_.set_title('Confusion Matrix', color=color)
    # plt.xlabel('Predicted Label', color=color)
    # plt.ylabel('True Label', color=color)
    # plt.gcf().axes[0].tick_params(colors=color)
    # plt.gcf().axes[1].tick_params(colors=color)
    # plt.savefig('./static/files')
