# These two lines of code and the two functions below should work

img2_r_reg = register_nonrigid_single_ch(img1_r, img2_r, nonrigid=True, kp_algo='orb')
fov_show(img2_r_reg, vmax_fact=1)

# Functions

def register_keypoints(img1, img2, pts1, pts2, matches=[], nonrigid=False, affine=False, show_fov_keypoints=False):
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
    
    if nonrigid:
        # Compute the non-rigid transformation using TPS
        tps = cv2.createThinPlateSplineShapeTransformer(regularizationParameter=-10)

        tps.estimateTransformation(pts2.reshape(1, -1, 2), pts1.reshape(1, -1, 2), matches)

        # Apply the transformation to the first image
        result = tps.warpImage(img2)
        
    else:
        # Estimate the affine transform using cv2.estimateAffine2D()
        if affine:
            M, _ = cv2.estimateAffine2D(pts2, pts1)
        else:
            M, _ = cv2.estimateAffinePartial2D(pts2, pts1)
        
        # Apply the affine transform to the second image
        result = cv2.warpAffine(img2, M, (img1.shape[1], img1.shape[0]))

    return result



def register_nonrigid_single_ch(img1_ch, img2_ch, kp_algo='sift', nonrigid=False):
    
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
    
    img2_ch_reg = register_keypoints(img1, img2, pts1, pts2, matches=matches, nonrigid=nonrigid)
    
    return img2_ch_reg