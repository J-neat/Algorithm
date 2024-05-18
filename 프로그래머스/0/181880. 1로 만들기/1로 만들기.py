def solution(num_list):
    answer = 0    
    for i in num_list:
        count = 0
        while i != 1:
            count += 1
            if i % 2 == 0:
                i = i / 2
            else:
                i = (i - 1) / 2
        answer += count
    
    return answer