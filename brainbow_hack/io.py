import numpy as np
import os
from PIL import Image


def load_avg_movie(ds):
    ops = np.load(f'data/{ds}/physiology/neural_activity/ops.npy', allow_pickle=True).item()
    avg_movie = ops['meanImg']
    avg_movie = (avg_movie - np.min(avg_movie))/np.max(avg_movie)
    return avg_movie

def load_rois(ds):
    stat = np.load(f'data/{ds}/physiology/neural_activity/stat.npy', allow_pickle=True)
    iscell = np.load(f'data/{ds}/physiology/neural_activity/iscell.npy')
    stat = stat[iscell[:,0].astype(bool)]
    
    xpix = []
    ypix = []
    for s in stat:
        xpix.append(s['xpix'])
        ypix.append(s['ypix'])

    return xpix, ypix

def load_data(ds, acts='spks'):
    
    # loading data
    fluo = np.load(f'data/{ds}/physiology/neural_activity/F.npy')
    spks = np.load(f'data/{ds}/physiology/neural_activity/spks.npy')
    iscell = np.load(f'data/{ds}/physiology/neural_activity/iscell.npy')

    if acts == 'spks':
        data = prepare_data(spks, iscell) # here choose spikes or fluorescence + get rid of non-cells + z-scores
    elif acts == 'fluo':
        data = prepare_data(fluo, iscell)
        
    t_max = data.shape[1]
    n_max = data.shape[0]
    
    print('Length of recording (timestamps): ', t_max)
    print('Number of ROIs: ', n_max)

    return data

def prepare_data(data_in, iscell):
    
    iscell_bool = iscell[:,0].astype(bool) # getting rid of 'non-cells'
    
    data = data_in[iscell_bool,:] # choose which data to analyse (spks or fluo)
    data = (data-np.mean(data,1)[:,np.newaxis])/np.std(data,1)[:,np.newaxis]
    
    return data

def load_tiff(ds, channel=''):
    img = Image.open(f'data/{ds}/anatomy/{channel}.tif')
    return np.array(img)