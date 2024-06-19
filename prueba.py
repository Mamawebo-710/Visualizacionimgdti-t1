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
from collections import Counter

'''Crear regla para elimnar las img con una mayor cantidad de 0 (umbral de x)           pixeles totales =7505 '''

tamanio= [0,0,0]


folder_path = 'path'
files = os.listdir(folder_path)
text_files = [f for f in files if f.endswith('.nii')]
                                             

for text_file in text_files:

    file_path = os.path.join(folder_path, text_file)
    i=1
    brain_vol = nib.load(file_path)
    brain_vol_dato = brain_vol.get_fdata()
    print(brain_vol_dato.shape)



    if isinstance(brain_vol_dato, np.memmap):


        
     #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           IMG DTI          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


        np.sum(np.isnan(brain_vol_dato))

        brain_vol_data = np.where(np.isnan(brain_vol_dato),0.0,brain_vol_dato)


        plt.imshow(brain_vol_dato[:,:,1], cmap='bone')
        plt.axis('off')
        plt.show()

        num_imagenes = 79
        rows = 9
        cols = 9


        #&&&&&&&&&&&&&& Histograma &&&&&&&&&&&&&&#
        min_value = 0.0
        max_value = 1.0
        max_valuee = 20000


        values_within_range = brain_vol_data[:, :, 1][(brain_vol_data[:, :, 1] >= min_value) & (brain_vol_data[:, :, 1] <= max_value)]
        flat_values = values_within_range.flatten()

        value_counts = Counter(np.round(flat_values, 3))

        x = list(value_counts.keys())
        y = list(value_counts.values())


        plt.figure(figsize=(12, 6))
        plt.bar(x, y, width=0.08, align='center', color='skyblue') 
        plt.xlabel('Escala de grises')
        plt.ylabel('Cantidad de ese gris (Escala log)')
        plt.yscale('log')  
        plt.ylim([0,max_valuee])
        plt.title('Histograma de escala de grises')
        plt.tight_layout()
        plt.show()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Primer corte%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        fig, axes = plt.subplots(rows, cols, figsize=(30, 30))

        for i in range(num_imagenes):
            ax = axes[i // cols, i % cols]  
            np.where(np.isnan(brain_vol_data[i, :, :]), 0.0, brain_vol_data[i, :, :])
            ax.imshow(brain_vol_data[i, :, :]) 
            ax.axis('off') 

        for i in range(num_imagenes, rows * cols):
            ax = axes[i // cols, i % cols]
            ax.axis('off')
            ax.set_visible(False)

        plt.suptitle('DTI, Corte Sagital', x=0.93, y=0.07, ha='right', fontsize=20)
        plt.tight_layout()  
        plt.show()

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Segundo corte%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            
        fig, axes = plt.subplots(10, 10, figsize=(30, 30)) 

        for j in range(95):
            ax = axes[j // 10, j % 10]
            np.where(np.isnan(brain_vol_data[:, j, :]), 0.0, brain_vol_data[:, j, :])
            ax.imshow(brain_vol_data[:, j, :]) 
            ax.axis('off') 

        for i in range(94, 10 * 10):
            ax = axes[i // 10, i % 10]
            ax.axis('off')
            ax.set_visible(False)

        plt.suptitle('DTI, Corte Coronal', x=0.92, y=0.07, ha='right', fontsize=20)
        plt.tight_layout()
        plt.show()


#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%Tercer corte%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        fig, axes = plt.subplots(rows, cols, figsize=(40, 40)) 

        for k in range(num_imagenes):
            ax = axes[k // cols, k % cols]
            np.where(np.isnan(brain_vol_data[:, :, k]), 0.0, brain_vol_data[:, :, k])
            ax.imshow(brain_vol_data[:, :, k])
            ax.axis('off')

        for i in range(num_imagenes, rows * cols):
            ax = axes[i // cols, i % cols]
            ax.axis('off')
            ax.set_visible(False)

        plt.suptitle('DTI, Corte Axial', x=0.94, y=0.07, ha='right', fontsize=20)
        plt.tight_layout()  
        plt.show()


    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Termino de img dti %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
       
        

    else :


     #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@           IMG T1          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

        num_imagenes = 79  
        rows = 9  
        cols = 9  
        brain_vol_data = np.where(np.isnan(brain_vol_dato),0.0,brain_vol_dato)


        plt.imshow(brain_vol_dato[:,45,:], cmap='bone')
        plt.axis('off')
        plt.show()

                #%%%%%%%%%%%%%%%%%%%%%%%%%%%%Primer corte%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        fig, axes = plt.subplots(rows, cols, figsize=(30, 30))

        for i in range(num_imagenes):
            ax = axes[i // cols, i % cols]  
            np.where(np.isnan(brain_vol_data[i, :, :]), 0.0, brain_vol_data[i, :, :])
            ax.imshow(brain_vol_data[i, :, :], cmap='gray') 
            ax.axis('off') 

        for i in range(num_imagenes, rows * cols):
            ax = axes[i // cols, i % cols]
            ax.axis('off')
            ax.set_visible(False)

        plt.suptitle('T1, Corte Sagital', x=0.93, y=0.07, ha='right', fontsize=20)
        plt.tight_layout()  
        plt.show()



            #%%%%%%%%%%%%%%%%%%%%%%%%%%%%Segundo corte%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        fig, axes = plt.subplots(10, 10, figsize=(30, 30)) 

        for j in range(95):
            ax = axes[j // 10, j % 10]
            np.where(np.isnan(brain_vol_data[:, j, :]), 0.0, brain_vol_data[:, j, :])
            ax.imshow(brain_vol_data[:, j, :], cmap='gray') 
            ax.axis('off') 

        for i in range(94, 10 * 10):
            ax = axes[i // 10, i % 10]
            ax.axis('off')
            ax.set_visible(False)

        plt.suptitle('T1, Corte Coronal', x=0.92, y=0.07, ha='right', fontsize=20)
        plt.tight_layout()
        plt.show()

            #%%%%%%%%%%%%%%%%%%%%%%%%%%%%Tercer corte%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        fig, axes = plt.subplots(rows, cols, figsize=(40, 40)) 

        for k in range(num_imagenes):
            ax = axes[k // cols, k % cols]
            np.where(np.isnan(brain_vol_data[:, :, k]), 0.0, brain_vol_data[:, :, k])
            ax.imshow(brain_vol_data[:, :, k], cmap='gray')
            ax.axis('off')

        for i in range(num_imagenes, rows * cols):
            ax = axes[i // cols, i % cols]
            ax.axis('off')
            ax.set_visible(False)

        plt.suptitle('T1, Corte Axial', x=0.94, y=0.07, ha='right', fontsize=20)
        plt.tight_layout()  
        plt.show()

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Termino img T1 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 