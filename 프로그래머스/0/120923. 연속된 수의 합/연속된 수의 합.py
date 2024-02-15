def solution(num, total):
    answer = [-1]*num
    mid = 0
    mid = total//num
    if total % num == 0:
        for i in range(num):
            answer[i] = mid - (num//2-i)
    else:
        for i in range(num):
            answer[i] = mid - (num//2 -i -1)
    return answer