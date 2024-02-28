def solution(food):
    answer = ''
    foods = ''
    for i in range(1, len(food)):
        foods += str(i) * (food[i]//2)
    
    answer = foods + '0' + foods[::-1]
    return answer