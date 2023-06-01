# centuri-hackathon-2023_brainbow
Welcome to the repo for the Brainbow project at Centuri Hackathon 2023!
![image1](https://github.com/juremaj/centuri-hackathon-2023_brainbow/blob/main/media/example_imgs/barrel_cytbow_01.png)

## Project description

### *Taste the rainbow* | Mirindra Ratsifandrihamanana and Jure Majnik

In the adult brain, neurons are active in groups called assemblies that orchestrate perception, action, and cognition. The genetic origin and functional homogeneity of cell assemblies and associated anomalies are still unknown. Investigating those processes requires the development of new tools that combined information from both neuronal activity as well as genetic lineage.

To do so, we developed an imaging technique that records the neuronal activity of living mice with cellular resolution using calcium-sensitive fluorescent dyes, combined with the labeling of each cell with a unique combination of colors that depends on their clonal origin (the ‘brainbow’ technique). Importantly, this technique can image the same mouse across multiple days. However, the resulting image sequences are complex, stochastic, and present changing geometry from one day to the next. As such, this project will focus on exploring the development of a few tools for the data-driven analysis of these multi-modal experiments. We have planned for the following tentative milestones representing increasing challenges.  

Associating brainbow signal and associated neuronal activity (calcium-recorded activity) at the cellular resolution using cell segmentation and co-localization across image modalities. This can be carried out using single-day imaging experiments.
Interrogating the association between brainbow signal and neuronal activity. Is lineage (brainbow signal) predictive of neuronal activity (calcium-recorded activity) ? This can be carried out using single-day imaging experiments.
Matching cellular cluster from one day to the next through graph-matching techniques. Are all cells visible across all days? Is the association between brainbow signal and calcium signal stable across time?

![abstract](https://github.com/juremaj/centuri-hackathon-2023_brainbow/blob/main/media/graphical-abstract.png)

## Data outline
All together we provide 4 datasets, roughtly organised in increasing complexity. Here's a brief overview:

- Dataset 1 (ds1): This dataset contains the anatomical (brainbow) and physiological (functional calcium imaging) data. This should allow us to solve the first two goals, linking cell lineage and neural activity. The quality of the recording is relatively good, but the data is only available for a single day.
- Dataset 2 (ds2): A simple dataset to implement and benchmark registration algorithms. It consists of only a single channel (red) anatomical data, but the same field of view is recorded on multiple consecutive days. These images then need to be registered.
- Dataset 3 (ds3): Same as ds2, but more challenging images (less clear correspondance).
- Dataset 4 (ds4): Most complex dataset with both anatomy and physiology (as in ds1) for multiple days in a row. To analyse this data we will need to combine all the points from the easier datasets above (ontogeny-pysiology relationship, registration...). This should allow us to answer the final goal of the project (is the ontogeny-physiology relationship stable).

The rough outline for the data organisation is:
```
- data/
    - ds#/
        - day1/
            - anatomy/
                - red.tif
                - blue.tif
                - green.tif
            - physiology/
                - neural_activity/
                    - F.npy
                    - ops.npy
        - day2/
            ...
        ...
        - dayN/
            ...
```

The `anatomy` subfolder contains the RGB channels for the brainbow data and the `physiology/neural_activity` contains the time-series (calcium traces) as `F.npy` and some additional metadata for each trace (such as its ROI within the FOV) in `ops.npy`. 

(Which exact folders are present in a particular dataset will of course depend on which modalities are given (e. g. ds2 only has anatomy) or for how many days the data is given for that dataset (e. g. ds1 only has a single day))

If this sounds a bit complicated or unclear don't worry :relaxed:, we will give a more extensive introduction into how the data was acquired, preprocessed etc. at the begining of the hackathon.

## Link to data

You can download all four datasets from [here](https://filesender.renater.fr/?s=download&token=3d3b079c-3311-442f-a305-90fb18ef33ec). Then you can just put them in a folder named `data` in the root of this repository (This is where the library/notebook expects the data to live).

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

5) Install basic dependencies (alternatively you can also use the `environment.yml` file in the root of this repo)
```
conda install -c conda-forge numpy
conda install -c conda-forge matplotlib
conda install -c conda-forge scikit-learn
conda install -c conda-forge opentsne
conda install -c conda-forge jupyterlab
```

6) Launch jupyterlab from the root of this directory and follow instructions in the `intro.ipynb` notebook



