def solution(arr):
    answer = []
    min = 999
    for i in range(len(arr)):
        answer.append(arr[i])
        if arr[i] < min:
            min = arr[i]
    answer.remove(min)
    
    if len(answer) == 0:
        answer.append(-1)
    return answer