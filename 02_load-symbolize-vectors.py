from qgis.PyQt import QtGui

fn = "C:/temp/outputs/stream_order.shp"

##simple vector symbology
#layer = iface.addVectorLayer(fn, '', 'ogr')
#
#symbol = QgsLineSymbol.createSimple({'line_style': 'dash', 'color': 'red'})
#layer.renderer().setSymbol(symbol)
#layer.triggerRepaint()

#graduated symbology
layer = QgsVectorLayer(fn, 'name', 'ogr')

tf = 'GRID_CODE'
rangeList = []
opacity = 1

# create symbology for first range
minVal = 0.0
maxVal = 2.0

lab = 'Group 1'

color1 = QtGui.QColor('#ffee00')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color1)
symbol.setOpacity(opacity)

range1 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range1)

# set up second symbol
minVal = 2.1
maxVal = 4.0

lab = 'Group 2'

color2 = QtGui.QColor('#00eeff')

symbol = QgsSymbol.defaultSymbol(layer.geometryType())
symbol.setColor(color2)
symbol.setOpacity(opacity)

range2 = QgsRendererRange(minVal, maxVal, symbol, lab)
rangeList.append(range2)

# apply ranges to layer
groupRenderer = QgsGraduatedSymbolRenderer('', rangeList)
groupRenderer.setMode(QgsGraduatedSymbolRenderer.EqualInterval)
groupRenderer.setClassAttribute(tf)

layer.setRenderer(groupRenderer)

QgsProject.instance().addMapLayer(layer)

