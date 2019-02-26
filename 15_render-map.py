# create image
img = QImage(QSize(800, 600), QImage.Format_ARGB32_Premultiplied)

# set image's background color
color = QColor(255, 255, 255, 0)
img.fill(color.rgba())

# create painter
p = QPainter()
p.begin(img)
p.setRenderHint(QPainter.Antialiasing)

mapSettings = QgsMapSettings() # first create the map settings, then pass to a renderer
mapSettings.setBackgroundColor(color)

# set layer set
layers = QgsProject.instance().mapLayersByName('NHDFlowline17a')
mapSettings.setLayers([layers[0]]) # this takes a list of QgsMapLayer as input

# set extent
rect = QgsRectangle(mapSettings.fullExtent())
rect.scale(1.1)
mapSettings.setExtent(rect)

# set output size
mapSettings.setOutputSize(img.size()) # dpi is now set separately (you would use mapsettings.setDpi(), but it's not necessary here)

# do the rendering
render = QgsMapRendererCustomPainterJob(mapSettings, p) # takes the settings and painter as parameters
render.start()             # rendering is now asynchronous, so you could use threads here
render.waitForFinished()   # but we will block until it's finished
p.end()

# save image
img.save("c:/temp/render.png","png")

print('image saved')