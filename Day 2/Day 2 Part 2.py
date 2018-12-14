file = open("Day 2 puzzle input.txt","r")

input = file.readlines()
output = ''
output1 = ''
output2 = ''
differences = 0

for first in input:
    for second in input:
        differences = 0
        for i in range(len(second)):
            if first[i-1] != second[i-1]:
                differences += 1
        if differences == 1:
            print("first output is ", first, ", second output is ", second)
            output1 = first
            output2 = second
            break

for i in range(len(output1)):
    if output1[i-1] == output2[i-1]:
        output += output1[i-1]
print(output)
