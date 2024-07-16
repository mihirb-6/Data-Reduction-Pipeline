# %%
import numpy as np
import matplotlib.pyplot as plt
import math
from matplotlib.colors import LogNorm

from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

from astropy.io import fits
from astropy.nddata import CCDData
import ccdproc

import os

def median_fits(filenames):
    FITS_list = []
    for filename in filenames:
        hdulist = fits.open(filename)
        FITS_list.append(hdulist[0].data)
        hdulist.close()
        
        FITS_stack = np.dstack(FITS_list)
        median = np.median(FITS_stack, axis=2)
        
    return median

def get_files(path):
    filelist = []
    for filename in os.listdir(path):
        file = os.path.join(path, filename)
        filelist.append(file)
    return filelist

        

if __name__ == '__main__':
    light_path = 'C:/Users/mihir/image_process/NGC7000/lights'
    dark_path = 'C:/Users/mihir/image_process/NGC7000/darks'
    flat_path = 'C:/Users/mihir/image_process/NGC7000/flats'
    bias_path = 'C:/Users/mihir/image_process/NGC7000/biases'
    
    lights = get_files(light_path)
    darks = get_files(dark_path)
    flats = get_files(flat_path)
    lights = get_files(light_path)
