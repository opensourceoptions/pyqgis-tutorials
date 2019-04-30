from qgis.PyQt import QtGui

layers = QgsProject.instance().mapLayersByName('stream_order')
layer = layers[0]

project = QgsProject.instance()
manager = project.layoutManager()
layoutName = 'Layout1'
layouts_list = manager.printLayouts()
# remove any duplicate layouts
for layout in layouts_list:
    if layout.name() == layoutName:
        manager.removeLayout(layout)
layout = QgsPrintLayout(project)
layout.initializeDefaults()
layout.setName(layoutName)
manager.addLayout(layout)

# create map item in the layout
map = QgsLayoutItemMap(layout)
map.setRect(20, 20, 20, 20)

# set the map extent
ms = QgsMapSettings()
ms.setLayers([layer]) # set layers to be mapped
rect = QgsRectangle(ms.fullExtent())
rect.scale(1.0)
ms.setExtent(rect)
map.setExtent(rect)
map.setBackgroundColor(QColor(255, 255, 255, 0))
layout.addLayoutItem(map)

map.attemptMove(QgsLayoutPoint(5, 20, QgsUnitTypes.LayoutMillimeters))
map.attemptResize(QgsLayoutSize(180, 180, QgsUnitTypes.LayoutMillimeters))

legend = QgsLayoutItemLegend(layout)
legend.setTitle("Legend")
layerTree = QgsLayerTree()
layerTree.addLayer(layer)
legend.model().setRootGroup(layerTree)
layout.addLayoutItem(legend)
legend.attemptMove(QgsLayoutPoint(230, 15, QgsUnitTypes.LayoutMillimeters))

scalebar = QgsLayoutItemScaleBar(layout)
scalebar.setStyle('Line Ticks Up')
scalebar.setUnits(QgsUnitTypes.DistanceKilometers)
scalebar.setNumberOfSegments(4)
scalebar.setNumberOfSegmentsLeft(0)
scalebar.setUnitsPerSegment(0.5)
scalebar.setLinkedMap(map)
scalebar.setUnitLabel('km')
scalebar.setFont(QFont('Arial', 14))
scalebar.update()
layout.addLayoutItem(scalebar)
scalebar.attemptMove(QgsLayoutPoint(220, 190, QgsUnitTypes.LayoutMillimeters))

title = QgsLayoutItemLabel(layout)
title.setText("My Title")
title.setFont(QFont('Arial', 24))
title.adjustSizeToText()
layout.addLayoutItem(title)
title.attemptMove(QgsLayoutPoint(10, 5, QgsUnitTypes.LayoutMillimeters))

layout = manager.layoutByName(layoutName)
exporter = QgsLayoutExporter(layout)

fn = 'C:/temp/layout_export.pdf'
#exporter.exportToImage(fn, QgsLayoutExporter.ImageExportSettings())
exporter.exportToPdf(fn, QgsLayoutExporter.PdfExportSettings())

