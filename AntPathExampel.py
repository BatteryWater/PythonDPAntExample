'''
DP example for ant pathing problem
'''
def CalcDistance(maxX, maxY, x, y):
    return abs(x/maxX - y/maxY)

def DictCombine(currentDict, otherDict, d):
    for D, count in otherDict.items():
        if D > d:
            if D not in currentDict:
                currentDict[D] = 0
            currentDict[D] += count
        else:
            if d not in currentDict:
                currentDict[d] = 0
            currentDict[d] += count
  

def AntPathing(maxX, maxY):
    if(maxX == 0) or (maxY == 0):
        return 0
    
    current = [] #we'll store only two columns in memory
    
    for y in range(0, maxY+1):
        current.append({CalcDistance(maxX, maxY, 0, y) : 1})
        
    for x in range(1, maxX+1):
        last = current
        current = []
        current.append({CalcDistance(maxX, maxY, x, 0) : 1})
        for y in range(1, maxY+1):
            d = CalcDistance(maxX, maxY, x, y)
            current.append({})
            DictCombine(current[y], current[y-1], d)
            DictCombine(current[y], last[y], d)
            
    LastPointDict = current[-1]
    Sum = 0.0
    Count = 0
    for pathValue, pathCount in LastPointDict.items():
        Sum += (pathValue * pathCount)
        Count += pathCount
        
    print ('Total D: ', Sum)
    print('Paths: ', Count)
    print('Average D:', Sum/Count)
