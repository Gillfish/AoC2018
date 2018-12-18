file = open("Day 7 Puzzle Input.txt","r")
#file = open("Day 7 Puzzle Input Test Data.txt","r")

puzzlein = file.readlines()
output = ""
uniquesteps = []
stepsnotdone = 0
checksteps = []
steptodo = []
order = []
sip = []
sc = []
workers = 5
steptimelist = {}
steptime = 61
numsteps = 0
timetaken = 0
fullyordered = False
complete = False


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
numsteps = len(uniquesteps)


for step in range(numsteps):
    steptimelist[step,0] = uniquesteps[step]
    steptimelist[step,1] = steptime
    steptimelist[step,2] = 0
    steptime += 1
    

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


while complete == False:
    appended = False
    for step in order:
        checksteps = []
        if step not in steptodo:
            if step not in sc:
                if step not in sip:
                    if len(sip) < workers:
                        sip.append(step)
                        steptimelist[uniquesteps.index(step),2] = timetaken
                        appended = True
        else:
            for line in puzzlein:
                sn = getstepneeded(line)
                st = getsteptodo(line)
                if st == step:
                    checksteps.append(sn)
            stepsnotdone = 0
            for check in checksteps:
                if check not in sc:
                    stepsnotdone += 1
            if stepsnotdone == 0:
                if step not in sc:
                    if step not in sip:
                        if len(sip) < workers:
                            sip.append(step)
                            steptimelist[uniquesteps.index(step),2] = timetaken
                            appended = True
    if appended == False:
        timetaken += 1
    print("Timestamp: " + str(timetaken))
    print("Steps complete: " + str(sc))
    print("Steps in progress: " + str(sip))
    for step in sip:
        if timetaken >= int(steptimelist[uniquesteps.index(step),2]) + int(steptimelist[uniquesteps.index(step),1]):
            sc.append(sip[sip.index(step)])
            sip.pop(sip.index(step))
    if len(sc) == len(uniquesteps):
        complete = True

    
        
        

print(sc)
print(timetaken)
