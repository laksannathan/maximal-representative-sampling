import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

def roc(y_test, preds, iteration, name):
    alpha = min(iteration+0.2,0.8)
    #alp = 1
    fpr, tpr, threshold = metrics.roc_curve(y_test, preds)
    roc_auc = metrics.auc(fpr, tpr)
    #plt.title('Iteration: '+ str(name))
    plt.figure(figsize=(12,8))
    plt.plot(fpr, tpr, 'black', label = 'AUC = %0.2f' % roc_auc,alpha=alp)
    plt.legend(loc = 'lower right')
    plt.plot([0, 1], [0, 1],'k--', alpha=alp)
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.savefig('roc/roc_'+str(name)+".png")
    plt.show()
    
gbs = pd.read_csv('gbs_processed.csv', encoding = "ISO-8859-1", delimiter = ',')
gbs = gbs.fillna(gbs.median())

gesis = pd.read_csv('gesis_processed.csv', encoding = "ISO-8859-1", delimiter = ',')
gesis = gesis.fillna(gesis.median())

gesis.drop(columns = ['GESIS-CODE'], axis=1, inplace = True)
gbs.drop(columns = ['GBS-CODE', 'Gruppe'], axis=1, inplace = True)

gbs['Umfrage'] = 1
gesis['Umfrage'] = 0

print(gbs.shape)
print(gesis.shape)

drop = ['Personen im Haushalt',
       'Nettoeinkommen Selbst', 'Nettoeinkommen Haushalt', 'Schlechter Schlaf',
       'Leben genießen', 'Zu Nichts aufraffen', 'Alles anstrengend',
       'Wahlteilnahme', 'Wahlabsicht', 'Desinteresse Politiker',
       'Zufriedenheit Leben', 'Aktiv', 'Verärgert', 'Wach', 'Nervös', 
       'Ängstlich',
       'Geburtsjahr', 'Geburtsland', 'Nationalitaet',
       'Familienstand', 'Hoechster Bildungsabschluss', 'Berufliche Ausbildung',
       'Erwerbstaetigkeit', 'Berufsgruppe']

#sampled from these two
gbs = gbs.drop(columns=drop, axis=1)
gesis = gesis.drop(columns=drop, axis=1)

gbs_base = gbs.copy()

#predicted/evaluated on these two
gbs_eval = gbs.copy()
gbs_eval.drop(columns = ['Umfrage'], axis=1, inplace=True)

gesis_eval = gesis.copy()
gesis_eval.drop(columns = ['Umfrage'], axis=1, inplace=True)