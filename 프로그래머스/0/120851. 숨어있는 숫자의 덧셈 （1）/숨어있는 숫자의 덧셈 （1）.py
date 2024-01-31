def solution(my_string):
    answer = 0
    for i in range(len(my_string)):
        if my_string[i].isdigit() == True:
            answer += int(my_string[i])
    return answer