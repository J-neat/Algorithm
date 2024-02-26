def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        sliced = array[i-1:j]
        sliced.sort()
        answer.append(sliced[k-1])
    return answer
