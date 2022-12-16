import pandas as pd
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from io import BytesIO
from libraries import knn_training

def file_to_df(contents):
    buffer_var = BytesIO(contents)
    df = pd.read_csv(buffer_var)
    buffer_var.close()
    return df

def train_test_split(df, keyword):
    try:
        for index, value in enumerate(df[f'{keyword}'].unique()):
            df = df.replace({value: index})
    except:
        pass
    train = df.sample(frac = 0.8)
    return train, df.drop(train.index) 

def predict(train, test, neighbors):
    predicts = []
    real = []
    for x in test.values.tolist():
        real.append(x[-1])
        label = knn_training.predict_classification(train=train,test_row=x, num_neighbors=neighbors)
        predicts.append(label)
    return real, predicts

def create_confusion_matrix(real, predicts):
    plt.figure(figsize = (10,7))
    df_cfm = pd.DataFrame(confusion_matrix(real, predicts), index = list(set(real)), columns = list(set(real)))
    cfm_plot = sns.heatmap(df_cfm, annot=True)
    cfm_plot.figure.savefig("confusion_matrix.png")