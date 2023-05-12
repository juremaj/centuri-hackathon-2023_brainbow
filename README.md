# centuri-hackathon-2023_brainbow
Welcome to the repo for the Brainbow project at Centuri Hackathon 2023!

![image1](https://github.com/juremaj/centuri-hackathon-2023_brainbow/blob/main/media/example_imgs/barrel_cytbow_01.png)

## Requirements

1) Laptop with some free space (20 GB for full data or 300 MB for truncated version)
2) Local conda installation
3) Access to git through command line
4) Github account
5) Optional but useful: FIJI/ImageJ or another GUI for viewing and manipulating tiffs

![gif1](https://github.com/juremaj/centuri-hackathon-2023_brainbow/blob/main/media/example_imgs/nucbow_zsweep.gif)

## Setup

1) Clone github repo:
```
git clone https://github.com/juremaj/centuri-hackathon-2023_brainbow
```
2) Save data locally on your laptop:
You can copy it from the Google (https://drive.google.com/drive/u/0/folders/1GHHy_ASKAV_fGhZkEvEEUDzUQRcDNhFe) or from local drive

3) Save the folder containing 'day1', 'day2' ... as 'data' in the root of the directory we just cloned

4) Create conda environment and activate it:
```
conda create --name brainbow_hack
conda activate brainbow_hack
```

5) Install basic dependencies
```
conda install -c conda-forge numpy
conda install -c conda-forge matplotlib
conda install -c conda-forge scikit-learn
conda install -c conda-forge opentsne
conda install -c conda-forge jupyterlab
```

6) Launch jupyterlab from the root of this directory and follow instructions in the `intro.ipynb` notebook

 
