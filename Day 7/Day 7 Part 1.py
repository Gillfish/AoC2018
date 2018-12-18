file = open("Day 7 Puzzle Input.txt","r")
#file = open("Day 7 Puzzle Input Test Data.txt","r")

puzzlein = file.readlines()
output = ""
uniquesteps = []
stepsnotdone = 0
checksteps = []
steptodo = []
order = []
fullyordered = False


def getsteptodo(str):
    step = str.split(" ")
    step = step[7]
    return step

def getstepneeded(str):
    step = str.split(" ")
    step = step[1]
    return step

for line in puzzlein:
    sn = getstepneeded(line)
    st = getsteptodo(line)
    steptodo.append(st)
    if sn not in uniquesteps:
        uniquesteps.append(sn)
    if st not in uniquesteps:
        uniquesteps.append(st)

uniquesteps = sorted(uniquesteps)


#print(uniquesteps)
#uniquesteps.pop(0)wor
#print(uniquesteps)

while fullyordered == False:
    for step in uniquesteps:
        checksteps = []
        if step not in steptodo:
            if step not in order:
                order.append(step)
                break
        else:
            for line in puzzlein:
                sn = getstepneeded(line)
                st = getsteptodo(line)
                if st == step:
                    checksteps.append(sn)
            stepsnotdone = 0
            for check in checksteps:
                if check not in order:
                    stepsnotdone += 1
            if stepsnotdone == 0:
                if step not in order:
                    order.append(step)
                    break
    if len(order) == len(uniquesteps):
        fullyordered = True


#check each line
        
for step in order:
    output = output+step
print(output)
