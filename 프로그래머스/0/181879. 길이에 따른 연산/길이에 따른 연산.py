def solution(num_list):
    answer = 0
    num = 1
    if(len(num_list) >= 11):
        for i in range(len(num_list)):
            answer += num_list[i]
        return answer
    else:
        for i in range(len(num_list)):
            num *= num_list[i]
        return num