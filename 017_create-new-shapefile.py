import qgis

# create fields
layerFields = QgsFields()
layerFields.append(QgsField('ID', QVariant.Int))
layerFields.append(QgsField('Value', QVariant.Double))
layerFields.append(QgsField('Name', QVariant.String))

fn = 'C:/temp/newpoints.shp'
writer = QgsVectorFileWriter(fn, 'UTF-8', layerFields,\
QgsWkbTypes.Point,\
QgsCoordinateReferenceSystem('EPSG:26912'),\
'ESRI Shapefile')

feat = QgsFeature()
feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(455618, 4632221)))
feat.setAttributes([1, 1.1, 'one'])
writer.addFeature(feat)

layer = iface.addVectorLayer(fn, '', 'ogr')

del(writer)