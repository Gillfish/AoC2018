file = open("Day 2 puzzle input.txt","r")

input = file.readlines()
output = 0
countthreelet = 0
counttwolet = 0
counttwo = 0
countthree = 0

for boxid in input:
    for letter in boxid:
        count = boxid.count(letter)
        if count == 2:
            counttwolet += 1
        if count == 3:
            countthreelet += 1
    if counttwolet > 0:
        counttwo += 1
        counttwolet = 0
    if countthreelet > 0:
        countthree += 1
        countthreelet = 0

output = counttwo * countthree
print(output)

