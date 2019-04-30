#file information
fn = 'C:/temp/smr/trimmer_peak/dem/dem.tif'
fi = QFileInfo(fn)
fname = fi.baseName()

#add raster t0 qgis interface
layer = iface.addRasterLayer(fn, fname)

#query value with sample
val, res = layer.dataProvider().sample(QgsPointXY(246572, 4306418), 1)
print(val, res)

#query value with identify()
ident = layer.dataProvider().identify(QgsPointXY(246572, 4306418), 
QgsRaster.IdentifyFormatValue)
print(ident.isValid())
print(ident.results())