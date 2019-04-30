#raster filename
fn = 'C:/temp/smr/trimmer_peak/dem/dem.tif'

#add raster t0 qgis interface
layer = iface.addRasterLayer(fn, '')

#get statistics for raster band 1
stats = layer.dataProvider().bandStatistics(1, QgsRasterBandStats.All)

#print band statistics
print(stats.minimumValue)
print(stats.minimumValue)
print(stats.mean)
print(stats.range)
print(stats.stdDev)
print(stats.sum)
print(stats.sumOfSquares)