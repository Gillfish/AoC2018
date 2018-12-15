#input files
file = open("Day 5 Puzzle Input.txt","r")
#file = open("Day 5 Puzzle Input Test Data.txt","r")

#Global var setups
input = file.read().strip()
output = input
rebuiltoutput = []
rebuiltoutputstr = ""
pairsfound = 0
outputlength = len(output) - 1
skipnext = False
#print(outputlength)
nopairs = False

#Function definitions

def CheckPair( chara, charb ):
    delete = False
    #print (chara, charb)
    if chara.isupper() == True:
        if charb.isupper() == False:
            if chara == charb.upper():
                delete = True
    else:
        if charb.isupper() == True:
            if chara == charb.lower():
                delete = True
    return delete

#Main code

while nopairs == False:
    pairsfound = 0
    rebuiltoutput = []
    for i in range(outputlength):
        if skipnext == False:
            if CheckPair(output[i], output[i+1]) == False:
                if i == outputlength -1:
                    rebuiltoutput.append(output[i])
                    rebuiltoutput.append(output[i+1])
                else:
                    rebuiltoutput.append(output[i])  
            else:
                pairsfound += 1
                skipnext = True
        else:
            skipnext = False

    if pairsfound == 0:
        nopairs = True
    rebuiltoutputstr = ""
    for i in range(len(rebuiltoutput)):
        rebuiltoutputstr = rebuiltoutputstr + rebuiltoutput[i]
    output = rebuiltoutputstr
    outputlength = len(output) - 1
        
print (rebuiltoutput)
output = len(rebuiltoutputstr)
print(output)
