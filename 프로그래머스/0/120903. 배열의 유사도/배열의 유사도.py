def solution(s1, s2):
    answer = 0
    for i in range(len(s1)):
        if s1[i] in s2:
            answer += 1
    return answer