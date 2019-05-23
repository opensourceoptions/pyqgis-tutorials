import processing

polyPath = "C:/temp/buffer_clip.shp"
linePath = "C:/temp/streams_clip.shp"
clipPath = "C:/temp/clipped.shp"

processing.run("native:clip", {'INPUT':linePath,\
'OVERLAY':polyPath,\
'OUTPUT':clipPath})