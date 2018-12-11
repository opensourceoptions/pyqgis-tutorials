from qgis.PyQt import QtGui

#path to shapefile
fn = 'C:/temp/test/01_shpIn/brat_cap_20170224.shp'





#basic symbology
#layer = iface.addVectorLayer(fn, '', 'ogr')
#print field names and field types
#for field in layer.fields():
#    print(field.name(), field.type())
#print(layer.renderer().symbol().symbolLayers()[0].properties())
#symbol = QgsLineSymbol.createSimple({'line_style': 'dash', 'color': 'red'})
#layer.renderer().setSymbol(symbol)
#layer.triggerRepaint()

#graduated symbology
#open shapefile
#layer = QgsVectorLayer(fn, 'name', 'ogr')
#if not layer:
#    print('layer failed to load')
#myTargetField = 'totdams'
#myRangeList = []
#myOpacity = 1
# Make our first symbol and range...
#myMin = 0.0
#myMax = 5.0
#myLabel = 'Group 1'
#myColour = QtGui.QColor('#ffee00')
#mySymbol1 = QgsSymbol.defaultSymbol(layer.geometryType())
#mySymbol1.setColor(myColour)
#mySymbol1.setOpacity(myOpacity)
#myRange1 = QgsRendererRange(myMin, myMax, mySymbol1, myLabel)
#myRangeList.append(myRange1)
##now make another symbol and range...
#myMin = 5.1
#myMax = 12
#myLabel = 'Group 2'
#myColour = QtGui.QColor('#00eeff')
#mySymbol2 = QgsSymbol.defaultSymbol(
#     layer.geometryType())
#mySymbol2.setColor(myColour)
#mySymbol2.setOpacity(myOpacity)
#myRange2 = QgsRendererRange(myMin, myMax, mySymbol2, myLabel)
#myRangeList.append(myRange2)
#myRenderer = QgsGraduatedSymbolRenderer('', myRangeList)
#myRenderer.setMode(QgsGraduatedSymbolRenderer.EqualInterval)
#myRenderer.setClassAttribute(myTargetField)
#
#layer.setRenderer(myRenderer)
#QgsProject.instance().addMapLayer(layer)




