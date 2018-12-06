file = open("day 1 puzzle input.txt","r")

input = file.readlines()

output = 0
frequencies = []
found = False

while found == False:
    for item in input:
        if frequencies.count(output) > 1:
            found = True
            print ("output is", output)
            break
        output = output + int(item)
        frequencies.append(output)
    

print(output)

