fn = "C:/temp/outputs/stream_order - Copy.shp"

layer = iface.addVectorLayer(fn, '', 'ogr')

features = layer.getFeatures()

caps = layer.dataProvider().capabilities()

#if caps & QgsVectorDataProvider.AddAttributes:
#    res = layer.dataProvider().addAttributes([QgsField('OrderCat', QVariant.String),
#    QgsField('LenCat', QVariant.String)])
#    layer.updateFields()

if caps & QgsVectorDataProvider.DeleteAttributes:
    res = layer.dataProvider().deleteAttributes([7,8])
    layer.updateFields()

    