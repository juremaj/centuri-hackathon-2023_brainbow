import numpy as np
from openTSNE import TSNE
import os


def get_tstamps(tseries, F):
    return np.arange(0, tseries.shape[1]/F, 1/F)

def fit_tsne_1d(data):
    print('fitting 1d-tSNE...')
    # default openTSNE params
    tsne = TSNE(
        n_components=1,
        perplexity=30,
        initialization="pca",
        metric="euclidean",
        n_jobs=8,
        random_state=3,
    )

    tsne_emb = tsne.fit(data.T)
    return tsne_emb