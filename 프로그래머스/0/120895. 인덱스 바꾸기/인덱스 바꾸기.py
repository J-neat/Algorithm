def solution(my_string, num1, num2):
    answer = ''
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    for i in range(len(my_string)):
        answer += my_string[i]
    
    return answer