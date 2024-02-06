def solution(balls, share):
    answer = 0
    num1 = 1
    num3 = 1
    howmany = 0
    howmany = balls - share
    for i in range(howmany):
        num1 *= (balls - i)
        num3 *= (howmany-i)
    answer = num1 // num3
    return answer