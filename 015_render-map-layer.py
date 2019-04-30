# create image
img = QImage(QSize(800, 800), QImage.Format_ARGB32_Premultiplied)

# set background color
color = QColor(255, 255, 255, 255)
img.fill(color.rgba())

# create painter
p = QPainter()
p.begin(img)
p.setRenderHint(QPainter.Antialiasing)

# create map settings
ms = QgsMapSettings()
ms.setBackgroundColor(color)

# set layers to render
layer = QgsProject.instance().mapLayersByName('stream_order')
ms.setLayers([layer[0]])

# set extent
rect = QgsRectangle(ms.fullExtent())
rect.scale(1.1)
ms.setExtent(rect)

# set ouptut size
ms.setOutputSize(img.size())

# setup qgis map renderer
render = QgsMapRendererCustomPainterJob(ms, p)
render.start()
render.waitForFinished()
p.end()

# save the image
img.save('C:/temp/test_render.png')

print('image saved')





