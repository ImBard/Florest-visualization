import rasterio
import numpy as np 
from rasterio.crs import CRS 
forest_file = rasterio.open("gm_ve_v1.tif")
forests = forest_file.read()

print(np.amin(forests))
print(np.amax(forests))
print(len(np.unique(forests)))
