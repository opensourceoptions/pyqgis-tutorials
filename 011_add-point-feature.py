layers = QgsProject.instance().mapLayersByName('beaver_ponds')
layer = QgsVectorLayer(layers[0].dataProvider().dataSourceUri(), '', 'ogr')
caps = layer.dataProvider().capabilities()

if caps & QgsVectorDataProvider.AddFeatures:
    feat = QgsFeature(layer.fields())
    feat.setAttributes([0, 'added programatically'])
    feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(453257, 4631706)))
    res, outFeats = layer.dataProvider().addFeatures([feat])
    
