
def solution(strArr):
    answer = 0
    cntDict = dict()
    for s in strArr:
        if len(s) in cntDict.keys():
            cntDict[len(s)] += 1
        else:
            cntDict[len(s)] = 1
    answer = max(cntDict.values()) 
    return answer