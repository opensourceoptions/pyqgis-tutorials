fn = "C:/temp/doesntexist.tif"

if os.path.exists(fn):
    iface.messageBar().pushMessage("Success", \
    "The file exists and will be loaded", level=3)
    iface.addRasterLayer(fn)
else:
    iface.messageBar().pushMessage("Error", "The file does not exist",\
    level=2)