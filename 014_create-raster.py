from osgeo import gdal, osr
import numpy as np

fn = 'C:/temp/new_raster.tif'

rasterband = np.zeros((10,10))

driver = gdal.GetDriverByName('GTiff')
ds = driver.Create(fn, xsize=10, ysize=10, bands=1, eType=gdal.GDT_Float32)
ds.GetRasterBand(1).WriteArray(rasterband)

geot = [500000, 10, 0, 4600000, 0, -10]
ds.SetGeoTransform(geot)
srs = osr.SpatialReference()
srs.SetUTM(12,1)
srs.SetWellKnownGeogCS('NAD83')
ds.SetProjection(srs.ExportToWkt())
ds = None

rlayer = iface.addRasterLayer(fn)
print('done')