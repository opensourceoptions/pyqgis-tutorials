fn = 'C:/temp/smr/trimmer_peak/dem/dem.tif'

fi = QFileInfo(fn)
fname = fi.baseName()

rlayer = iface.addRasterLayer(fn, fname)

stats = rlayer.dataProvider().bandStatistics(1, QgsRasterBandStats.All)
min = stats.minimumValue
max = stats.maximumValue

fnc = QgsColorRampShader()
fnc.setColorRampType(QgsColorRampShader.Interpolated)

lst = [QgsColorRampShader.ColorRampItem(min, QColor(0, 255, 0)), \
QgsColorRampShader.ColorRampItem(max, QColor(255, 255, 0))]

fnc.setColorRampItemList(lst)

shader = QgsRasterShader()
shader.setRasterShaderFunction(fnc)

renderer = QgsSingleBandPseudoColorRenderer(rlayer.dataProvider(), 1, shader)
rlayer.setRenderer(renderer)