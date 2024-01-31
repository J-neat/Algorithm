def solution(array):
    answer = 0
    # 원소 1개씩
    set_array = set(array)
    
    max_count = 0
    # 각 원소의 개수를 구하고 가장 많은 개수를 가지고 있는
    # 원소를 저장, 같으면 -1
    for i in set_array:
        count = array.count(i)
        if max_count < count:
            max_count = count
            answer = i
        elif max_count == count:
            answer = -1
    return answer