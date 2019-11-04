fnpts = 'C:/temp/newpoints.shp'
fnstr = 'C:/temp/outputs/stream_order.shp'
fnws = 'C:/temp/outputs/watershed_boundary.shp'
fnout = 'C:/temp/locationjoin.shp'

# join by location\
processing.run("qgis:joinattributesbylocation",\
{'INPUT':fnpts,\
'JOIN':fnws,\
'PREDICATE':[0],\
'JOIN_FIELDS':[],\
'METHOD':0,\
'DISCARD_NONMATCHING':False,\
'PREFIX':'',\
'OUTPUT':fnout})

iface.addVectorLayer(fnout, '', 'ogr')

# join by nearest
#processing.run("native:joinbynearest",\
#{'INPUT':fnpts,\
#'INPUT_2':fnstr,\
#'FIELDS_TO_COPY':['lengthm'],\
#'DISCARD_NONMATCHING':True,\
#'PREFIX':'joined_',\
#'NEIGHBORS':1,\
#'MAX_DISTANCE':73.0,\
#'OUTPUT':fnout})
#
#iface.addVectorLayer(fnout, '', 'ogr')