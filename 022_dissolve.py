import processing

#input and output file names
infn = "C:/temp/buffer.shp"
infn2 = "C:/temp/outputs/stream_order.shp"
outfn = "C:/temp/buffer_dissolved_all.shp"
outfn2 = "C:/temp/buffer_dissolved_strord.shp"
outfn3 = "C:/temp/buffer_dissolved.shp"

#basic dissolve: dissolve all features into a single feature
processing.run("native:dissolve", {'INPUT':infn, 'OUTPUT':outfn})

#dissolve features based on values in an attribute table field
processing.run("native:dissolve", {'INPUT':infn, \
FIELD':['GRID_CODE'], 'OUTPUT':outfn2})

#dissolve buffer output into a single feature
processing.run("native:buffer", {'INPUT':infn2, 'DISTANCE':20, \
'DISSOLVE':True, 'OUTPUT':outfn3})

#add layer to the QGIS interface
iface.addVectorLayer(outfn3, '', 'ogr')

