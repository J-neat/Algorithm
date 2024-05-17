def solution(myString):
    answer = ''
    for i in range(len(myString)):
        if myString[i] in ["a", "b", "c", "d", "e", "f", "g", "h", "h", "i", "j", "k"]:
            answer += "l"
        else:
            answer += myString[i]
    return answer