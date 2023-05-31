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


def norm(img):
    return (img - np.min(img))/np.max(img)

def saturate(norm_img, prop_vmax=0.5):
    norm_img[norm_img>prop_vmax] = prop_vmax
    return norm(norm_img)

def get_img_rgb(img_r, img_g, img_b, prop_vmax_r=1, prop_vmax_g=0.5, prop_vmax_b=0.5):
    r = saturate(norm(img_r), prop_vmax=prop_vmax_r)
    g = saturate(norm(img_g), prop_vmax=prop_vmax_g)
    b = saturate(norm(img_b), prop_vmax=prop_vmax_b)
    
    img_rgb = np.stack((r, g, b)).transpose(1, 2, 0)
    return img_rgb