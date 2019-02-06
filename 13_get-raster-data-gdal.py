from osgeo import gdal
layers = QgsProject.instance().mapLayersByName('dem')
layer = layers[0]
ds = gdal.Open(layer.dataProvider().dataSourceUri())
dem_arr = ds.GetRasterBand(1).ReadAsArray()
print(dem_arr[0][0])