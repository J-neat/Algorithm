rspdict = {
    "5" : "2",
    "2" : "0",
    "0" : "5"
}
    
def solution(rsp):
    answer = ''
    for i in range(len(rsp)):
        answer += rspdict[rsp[i]]
    return answer