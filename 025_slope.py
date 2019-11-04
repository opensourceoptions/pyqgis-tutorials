fn = "C:/temp/elevation/ned10m.tif"
out_qgis = "C:/temp/slope_qgis.tif"
out_gdal = "C:/temp/slope_gdal.tif"

def slope_qgis(in_fn, out_fn='TEMPORARY_OUTPUT', zfact=1.0, add_iface=True):
    processing.run("qgis:slope", \
    {'INPUT':fn,\
    'Z_FACTOR':zfact,\
    'OUTPUT':out_fn})
    if add_iface:
        iface.addRasterLayer(out_fn)

def slope_gdal(in_fn, out_fn='TEMPORARY_OUTPUT', percent=True):
    processing.run("gdal:slope", \
    {'INPUT':fn,\
    'BAND':1,\
    'SCALE':1,\
    'AS_PERCENT':percent,\
    'COMPUTE_EDGES':True,\
    'ZEVENBERGEN':False,\
    'OPTIONS':'',\
    'OUTPUT':out_fn})
    iface.addRasterLayer(out_fn)

slope_qgis(fn, out_qgis)
slope_gdal(fn, out_gdal)