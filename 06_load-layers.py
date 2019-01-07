fn = "C:/temp/outputs/stream_order.shp"

vlayer = QgsVectorLayer(fn, '', 'ogr')
for field in vlayer.fields():
    print(field.name())

fn2 = 'C:/temp/smr/trimmer_peak/dem/dem.tif'
rlayer = QgsRasterLayer(fn, '')
print(rlayer.bandCount())
    