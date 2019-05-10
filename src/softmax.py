import numpy as np

def samples(softmax, temperature):

    EPSILON = 10e-16 # to avoid taking the log of zero
    (np.array(softmax) + EPSILON).astype('float64')

    preds = np.log(softmax) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)

    return probas[0]
 