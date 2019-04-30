layers = QgsProject.instance().mapLayersByName('stream_order')
layer = layers[0]
layer.selectByExpression('"GRID_CODE"=4')

fn = 'C:/temp/outputs/select_gc4.shp'
writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn, 'utf-8', \
driverName='ESRI Shapefile', onlySelected=True)

selected_layer = iface.addVectorLayer(fn, '', 'ogr')

del(writer)
