def solution(n, k):
    answer = 0
    x = n // 10
    answer = 12000*n + 2000*(k-x)
    return answer
