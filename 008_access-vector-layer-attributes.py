fn = "C:/temp/outputs/stream_order.shp"
layer = QgsVectorLayer(fn, '', 'ogr')

fc = layer.featureCount()

for i in range(0, fc):
    feat = layer.getFeature(i)
    print(feat['ARCID'], feat['GRID_CODE'], feat[1])