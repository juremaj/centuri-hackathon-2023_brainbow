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

def pix_transform(pix, shift=0, stretch=1):
    pix_new = []

    for this_pix in pix:
        this_pix = this_pix * stretch
        this_pix = this_pix.astype(int) + shift
        pix_new.append(this_pix)
    
    return pix_new

def pad_shifts(img, xshift, yshift):
    if len(img.shape) == 3:
        img = np.pad(img, ((0,yshift+1), (0,xshift+1), (0,0)))
    elif len(img.shape) == 2:
        img = np.pad(img, ((0,yshift+1), (0,xshift+1)))
    return img

def correct_ds1_day1(xpix, ypix, img_r, img_g, img_b, xshift=18, xstretch=1, yshift=25, ystretch=0.92):
    xpix = pix_transform(xpix, shift=xshift)
    ypix = pix_transform(ypix, shift=yshift, stretch=ystretch)

    img_r = pad_shifts(img_r, xshift, yshift)
    img_g = pad_shifts(img_g, xshift, yshift)
    img_b = pad_shifts(img_b, xshift, yshift)
    
    return xpix, ypix, img_r, img_g, img_b