
def solution(array):
    max = -999
    max_i = -999
    answer = []
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
            max_i = i
    answer.append(max)
    answer.append(max_i)    
    return answer