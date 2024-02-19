def solution(n):
    n = str(n)
    answer = [0]*len(n)
    for i in range(len(n)):
        answer[i] = int(n[len(n)-1-i])
    return answer