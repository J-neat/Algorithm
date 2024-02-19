from itertools import combinations

def solution(numbers):
    answer = []
    nums = list(combinations(numbers, 2))
    for i in range(len(nums)):
        num = sum(nums[i])
        if num not in answer:
            answer.append(num)
    answer.sort()
    return answer
