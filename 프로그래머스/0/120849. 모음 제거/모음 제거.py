def solution(my_string):
    answer = ''
    mother = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(my_string)):
        if my_string[i] not in mother:
            answer += my_string[i]
    return answer