def solution(myString):
    answer = ''
    for i in range(len(myString)):
        answer += myString[i].lower()
    return answer