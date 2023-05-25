# here we need to load additional outputs of suite2p (this will be much easier when re-implemented in datajoint)

# paths
stat1_path = f'{data_root}/JM/{ds1}/{tseries1}/suite2p/plane0/stat.npy'
stat2_path = f'{data_root}/JM/{ds2}/{tseries2}/suite2p/plane0/stat.npy'

redcell1_path = f'{data_root}/JM/{ds1}/{tseries1}/suite2p/plane0/redcell.npy'
redcell2_path = f'{data_root}/JM/{ds2}/{tseries2}/suite2p/plane0/redcell.npy'

# loading
stat1 = np.load(stat1_path, allow_pickle=True)
stat2 = np.load(stat2_path, allow_pickle=True)

redcell1 = np.load(redcell1_path, allow_pickle=True)[:,0]
redcell2 = np.load(redcell2_path, allow_pickle=True)[:,0]

# choose which stat (coordinates of which ROIs) to use
stat1_redcell = stat1[redcell1 == True]
stat2_redcell = stat2[redcell2 == True]

img2_r_reg = register_rigid_fromstat(img1_r, img2_r, stat1_redcell, stat2_redcell)
show_fov_rg(img2_r_reg, img1_r, vmax_fact_r=1.5)