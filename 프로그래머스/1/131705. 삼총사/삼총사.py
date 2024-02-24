from itertools import combinations
def solution(number):
    answer = 0
    my_list = list(combinations(number, 3))
    for i in my_list:
        if sum(i) == 0:
            answer += 1        

    return answer