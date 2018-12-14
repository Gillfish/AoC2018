#input files
file = open("Day 4 Puzzle Input.txt","r")
#file = open("Day 4 Puzzle Input Test Data.txt","r")

#Global var setups
input = file.readlines()
input.sort()
output = 0
totalguards = []
entryno = 0
dayrow = 0
sleep = 0
wake = 0
naplength = 0
timeasleep = 0
longesttime = 0
sleepyguard = 0
sleepmin = 0
sleepmincount = 0
prevsleepmincount = 0
finalsleepmincount = 0
finalsleepmin = 0
asleep = False
currentday = ""
prevday = ""
totaldays = 0

#Function definitions

def getguardid( str ):
    guardid = str.split("#")
    guardid = guardid[1].split(" ")
    guardid = guardid[0]
    return int(guardid)

def getlog( str ):
    log = str.split("] ")
    log = log[1]
    return log

def getmonth( str ):
    month = str.split("-")
    month = month[1]
    return month

def getday( str ):
    day = str.split("-")
    day = day[2].split(" ")
    day = day[0]
    return day

def getminute( str ):
    minute = str.split(":")
    minute = minute[1].split("]")
    minute = minute[0]
    return int(minute)

for entries in input:
    currentday = getmonth(entries) + getday(entries)
    if currentday != prevday:    
        totaldays += 1
        prevday = currentday

#totaldays -= 1

chart = {}
for test in range(62):
    #60 minutes + day id + guard ID
    for test2 in range(totaldays):
        #total days in actual data
        chart[test,test2] = 0

#main code


for entry in input:
    if getlog(entry)[0] == "G":
        if entryno != 0:
            dayrow += 1
        chart[1,dayrow] = getguardid(entry)
        if getguardid(entry) not in totalguards:
            totalguards.append(getguardid(entry))
    if getlog(entry)[0] == "f":
        sleep = getminute(entry)
        asleep = True
    if getlog(entry)[0] == "w":
        wake = getminute(entry)
        asleep = False
        naplength = wake - sleep
        for i in range(naplength):
            chart[sleep+i+2,dayrow] = 1
    if asleep == True:
        chart[getminute(entry)+2,dayrow] = 1
    entryno += 1

for guards in totalguards:
    timeasleep = 0
    for days in range(totaldays):
        for mins in range(2,62):
            if chart[1,days] == guards:
                if chart[mins,days] > 0:
                    timeasleep += 1
    if timeasleep > longesttime:
        longesttime = timeasleep
        sleepyguard = guards
    #print("longest time asleep is: ", str(longesttime), "current time asleep is: ", str(timeasleep), "sleepiest guard is: ", sleepyguard, "current guard is: ", guards)

for guards in totalguards:
    prevsleepmincount = 0
    sleepmin = 0
    for minute in range(2, 62):
        sleepmincount = 0
        for day in range(totaldays):
            if chart[1,day] == guards:
                if chart[minute,day] == 1:
                    sleepmincount += 1
        
        if sleepmincount > prevsleepmincount:
            prevsleepmincount = sleepmincount
            sleepmin = minute - 2 #offset
    if prevsleepmincount > finalsleepmincount:
        finalsleepmincount = prevsleepmincount
        finalsleepmin = sleepmin
        sleepyguard = guards
        
#end of file - should be result
print("sleepiest guard is: " + str(sleepyguard))
print("minute most asleep is: " + str(finalsleepmin))
print("asleep at that minute: " + str(finalsleepmincount), " times")
output = sleepyguard * finalsleepmin
print(output)
