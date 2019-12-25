fn = 'C:/temp/outputs/stream_order - Copy.shp'

layer = QgsVectorLayer(fn, '', 'ogr')
pv = layer.dataProvider()
pv.addAttributes([QgsField('len_test_m', QVariant.Double), \
QgsField('calc', QVariant.Double)])

layer.updateFields()

expression1 = QgsExpression('$length')
expression2 = QgsExpression('"lengthm"/"len_test_m"')

context = QgsExpressionContext()
context.appendScopes(\
QgsExpressionContextUtils.globalProjectLayerScopes(layer))

with edit(layer):
    for f in layer.getFeatures():
        context.setFeature(f)
        f['len_test_m'] = expression1.evaluate(context)
        layer.updateFeature(f)
        
with edit(layer):
    for f in layer.getFeatures():
        context.setFeature(f)
        f['calc'] = expression2.evaluate(context)
        layer.updateFeature(f)
    
