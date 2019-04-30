#get layers with the name 'dem'
layers = QgsProject.instance().mapLayersByName('dem')

#print the number of layers with name 'dem'
print(len(layers))

#for each layer, print the name, file name, band count, height(cells), and width(cells)
for layer in layers:
    print(layer.name())
    print(layer.dataProvider().dataSourceUri())
    print(layer.bandCount(), layer.height(), layer.width())

#get vector layers with the name 'stream_order'
vlayers = QgsProject.instance().mapLayersByName('stream_order')

#print the number of layers with name 'stream_order'
print(len(vlayers))

#for each layer print the layer name and the file name
for layer in vlayers:
    print(layer.name())
    print(layer.dataProvider().dataSourceUri())

#add the layer into the interface using the file name of the layer already in the interface
testlayer = iface.addVectorLayer(vlayers[0].dataProvider().dataSourceUri(), '', 'ogr')