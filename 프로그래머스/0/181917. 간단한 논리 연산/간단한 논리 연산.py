def solution(x1, x2, x3, x4):
    answer = True
    x5 = x1 or x2
    x6 = x3 or x4
    answer = x5 and x6
    return answer