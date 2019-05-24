import processing

#set input and output file names
polyPath = "C:/temp/buffer_clip.shp"
linePath = "C:/temp/streams_clip.shp"
clipPath = "C:/temp/clipped.shp"

#run the clip tool
processing.run("native:clip", {'INPUT':linePath,\
'OVERLAY':polyPath,\
'OUTPUT':clipPath})

#add output to the qgis interface
iface.addVectorLayer(clipPath, '', 'ogr')
