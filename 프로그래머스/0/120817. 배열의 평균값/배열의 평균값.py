def solution(numbers):
    answer = 0
    for i in range(0, len(numbers)):
        answer += numbers[i]
    answer = answer / len(numbers)
    return answer