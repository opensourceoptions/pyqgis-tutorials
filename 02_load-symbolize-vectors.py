#path to shapefile
fn = 'C:/temp/test/01_shpIn/brat_cap_20170224.shp'

#open shapefile and add to map
layer = iface.addVectorLayer(fn, '', 'ogr')
if not layer:
    print('layer failed to load')

#print field names and field types
#for field in layer.fields():
#    print(field.name(), field.type())

#symbology
print(layer.renderer().symbol().symbolLayers()[0].properties())
symbol = QgsLineSymbol.createSimple({'line_style': 'dash', 'color': 'red'})
layer.renderer().setSymbol(symbol)
layer.triggerRepaint()

