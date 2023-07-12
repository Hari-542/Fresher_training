import pandas as pd
import numpy as np
from sklearn import metrics

data=pd.read_csv("ex-metrics.csv")
x_test=data.iloc[:,-1]
y_pred1=data.iloc[:,4]
y_test=data.iloc[:,3]
print('Accuracy : ',metrics.accuracy_score(x_test,y_pred1))
print('Precision :',metrics.precision_score(x_test,y_pred1))
print('Recall : ',metrics.recall_score(x_test,y_pred1))
print('F1 score : ',metrics.f1_score(x_test,y_pred1))
print('Roc_Auc : ',metrics.roc_auc_score(x_test,y_test))
