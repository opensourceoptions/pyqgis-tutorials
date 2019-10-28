
fn = "C:/temp/elevation/ned10m.tif"
out_qgis = "C:/temp/slope_qgis.tif"
out_gdal = "C:/temp/slope_gdal.tif"

processing.run("qgis:slope", \
{'INPUT':fn,\
'Z_FACTOR':1,\
'OUTPUT': out_qgis})

iface.addRasterLayer(out_qgis)

processing.run("gdal:slope", \
{'INPUT':fn,\
'BAND':1,\
'SCALE':1,\
'AS_PERCENT':True,\
'COMPUTE_EDGES':True,\
'ZEVENBERGEN':False,\
'OPTIONS':'',\
'OUTPUT':out_gdal})

iface.addRasterLayer(out_gdal)