def solution(slice, n):
    answer = 0
    if n % slice > 0:
        answer = n//slice + 1
    elif n % slice == 0:
        answer = n //slice
    return answer