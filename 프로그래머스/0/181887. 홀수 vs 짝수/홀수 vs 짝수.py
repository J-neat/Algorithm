def solution(num_list):
    answer = 0
    odd = 0
    even = 0
    for i in range(len(num_list)):
        if (i+1) % 2 == 1:
            odd += num_list[i]
        else:
            even += num_list[i]
    
    answer = max(odd, even)
    return answer