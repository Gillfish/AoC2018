file = open("day 1 puzzle input.txt","r")

input = file.readlines()

output = 0

for line in input:
    output = output + int(line)

print(output)
