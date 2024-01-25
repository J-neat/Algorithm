def solution(my_string):
    answer = ''
    for i in range(len(my_string)):
        answer += my_string[len(my_string)-i-1]
    return answer