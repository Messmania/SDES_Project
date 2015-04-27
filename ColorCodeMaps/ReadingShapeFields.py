import shapefile
sf = shapefile.Reader('st99_d00')
shapes = sf.shapes()
fields = sf.fields
print fields,len(fields)
print type(fields)
print type(fields[0]),type(fields[1])
for i in range(11):
    print fields[i][0]
