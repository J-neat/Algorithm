def solution(myString):
    answer = []
    answer = myString.split("x")
    for i in range(len(answer)):
        answer[i] = len(answer[i])
    return answer