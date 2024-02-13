def solution(i, j, k):
    answer = 0
    for num in range(i, j + 1):
        for x in str(num):
            if x == str(k):
                answer += 1
    return answer