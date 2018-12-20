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
    retval = []
    child, meta = arr[:2]
    remain = arr[2:]
    for ele in range(child):
        total, remain = parsenode(remain)
        retval.append(total)
    if child == 0:
        return(sum(remain[:meta]), remain[meta:])
    else:
        return(sum(retval[k - 1] for k in remain[:meta] if k > 0 and k <= len(retval)), remain[meta:])
  

finaltot, finalremain = parsenode(nodes)
print(finaltot)

print(output)
