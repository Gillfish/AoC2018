#input files
file = open("Day 5 Puzzle Input.txt","r")
#file = open("Day 5 Puzzle Input Test Data.txt","r")

#Global var setups
input = file.read()
output = input
rebuiltoutput = []
rebuiltoutputstr = ""
pairsfound = 0
outputlength = len(output) - 1
skipnext = False
#print(outputlength)
nopairs = False
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

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

for letter in alphabet:
    file = open("Day 5 Puzzle Input.txt","r")
    input = file.read()
    output = input.replace(letter,"")
    output = output.replace(letter.upper(),"")
    outputlength = len(output) - 1
    nopairs = False
    while nopairs == False:
        pairsfound = 0
        rebuiltoutput = []
        for i in range(outputlength):
            if skipnext == False:
                if i == 0:
                    #first time round
                    if CheckPair (output[i], output[i+1]) == False:
                        rebuiltoutput.append(output[i])
                elif i == outputlength -1:
                    #last time round
                    if len(rebuiltoutput) != 0:
                        if CheckPair (output[i],rebuiltoutput[-1]) == False:
                            #check against last char in rebuilt output
                            if CheckPair (output[i], output[i+1]) == False:
                                #check against next character
                                rebuiltoutput.append(output[i])
                                rebuiltoutput.append(output[i+1])
                            else:
                                pairsfound += 1
                                skipnext = True
                        else:
                            rebuiltoutput.pop()
                            rebuiltoutput.append(output[i+1])
                    else:
                        if CheckPair (output[i], output[i+1]) == False:
                            #check against next character
                            rebuiltoutput.append(output[i])
                            rebuiltoutput.append(output[i+1])
                        else:
                            pairsfound += 1
                            skipnext = True
                else:
                    #most times
                    if len(rebuiltoutput) != 0:
                        if CheckPair (output[i],rebuiltoutput[-1]) == False:
                            #check against last char in rebuilt output
                            if CheckPair (output[i], output[i+1]) == False:
                                #check against next character
                                rebuiltoutput.append(output[i])
                            else:
                                pairsfound += 1
                                skipnext = True
                        else:
                            rebuiltoutput.pop()
                    else:
                        if CheckPair (output[i], output[i+1]) == False:
                            #check against next character
                            rebuiltoutput.append(output[i])
                        else:
                            pairsfound += 1
                            skipnext = True
            else:
                skipnext = False
        rebuiltoutputstr = ""
        for i in range(len(rebuiltoutput)):
            rebuiltoutputstr = rebuiltoutputstr + rebuiltoutput[i]
        output = rebuiltoutputstr
        outputlength = len(output) - 1
        if pairsfound == 0:
            nopairs = True
    output = len(rebuiltoutputstr)
    print(letter + ": " + str(output))
    rebuiltoutputstr = ""        

