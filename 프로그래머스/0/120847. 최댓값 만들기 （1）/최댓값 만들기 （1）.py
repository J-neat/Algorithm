def solution(numbers):
    answer = 0
    numbers.sort()
    answer = numbers[len(numbers)-1]*numbers[len(numbers)-2]
    return answer