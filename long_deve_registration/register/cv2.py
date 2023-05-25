import numpy as np
import matplotlib.pyplot as plt

import cv2
from plot.utils import *

def get_kp_des(img, kp_algo='sift'):
        
    if kp_algo == 'orb':
        kp_algo = cv2.ORB_create()
    elif kp_algo == 'sift':
        kp_algo = cv2.SIFT_create()
        
    kp, des = kp_algo.detectAndCompute(img, None)
    des = des.astype(np.uint8)
    
    return kp, des
    
    
def register_rigid_single_ch(img1_ch, img2_ch, kp_algo='sift'):
    
    # Registers img2_ch to img1_ch
    img1 = cv2.convertScaleAbs(img1_ch)
    img2 = cv2.convertScaleAbs(img2_ch)

    kp1, des1 = get_kp_des(img1, kp_algo=kp_algo)
    kp2, des2 = get_kp_des(img2, kp_algo=kp_algo)
    
    # Match the keypoints using a brute-force matcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)

    # Sort the matches by their distances
    matches = sorted(matches, key=lambda x: x.distance)

    # Extract the matched keypoints from the two images
    pts1 = np.float32([kp1[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    pts2 = np.float32([kp2[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
    
    img2_ch_reg = register_rigid_keypoints(img1, img2, pts1, pts2)
    
    return img2_ch_reg


def register_rigid_keypoints(img1, img2, pts1, pts2, affine=False, show_fov_keypoints=False):
    # find an affine transformation based on given keypoints (for example from keypoint detection algorithm, or suite2p soma coordinates)
    
    if type(img1) == 'numpy.ndarray' and type(img2) == 'numpy.ndarray':
        img1 = cv2.convertScaleAbs(img1_ch)
        img2 = cv2.convertScaleAbs(img2_ch)

    # Plot detected keypoints
    if show_fov_keypoints:
        fov_show_keypoints(img1, pts1)
        fov_show_keypoints(img2, pts2)

    # TODO: keypoints scatter
    scatter_pts(pts1, pts2)
    
    # Estimate the affine transform using cv2.estimateAffine2D()
    if affine:
        M, _ = cv2.estimateAffine2D(pts2, pts1)
    else:
        M, _ = cv2.estimateAffinePartial2D(pts2, pts1)
        
    # Apply the affine transform to the second image
    result = cv2.warpAffine(img2, M, (img1.shape[1], img1.shape[0]))
    
    return result, M


def from_stat_to_coords(stat):
    all_x = []
    all_y = []
    
    for i in range(len(stat)):
        x = stat[i]['xpix'][0]
        y = stat[i]['ypix'][0]
        
        all_x.append(x)
        all_y.append(y)
    
    coords = np.array((all_x, all_y)).T#[:,np.newaxis,:] # reformatting to cv format

    return coords


def register_rigid_fromstat(img1, img2, stat1, stat2):
    
    coords1 = from_stat_to_coords(stat1)
    coords2 = from_stat_to_coords(stat2)
    
    # matching ROI points
    bf = cv2.BFMatcher()
    matches = bf.match(coords1.astype(np.float32), coords2.astype(np.float32))
    
    pts1 = np.float32([coords1[m.queryIdx] for m in matches]).reshape(-1, 1, 2)
    pts2 = np.float32([coords2[m.trainIdx] for m in matches]).reshape(-1, 1, 2)
    
    img2_r_reg = register_rigid_keypoints(img1, img2, pts1, pts2)
    
    return img2_r_reg