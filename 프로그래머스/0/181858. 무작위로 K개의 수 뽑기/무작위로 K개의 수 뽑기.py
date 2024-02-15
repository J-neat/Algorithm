def solution(arr, k):
    answer = []
    for num in arr:
        if num not in answer and len(answer) < k:
            answer.append(num)
    while len(answer) < k:
        answer.append(-1)
    return answer
