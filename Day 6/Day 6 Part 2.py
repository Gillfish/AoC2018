file = open("Day 6 puzzle input.txt","r")
#file = open("Day 6 Puzzle Input Test Data.txt","r")

puzzlein = file.readlines()
output = 0
xvalues = []
yvalues = []
gridwidth = 0
gridheight = 0
gridsize = 0
grid = {}
claimid = 0
currenttotal = 0
currentsquares = 0
xloop = 0
yloop = 0
gridx = []
ignoredclaims = []
withinrange = []
totalclaims = 0

def getx( str ):
    #used to get both co-ord and claimid as I formatted that the same way
    xval = str.split(", ")
    xval = xval[0]
    return xval

def gety( str ):
    #used to both get co-ord and distance from claim as I formatted that the same
    yval = str.split(", ")
    yval = yval[1]
    return int(yval)

def getdist( xsquare, ysquare, xcoord, ycoord):
    #get distance from co-ord
    dist = abs(xsquare-xcoord) + abs(ysquare - ycoord)
    return dist

for line in puzzlein:
    xvalues.append(int(getx(line)))
    yvalues.append(gety(line))

#setting up grid
gridwidth = max(xvalues)
gridheight = max(yvalues)
gridsize = max(gridwidth, gridheight)
#print(gridsize)
print("Grid width is: " + str(gridwidth) + ", grid height is: " + str(gridheight))

for x in range(gridwidth):
    for y in range(gridheight):
        grid[x,y] = 0

#populating grid
for line in puzzlein:
    currentx = int(getx(line))
    currenty = gety(line)
    for x in range(gridwidth):
        for y in range(gridheight):
            #positive x, positive y
            if currentx+x < gridwidth:
                if currenty+y < gridheight:
                    grid[currentx+x, currenty+y] += getdist(currentx+x, currenty+y, currentx, currenty)
            #positive x, negative y
            if currentx+x < gridwidth:
                if currenty-y >= 0 and currenty-y < gridheight:
                    grid[currentx+x, currenty-y] += getdist(currentx+x, currenty-y, currentx, currenty)
            #negative x, positive y
            if currentx-x >= 0 and currentx-x < gridwidth:
                if currenty+y < gridheight:
                    grid[currentx-x, currenty+y] += getdist(currentx-x, currenty+y, currentx, currenty)
            #negative x, negative y
            if currentx-x >= 0 and currentx-x < gridwidth:
                if currenty-y >= 0 and currenty-y < gridheight:
                   grid[currentx-x, currenty-y] += getdist(currentx-x, currenty-y, currentx, currenty)


#getting answer
for x in range(gridwidth):
    for y in range(gridheight):
        #print (grid[x,y])
        if grid[x,y] < 10000:
            currentsquares += 1

      
currenttotal = currentsquares
output = currenttotal
print("Answer is " +str(output))
