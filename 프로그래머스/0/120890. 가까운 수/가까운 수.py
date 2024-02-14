def solution(array, n):
    answer = 0
    dif = 999
    array.sort()
    for i in range(len(array)):
        if abs(n - array[i]) < dif:
            dif = abs(n - array[i])
            answer = array[i]
    return answer