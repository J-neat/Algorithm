import math
def solution(num_list):
    answer = 0
    num1 = 1
    num2 = 0
    for i in range(len(num_list)):
        num1 *= num_list[i]
        num2 += num_list[i]
    
    num2 = num2*num2
    
    if num1 < num2:
        answer = 1
    return answer