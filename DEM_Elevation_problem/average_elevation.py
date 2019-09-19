import geopandas as gpd
import numpy as np
import csv
import rasterio
from rasterio.warp import calculate_default_transform, reproject, Resampling
from rasterstats import zonal_stats

"""
Reproject the tif file as WGS84 projection
"""

src_img = 'eleven.tif'
dst_img = 'new_eleven.tif'

# Set to WGS84 projection
dst_crs = {'init': 'epsg:4326'}

with rasterio.open(src_img) as src_ds:
    profile = src_ds.profile

    # Transform bounds to WGS84 CRS by using calculate_default_transform
    dst_transform, dst_width, dst_height = calculate_default_transform(
        src_ds.crs, dst_crs, src_ds.width, src_ds.height, *src_ds.bounds)

    # Update profile
    profile.update({
        'crs': dst_crs,
        'transform': dst_transform,
        'width': dst_width,
        'height': dst_height,
        'nodata': 0
    })

    # Write data to new tif file with updated profile
    with rasterio.open(dst_img, 'w', **profile) as dst_ds:
        for i in range(1, src_ds.count + 1):
            src_array = src_ds.read(i)
            dst_array = np.empty((dst_height, dst_width), dtype=profile['dtype'])

            reproject(
                # Source file parameters
                source=src_array,
                src_crs=src_ds.crs,
                src_transform=src_ds.transform,
                # Destinate file parameters
                destination=dst_array,
                dst_transform=dst_transform,
                dst_crs=dst_crs,
                resampling=Resampling.average)

            dst_ds.write(dst_array, i)

# Calculate average elevation
zs = zonal_stats('eleven.shp', 'new_eleven.tif', stats='mean')
aver_ele = [round(z['mean'], 2) for z in zs]

# Open shape file
sp = gpd.read_file('eleven.shp')

# Find PRISM_ID from shape file
_id = sp.PRISM_ID

# Write average elevation along with PRISM_ID into a csv file
with open('average_elevation.csv', "w") as csvFile:
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(['PRISM_ID', 'AVERAGE_ELEVATION'])
    for key in _id.keys():
        csvWriter.writerow([_id[key], aver_ele[key]])

# Reference: https://rasterio.readthedocs.io/en/stable/topics/reproject.html