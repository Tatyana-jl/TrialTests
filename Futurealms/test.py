import numpy

matrica = numpy.random.random_integers(0, 9, (10,10,10))
coordinate=0
for x in range(0,len(matrica)):
    while coordinate==0:
        for y in range(0,len(matrica)):
            while coordinate==0:
                for z in range(0,len(matrica)):
                    if matrica[x][y][z]==0:
                        coordinate=[x,y,z]                       
print ("N of column х:",coordinate[0])
print ("N of column y:",coordinate[1])
print ("N of column z:",coordinate[2])
print ("Intersection point",coordinate)

