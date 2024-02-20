def solution(s):
    answer = True
    check_p = 0
    check_y = 0
    for i in s:
        if i == 'p' or i == 'P':
            check_p += 1
        elif i == 'y' or i == 'Y':
            check_y += 1
    if check_p != check_y:
        answer = False
    
    return answer
