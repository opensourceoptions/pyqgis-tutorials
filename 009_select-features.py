fn = "C:/temp/outputs/stream_order.shp"

layer = iface.addVectorLayer(fn, '', 'ogr')
selectid = [1, 3, 6, 8, 11]
layer.select(selectid)
#layer.selectByExpression('"GRID_CODE"=4')
#layer.selectAll()

selection = layer.selectedFeatures()

for feat in selection:
    print(feat['GRID_CODE'])