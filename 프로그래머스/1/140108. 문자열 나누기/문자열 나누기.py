def solution(s):
    answer = 0
    check1, check2 = 0, 0
    for i in s:
        if check1 == check2:
            answer += 1
            first = i
        if first == i:
            check1 += 1
        elif first != i:
            check2 += 1
    return answer