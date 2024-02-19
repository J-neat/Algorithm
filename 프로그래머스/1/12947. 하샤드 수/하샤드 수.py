def solution(x):
    answer = True
    x = str(x)
    n = len(x)
    n2 = 0
    for i in range(n):
        n2 += int(x[i])
        if int(x) % n2 == 0:
            answer = True
        else:
            answer = False
    return answer