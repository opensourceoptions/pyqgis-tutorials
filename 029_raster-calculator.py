lyr1 = QgsRasterLayer('C:/temp/elevation/ned10m.tif')
output = 'C:/temp/rascalc.tif'
entries = []

ras = QgsRasterCalculatorEntry()
ras.ref = 'ras@1'
ras.raster = lyr1
ras.bandNumber = 1
entries.append(ras)

calc = QgsRasterCalculator('ras@1 + 1.0', output, 'GTiff', \
lyr1.extent(), lyr1.width(), lyr1.height(), entries)
calc.processCalculation()

lyr2 = QgsRasterLayer(output)
output2 = 'c:/temp/rascalc2.tif'

ras = QgsRasterCalculatorEntry()
ras.ref = 'ras@2'
ras.raster = lyr2
ras.bandNumber = 1
entries.append(ras)

calc = QgsRasterCalculator('ras@1 + ras@2', output2, 'GTiff', \
lyr1.extent(), lyr1.width(), lyr1.height(), entries)
calc.processCalculation()