layers = QgsProject.instance().mapLayersByName('stream_order - Copy')
layer = layers[0]
caps = layer.dataProvider().capabilities()
feats = layer.getFeatures()
dfeats = []

if caps & QgsVectorDataProvider.DeleteFeatures:
    for feat in feats:
        if feat['GRID_CODE'] == 3:
            dfeats.append(feat.id())
    res = layer.dataProvider().deleteFeatures(dfeats)
    layer.triggerRepaint()