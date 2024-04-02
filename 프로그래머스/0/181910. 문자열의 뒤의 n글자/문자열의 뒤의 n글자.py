def solution(my_string, n):
    answer = ''
    for i in range(len(my_string)-n, len(my_string)):
        answer += my_string[i]
    return answer