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
currentsquares = []
xloop = 0
yloop = 0
gridx = []
ignoredclaims = []

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
        grid[x,y] = "u, 0"

#populating grid
for line in puzzlein:
    claimid += 1
    currentx = int(getx(line))
    currenty = gety(line)
    grid[currentx, currenty] = str(claimid) + ", 0"
    for x in range(gridwidth):
        for y in range(gridheight):
            #positive x, positive y
            if currentx+x < gridwidth:
                if currenty+y < gridheight:
                    if getx(grid[currentx+x, currenty+y]) == "u":
                        #unclaimed square
                        grid[currentx+x, currenty+y] = str(claimid) + ", " + str(x+y)
                    elif gety(grid[currentx+x, currenty+y]) > x+y:
                        #claimed but further away from old square
                        grid[currentx+x, currenty+y] = str(claimid) + ", " + str(x+y)
                    elif gety(grid[currentx+x, currenty+y]) == x+y:
                        #claimed but distance is the same
                        if getx(grid[currentx+x, currenty+y]) != str(claimid):
                            grid[currentx+x, currenty+y] = "., " + str(x+y)
            #positive x, negative y
            if currentx+x < gridwidth:
                if currenty-y >= 0 and currenty-y < gridheight:
                    if getx(grid[currentx+x, currenty-y]) == "u":
                        #unclaimed square
                        grid[currentx+x, currenty-y] = str(claimid) + ", " + str(x+y)
                    elif gety(grid[currentx+x, currenty-y]) > x+y:
                        #claimed but further away from old square
                        grid[currentx+x, currenty-y] = str(claimid) + ", " + str(x+y)
                    elif gety(grid[currentx+x, currenty-y]) == x+y:
                        #claimed but distance is the same
                        if getx(grid[currentx+x, currenty-y]) != str(claimid):
                            grid[currentx+x, currenty-y] = "., " + str(x+y)
            #negative x, positive y
            if currentx-x >= 0 and currentx-x < gridwidth:
                if currenty+y < gridheight:
                    if getx(grid[currentx-x, currenty+y]) == "u":
                        #unclaimed square
                        grid[currentx-x, currenty+y] = str(claimid) + ", " + str(x+y)
                    elif gety(grid[currentx-x, currenty+y]) > x+y:
                        #claimed but further away from old square
                        grid[currentx-x, currenty+y] = str(claimid) + ", " + str(x+y)
                    elif gety(grid[currentx-x, currenty+y]) == x+y:
                        #claimed but distance is the same
                        if getx(grid[currentx-x, currenty+y]) != str(claimid):
                            grid[currentx-x, currenty+y] = "., " + str(x+y)
            #negative x, negative y
            if currentx-x >= 0 and currentx-x < gridwidth:
                if currenty-y >= 0 and currenty-y < gridheight:
                    if getx(grid[currentx-x, currenty-y]) == "u":
                        #unclaimed square
                        grid[currentx-x, currenty-y] = str(claimid) + ", " + str(x+y)
                    elif gety(grid[currentx-x, currenty-y]) > x+y:
                        #claimed but further away from old square
                        grid[currentx-x, currenty-y] = str(claimid) + ", " + str(x+y)
                    elif gety(grid[currentx-x, currenty-y]) == x+y:
                        #claimed but distance is the same
                        if getx(grid[currentx-x, currenty-y]) != str(claimid):
                            grid[currentx-x, currenty-y] = "., " + str(x+y)



for y in range(gridheight):
    if getx(grid[0,y]) not in ignoredclaims:
        ignoredclaims.append(getx(grid[0,y]))
    if getx(grid[gridwidth-1,y]) not in ignoredclaims:
        ignoredclaims.append(getx(grid[gridwidth-1,y]))
    for x in range(gridwidth):
        if getx(grid[x,0]) not in ignoredclaims:
            ignoredclaims.append(getx(grid[x,0]))
        if getx(grid[x,gridheight-1]) not in ignoredclaims:
            ignoredclaims.append(getx(grid[x,gridheight-1]))

print(ignoredclaims)

#getting answer
claimid = 0
for line in puzzlein:
    currentsquares = []
    claimid += 1
    if str(claimid) not in ignoredclaims:
        for x in range(gridwidth):
            for y in range(gridheight):
                if getx(grid[x,y]) != "u":
                    if getx(grid[x,y]) != ".":
                        if int(getx(grid[x,y])) == claimid:
                            currentsquares.append(grid[x,y])
        print ("currentsuares length is: " + str(len(currentsquares)) + ", claimid is: " + str(claimid))
        if len(currentsquares) > currenttotal:
            currenttotal = len(currentsquares)

output = currenttotal
print("Answer is " +str(output))
