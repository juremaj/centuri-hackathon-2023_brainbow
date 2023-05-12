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



