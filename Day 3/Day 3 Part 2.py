file = open("Day 3 puzzle input.txt","r")
#file = open("Day 3 puzzle input test data.txt","r")

input = file.readlines()
output = "0"
printxaxis = 0
printyaxis = 0
printxlength = 0
printylength = 0
Squares = {}
for test in range(1000):
    for test2 in range(1000):
        Squares[test,test2] = 0

def getclaimid( str ):
    claimid = str.split(" @ ")
    claimid = claimid[0].split("#")
    claimid = claimid[1]
    return claimid

def getxstart( str ):
    xstart = str.split("@ ")
    xstart = xstart[1].split(",")
    xstart = xstart[0]
    return int(xstart)

def getystart( str ):
    ystart = str.split("@ ")
    ystart = ystart[1].split(",")
    ystart = ystart[1].split(": ")
    ystart = ystart[0]
    return int(ystart)

def getxlength( str ):
    xlength = str.split("@ ")
    xlength = xlength[1].split(",")
    xlength = xlength[1].split(": ")
    xlength = xlength[1].split("x")
    xlength = xlength[0]
    return int(xlength)

def getylength( str ):
    ylength = str.split("@ ")
    ylength = ylength[1].split(",")
    ylength = ylength[1].split(": ")
    ylength = ylength[1].split("x")
    ylength = ylength[1]
    return int(ylength)

for claim in input:
    printxaxis = getxstart(claim)
    printyaxis = getystart(claim)
    printxlength = getxlength(claim)
    printylength = getylength(claim)
    for x in range(printxlength):
        xcoord = x+printxaxis
        for y in range(printylength):
            ycoord = y+printyaxis
            Squares[xcoord,ycoord] += 1
            
found = False

for claim in input:
    found = True
    printxaxis = getxstart(claim)
    printyaxis = getystart(claim)
    printxlength = getxlength(claim)
    printylength = getylength(claim)
    for x in range(printxlength):
        xcoord = x+printxaxis
        for y in range(printylength):
            ycoord = y+printyaxis
            if Squares[xcoord,ycoord] != 1:
                found = False
    if found == True:
        output = getclaimid(claim)
        break



print(output)
