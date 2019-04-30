layerName = 'input_layer_name'
outFile = 'path/to/buffer.shp'
bufDist = 50
layers = QgsProject.instance().mapLayersByName(layerName)
layer = layers[0]
fields = layer.fields()
feats = layer.getFeatures()

writer = QgsVectorFileWriter(outFile, 'UTF-8', fields, \
QgsWkbTypes.Polygon, layer.sourceCrs(), 'ESRI Shapefile')

for feat in feats:
    geom = feat.geometry()
    buffer = geom.buffer(bufDist, 5)
    feat.setGeometry(buffer)
    writer.addFeature(feat)
print('done')
iface.addVectorLayer(outFile, '', 'ogr')
del(writer)


