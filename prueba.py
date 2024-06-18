import dicom2nifti
import nibabel as nib
import nilearn as nil
from nilearn import plotting
import scipy.ndimage as ndi                 
import matplotlib.pyplot as plt
import os
from skimage.segmentation import clear_border
from skimage import measure
from skimage.measure import label,regionprops
from scipy import ndimage as ndi
from scipy.ndimage import measurements, center_of_mass, binary_dilation, zoom
import plotly.graph_objects as go
import numpy as np


i=1
tamanio= [0,0,0]
brain_vol = nib.load('/home/jlagos/Desktop/felipers/f/f/wFELIPE_VALENZUELA.src.gz.dti.fib.gz.fa0.nii')
print(type(brain_vol))


brain_vol_dato = brain_vol.get_fdata()
print(type(brain_vol_dato))


if isinstance(brain_vol_dato, np.memmap):


    
    print("Img dti")



    np.sum(np.isnan(brain_vol_dato))

    brain_vol_data = np.where(np.isnan(brain_vol_dato),0.0,brain_vol_dato)

    num_imagenes = 79  
    rows = 9  
    cols = 9  

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%Primer corte%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    fig, axes = plt.subplots(rows, cols, figsize=(30, 30))  

    for i in range(num_imagenes):
        ax = axes[i // cols, i % cols]  
        np.where(np.isnan(brain_vol_data[i, :, :]), 0.0, brain_vol_data[i, :, :])
        ax.imshow(brain_vol_data[i, :, :], cmap='gray') 
        ax.axis('off')  

    plt.tight_layout()  
    plt.show()



        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%Segundo corte%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    fig, axes = plt.subplots(10, 10, figsize=(30, 30)) 

    for j in range(95):
        ax = axes[j // 10, j % 10]
        np.where(np.isnan(brain_vol_data[:, j, :]), 0.0, brain_vol_data[:, j, :])
        ax.imshow(brain_vol_data[:, j, :], cmap='gray') 
        ax.axis('off') 

    plt.tight_layout()  # Adjust spacing between subplots for better layout
    plt.show()

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%Tercer corte%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    fig, axes = plt.subplots(rows, cols, figsize=(40, 40)) 

    for k in range(num_imagenes):
        ax = axes[k // cols, k % cols]
        np.where(np.isnan(brain_vol_data[:, :, k]), 0.0, brain_vol_data[:, :, k])
        ax.imshow(brain_vol_data[:, :, k], cmap='gray')
        ax.axis('off')

    plt.tight_layout()  
    plt.show()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%Termino de img dti %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    

else :


    print("Img T1")
    
    num_imagenes = 79  
    rows = 9  
    cols = 9  
    brain_vol_data = np.where(np.isnan(brain_vol_dato),0.0,brain_vol_dato)

    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%Primer corte%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    fig, axes = plt.subplots(rows, cols, figsize=(30, 30))  

    for i in range(num_imagenes):
        ax = axes[i // cols, i % cols]  
        np.where(np.isnan(brain_vol_data[i, :, :]), 0.0, brain_vol_data[i, :, :])
        ax.imshow(brain_vol_data[i, :, :], cmap='gray') 
        ax.axis('off')  

    plt.tight_layout()  
    plt.show()



        #%%%%%%%%%%%%%%%%%%%%%%%%%%%% Segundo corte %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    fig, axes = plt.subplots(10, 10, figsize=(30, 30)) 

    for j in range(95):
        ax = axes[j // 10, j % 10]
        np.where(np.isnan(brain_vol_data[:, j, :]), 0.0, brain_vol_data[:, j, :])
        ax.imshow(brain_vol_data[:, j, :], cmap='gray') 
        ax.axis('off') 

    plt.tight_layout()  # Adjust spacing between subplots for better layout
    plt.show()

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Tercer corte %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    fig, axes = plt.subplots(rows, cols, figsize=(40, 40)) 

    for k in range(num_imagenes):
        ax = axes[k // cols, k % cols]
        np.where(np.isnan(brain_vol_data[:, :, k]), 0.0, brain_vol_data[:, :, k])
        ax.imshow(brain_vol_data[:, :, k], cmap='gray')
        ax.axis('off')

    plt.tight_layout()  
    plt.show()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Termino img T1 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%