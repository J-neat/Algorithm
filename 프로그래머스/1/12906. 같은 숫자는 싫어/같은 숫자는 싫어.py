def solution(arr):
    answer = [arr[0]]
    start = arr[0]
    for i in range(1, len(arr)):
        answer.append(arr[i])
        if start == arr[i]:
            answer.pop()
            start = arr[i]
        else:
            start = arr[i]
    return answer