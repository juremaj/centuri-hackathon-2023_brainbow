import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def fov_show(img, cmap='Greys_r', vmax_fact=1/2, show=False):
    plt.figure(dpi=600)
    plt.imshow(img,cmap=cmap, vmax = np.max(img)*vmax_fact)
    plt.axis('off')
    
    if show == True:
        plt.show()
        

def fov_show_pair(img1, img2, cmap='Greys_r', vmax_fact=1/2, show=True):
    fig, axs = plt.subplots(1,2, dpi=300)
    axs[0].imshow(img1,cmap=cmap, vmax = np.max(img1)*vmax_fact)
    axs[0].axis('off')
    axs[1].imshow(img2,cmap=cmap, vmax = np.max(img2)*vmax_fact)
    axs[1].axis('off')
    plt.show()
    
def get_cm_rg():

    black = (0, 0, 0)  # RGB values for black
    red = (1, 0, 0)    # RGB values for red
    green = (0, 1, 0)    # RGB values for red

    colors_red = [black, red]
    colors_green = [black, green]

    cmap_name_red = 'black_red'
    cmap_name_green = 'black_green'

    n_levels = 256

    cm_red = LinearSegmentedColormap.from_list(cmap_name_red, colors_red, N=n_levels)
    cm_green = LinearSegmentedColormap.from_list(cmap_name_green, colors_green, N=n_levels)
    
    return(cm_red, cm_green)

def show_fov_rg(img_r, img_g, vmax_fact_r=0.5, vmax_fact_g=0.5, show=False):
    
    # normalize and scale saturation
    img_r = img_r/(np.max(img_r)*vmax_fact_r)
    img_g = img_g/(np.max(img_g)*vmax_fact_g)
    img_b = np.zeros(img_r.shape) # empty glue channel
    
    img_rgb = np.stack((img_r, img_g, img_b))
    img_rgb = img_rgb.transpose((1, 2, 0))
    
    plt.figure(dpi=300)
    plt.imshow(img_rgb)
    plt.axis('off')
    plt.show()
    
def fov_show_diff(img1, img2, cmap='bwr', vlim_fact=1/2, binarize=False, thr=1.96):
    # normalize both images
    img1 = img1/np.std(img1)
    img2 = img2/np.std(img2)
    
    if binarize:
        img1 = (img1>thr).astype(int)
        img2 = (img2>thr).astype(int)
        
    diff = img1-img2
    lim = np.max(np.abs(diff)) * vlim_fact
    plt.figure(dpi=600)
    plt.imshow(diff,cmap=cmap, vmin=-lim, vmax=lim)#, vmax = np.max(img)*vmax_fact)
    plt.axis('off')
    plt.colorbar()
    plt.show()
    
def fov_show_overlay(img1, img2, cmap='Greys_r', vmax_fact=1/2):
    # normalize both images
    img1 = img1/np.std(img1)
    img2 = img2/np.std(img2)

    plt.figure(dpi=600)
    plt.imshow(img1, cmap=cmap)#, vmin=-lim, vmax=lim)#, vmax = np.max(img)*vmax_fact)
    plt.imshow(img2, cmap=cmap, alpha=0.5)
    plt.axis('off')
    plt.colorbar()
    plt.show()
    
def scatter_pts(pts1, pts2):
    x1 = pts1[:,:,0]
    y1 = pts1[:,:,1]
    
    x2 = pts2[:,:,0]
    y2 = pts2[:,:,1]
    
    plt.figure(figsize=(5,5))
    plt.scatter(x1, y1, s=2)
    plt.scatter(x2, y2, s=2)
    plt.title('Keypoints')
    plt.show()
    
def fov_show_keypoints(img, pts, cmap='Greys_r', vmax_fact=1):
    x = pts[:,:,0]
    y = pts[:,:,1]
    fov_show(img, cmap=cmap, vmax_fact=1, show=False)
    plt.scatter(x, y, s=1, c='red')
    plt.title('Keypoints')
    plt.show()