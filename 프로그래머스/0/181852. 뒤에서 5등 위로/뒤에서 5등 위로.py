def solution(num_list):
    answer = []
    num_list.sort()
    for i in range(5):
        num_list.pop(0)
    
    answer = num_list
    return answer