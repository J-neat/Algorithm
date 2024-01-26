def solution(my_string, n):
    answer = ''
    for j in range(len(my_string)):
        for i in range(n):
            answer += my_string[j]
    return answer