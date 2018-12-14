file = open("Day 2 puzzle input.txt","r")

input = file.readlines()
output = 0
boxidlength = len(input[0]) -1
#all boxids are same length - taking advantage of this to loop through each char
trimmedlist = []
trimmedid = ""
Chartoreplace = ""
trimmedlistid = 0

for position in range(boxidlength):
    for boxid in input:
    trimmedlistid = len(trimmedlist) -1
    for i in range(trimmedlistid):
        if trimmedlist.count(trimmedlist[i]) > 1:
            print("Shared values are: ", trimmedlist[i])
    trimmedlist.clear()

print(output)

