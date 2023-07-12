from sklearn import metrics
import numpy as np
from nltk.translate.bleu_score import sentence_bleu
from nltk.metrics import edit_distance

y_test=[1,0,0,1,1,0,1,1,1]
y_pred1=[1,0,1,0,1,0,1,0,1]
prop=[0.1,0.4,0.9,0.3,0.2,0.3,0.9,0.4,0.2]
print("accurary : ",metrics.accuracy_score(y_test,y_pred1))
print('Precision :',metrics.precision_score(y_test,y_pred1))
print('Recall : ',metrics.recall_score(y_test,y_pred1))
print('F1 score : ',metrics.f1_score(y_test,y_pred1))
print('Roc_Auc : ',metrics.roc_auc_score(y_test,prop))
print('PRC : ',metrics.average_precision_score(y_test,prop))


reference = [['that' ,'is', 'test','today','morning'],['thsw','is','fine','today','morning']]
candidate = ['this', 'is', 'test','today','morning']
print('bleu score 1 gram :', sentence_bleu(reference, candidate,weights=(1,0,0,0)))
print('bleu score 2 gram :', sentence_bleu(reference, candidate,weights=(0,1,0,0)))
print('bleu score 3 gram :', sentence_bleu(reference, candidate,weights=(0,0,1,0)))
print('bleu score 4 gram :', sentence_bleu(reference, candidate,weights=(0,0,0,1)))

x_char="everything is possible"
y_char="everything is none"
print('Character error : ',edit_distance(x_char,y_char)/len(x_char))

x_word=x_char.split()
y_word=y_char.split()
print('word error : ',edit_distance(x_word,y_word)/len(x_word))


