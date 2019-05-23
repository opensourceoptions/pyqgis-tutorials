sLayerName = "newpoints"
tLayerName = "stream_order"

sLayers = QgsProject.instance().mapLayersByName(sLayerName)
sLayer = sLayers[0]

# Distance between two features in the same layer
#sFeat = sLayer.getFeature(0)
#tFeat = sLayer.getFeature(1)
#sGeom = sFeat.geometry()
#tGeom = tFeat.geometry()
#dist_m = sGeom.distance(tGeom)
#print(dist_m)

# Distance between all features from two different layers
tLayers = QgsProject.instance().mapLayersByName(tLayerName)
tLayer = tLayers[0]

sFeats = sLayer.getFeatures()

print(sLayer.featureCount())
for sfeat in sFeats:
    sgeom = sfeat.geometry()
    tFeats = tLayer.getFeatures()
    for tfeat in tFeats:
        tgeom = tfeat.geometry()
        dist_pl = sgeom.distance(tgeom)
        print(sfeat.id(), tfeat.id(), dist_pl)
    print(sfeat.id(), 'done')
