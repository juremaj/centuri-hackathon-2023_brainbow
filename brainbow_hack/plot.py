import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
import warnings
import os  

def fov_show(img, cmap='Greys_r', vmax_fact=1/2, title=''):
    plt.figure(dpi=100)
    plt.imshow(img,cmap=cmap, vmax = np.max(img)*vmax_fact)
    plt.axis('off')
    plt.title(title)
    plt.show()

    
def plot_acts(tstamps, data, bottom_plot='Mean', add_plot=None, tmin=0, tmax=None, title='', save_path=None):
    
    # shortening data (optional)
    ind_tmax = data.shape[1] if tmax==None else int(tmax/(tstamps[1]-tstamps[0]))
    ind_tmin = int(tmin/(tstamps[1]-tstamps[0]))
    
    data = data[:, ind_tmin:ind_tmax]
    tstamps = tstamps[ind_tmin:ind_tmax]
    
    # plotting
    _, axs = plt.subplots(2, 1, figsize=(10,4), dpi = 400, gridspec_kw={'height_ratios': [3, 1]})
    
    axs[0].imshow(data, cmap='binary', interpolation='nearest', aspect='auto', vmin=0, vmax=3.291) # z scored for 0.001
    axs[0].xaxis.set_visible(False)
    axs[0].set_ylabel('roi id')
    axs[0].set_title(title)
    
    plot_mean = (np.mean(data, axis=0)-np.min(np.mean(data, axis=0)))/np.max((np.mean(data, axis=0)-np.min(np.mean(data, axis=0))))
    
    if type(bottom_plot) == str:
        axs[1].plot(tstamps, plot_mean, label='avg')
    else:
        axs[1].plot(tstamps, bottom_plot[ind_tmin:ind_tmax], label='avg')
        
    if not add_plot is None:
        axs[1].plot(tstamps, add_plot[ind_tmin:ind_tmax], label='add_plot', alpha=0.5, c='grey')
    axs[1].set_xlim((np.min(tstamps)), np.max(tstamps))
    axs[1].set_ylabel('% active')
    axs[1].set_xlabel('Time (s)')
    axs[1].set_ylim([-0.1, 1.1])

    if type(save_path) == str:
        save_filename = os.path.join(save_path, title)
        plt.savefig(save_filename)
            
def plot_acts_sorted(tstamps, data, embedding, bottom_plot='Mean', add_plot=None, component=0, tmin=0, tmax=None, title='embedding', save_path=None):
        
    # getting sorting indices
    temp = np.argsort(embedding[:,component])
    
    plot_acts(tstamps, data[temp,:], bottom_plot=bottom_plot, add_plot=add_plot, tmin=tmin, tmax=tmax, title=title, save_path=save_path)
    
    if type(save_path) == str:
        save_filename = os.path.join(save_path, title)
        plt.savefig(save_filename)
        
def plot_rois_cont_colorcoded(xpix, ypix, image_array, c_cells=None, title='', cmap='jet', save_path=None):
    
    warnings.filterwarnings("ignore") # just for hackathon (annoying!)
    ## start of function
    if c_cells is None:
        colors = ['C0'] * len(xpix) # set color to default if not specified
    else:
        colors = map_vec_to_colors(c_cells)

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(10,10),dpi=200)

    # Display the normalized image
    ax.imshow(image_array, cmap='gray', vmax=2/3*np.max(image_array)) # saturating a bit

    count = 0
    # Plot each ROI contour with a different color
    for roi_coords in zip(ypix, xpix):
        roi_patch = np.zeros_like(image_array, dtype=np.float32)
        roi_patch[roi_coords] = 1
        contours = ax.contour(roi_patch, levels=[0.5], colors=[colors[count]], alpha=1, linewidths=0.5)
        count+=1

    plt.axis('off')
    plt.title(title)

    if not c_cells is None:
        cmap = cm.get_cmap(cmap)
        norm = Normalize(vmin=0, vmax=len(xpix))
        scalar_map = cm.ScalarMappable(norm=norm, cmap=cmap)
        cbar = fig.colorbar(scalar_map, shrink=0.805)
        cbar.set_ticks([0, len(xpix)])
        cbar.set_ticklabels([0, len(xpix)])
        cbar.ax.tick_params(labelsize=20)

    if type(save_path) == str:
        save_filename = os.path.join(save_path, title)
        plt.savefig(save_filename)
        

def map_vec_to_colors(vec, cmap='jet'):
    
    # Normalize the float values between 0 and 1
    normalized_values = np.array(vec)
    normalized_values = (normalized_values - np.min(normalized_values)) / (np.max(normalized_values) - np.min(normalized_values))

    # Create the jet colormap
    cmap = cm.get_cmap('jet')

    # Map the normalized values to RGB colors
    colors = cmap(normalized_values)
    colors = colors[:,0,:3].tolist()
    
    return colors

def center_max_im(max_im, true_px_height=512, true_px_width=512):
    d_x = int((true_px_width - max_im.shape[1])/2)
    d_y = int((true_px_height - max_im.shape[0])/2)
    
    orig_y, orig_x = max_im.shape
    
    cent_max_im = np.zeros((true_px_height, true_px_width))
    cent_max_im[d_y:orig_y+d_y, d_x:orig_x+d_x] = max_im
    return cent_max_im

def plot_traces(tstamps, fluo, ind_neurons, tmin=0, tmax=None, title='', save_path=None):

    ind_tmax = fluo.shape[1] if tmax==None else int(tmax/(tstamps[1]-tstamps[0]))
    ind_tmin = int(tmin/(tstamps[1]-tstamps[0]))
    
    fluo_plot = fluo[ind_neurons, ind_tmin:ind_tmax]
    tstamps_plot = tstamps[ind_tmin:ind_tmax]
    
    fig, axs = plt.subplots(10, 1, figsize=(5,5), dpi=200)
    axs[0].set_title(title)
                   
    for i in range(len(ind_neurons)):
        
        axs[i].plot(tstamps_plot, fluo_plot[i,:], linewidth=0.5)

        axs[i].set_yticks([]) # y label is arbitrary units
        axs[i].set_ylabel("")
        axs[i].spines["top"].set_linewidth(0)
        axs[i].spines["right"].set_linewidth(0)
        axs[i].spines["left"].set_linewidth(0)  

        if i != len(ind_neurons)-1:
            axs[i].spines["bottom"].set_linewidth(0)
            axs[i].set_xticks([])
            axs[i].set_xlabel("")
        else:
            axs[i].set_xlabel('Time (s)')
        
        if type(save_path) == str:
            save_filename = os.path.join(save_path, title)
            plt.savefig(save_filename)
