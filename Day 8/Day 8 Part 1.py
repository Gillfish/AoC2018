file = open("Day 8 Puzzle Input.txt","r")
#file = open("Day 8 Puzzle Input Test Data.txt","r")

puzzlein = file.read().split()
nodes = []
for i in puzzlein:
    nodes.append(int(i))
output = "End"
finalchild = 0
finaltot = 0
finalremain = []


def parsenode( arr ):
    rettot = 0
    child, meta = arr[:2]
    remain = arr[2:]
    for ele in range(child):
        total, remain = parsenode(remain)
        rettot += total
    rettot += sum(remain[:meta])
    return(rettot, remain[meta:])
  

finaltot, finalremain = parsenode(nodes)
print(finaltot)

print(output)
