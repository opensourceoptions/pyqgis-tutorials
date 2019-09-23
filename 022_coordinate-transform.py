# coordinate transformation

crs = QgsCoordinateReferenceSystem(4326)  # WGS 84
crsNew = QgsCoordinateReferenceSystem(26912)  # NAD83 / UTM Zone 12 N
tform = QgsCoordinateTransform(crs, crsNew, QgsProject.instance())

x, y = -112.0, 35.0 # point in northern Arizona

# transform to UTM zone 12 N
ptUTM = tform.transform(QgsPointXY(x, y))
print("Transformed UTM:", ptUTM)

# reverse transformation
ptWGS = tform.transform(ptUTM, QgsCoordinateTransform.ReverseTransform)
print("Undone:", ptWGS)
