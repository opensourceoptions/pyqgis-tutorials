fn = "C:/temp/outputs/stream_order.shp"
layer = QgsVectorLayer(fn, '', 'ogr')
feats = layer.getFeatures()

for feat in feats:
    geom = feat.geometry()
    geomSingleType = QgsWkbTypes.isSingleType(geom.wkbType())
    if geom.type() == QgsWkbTypes.LineGeometry:
        if geomSingleType:
            x = geom.asPolyline()
            print("line:", x)
        else:
            x = geom.asMultiPolyline()
            print("multiline:", x)