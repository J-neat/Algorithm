def solution(num_list):
    answer = []
    num1, num2 = 0, 0
    for i in range(len(num_list)):
        if num_list[i]%2 == 0:
            num1 += 1
        elif num_list[i]%2==1:
            num2 += 1
    answer.append(num1)
    answer.append(num2)
    return answer