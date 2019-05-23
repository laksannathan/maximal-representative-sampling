import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics

path = Path(os.getcwd()).parent


#def puROC(auc, pos):
#    return (auc - pos/2)/(1-pos)

def roc(y_test, preds, alpha, name):
    alpha = alpha
    fpr, tpr, threshold = metrics.roc_curve(y_test, preds)
    roc_auc = metrics.auc(fpr, tpr)
    plt.figure(figsize=(3,2))
    label = 'AUC = %0.2f' % roc_auc
    plt.plot(fpr, tpr, 'black', label = label, alpha=alpha)
    plt.legend(loc = 'lower right')
    plt.plot([0, 1], [0, 1],'k--', alpha=alpha)
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('TPR')
    plt.xlabel('FPR')
    #plt.savefig(os.path.join(path, 'fig/roc/'+str(name)+'.png'))
    plt.show()
    return roc_auc

def sample(softmax, temperature):

    EPSILON = 10e-16 # to avoid taking the log of zero
    softmax = (np.array(softmax) + EPSILON).astype('float64')

    preds = np.log(softmax) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)

    return probas[0]



