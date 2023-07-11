from sklearn import metrics
import numpy as np
from nltk.translate.bleu_score import sentence_bleu,corpus_bleu

p='pepsi'
c='cola'
f='fanta'

x_test=[p,p,p,p,c,c,c,c,f,f,f,f]
y_pred=[p,p,p,c,c,c,f,c,f,c,f,p]

print(metrics.confusion_matrix(x_test,y_pred))
print(metrics.classification_report(x_test,y_pred))

y_test=[1,0,0,1,1,0,1,1,1]
y_pred1=[1,0,1,0,1,0,1,0,1]
prop=[0.1,0.4,0.9,0.3,0.2,0.3,0.9,0.4,0.2]
print(f'Precision : {metrics.precision_score(y_test,y_pred1)}')
print(f'Recall : {metrics.recall_score(y_test,y_pred1)}')
print(f'F1 score : {metrics.f1_score(y_test,y_pred1)}')
print(f'Roc_Auc : {metrics.roc_auc_score(y_test,prop)}')


reference = [['that', 'it', 'task']]
candidate = ['this', 'is', 'test']
print('bleu score:', sentence_bleu(reference, candidate))
# print('Individual 3-gram: %f' % sentence_bleu(reference, candidate, weights=(1, 0, 1)))


