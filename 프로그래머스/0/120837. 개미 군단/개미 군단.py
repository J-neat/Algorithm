def solution(hp):
    answer = 0
    if hp % 5 >= 0:
        answer += (hp//5)
        hp = hp%5
        if hp %3 >= 0:
            answer += (hp//3)
            hp = hp%3
            if hp >= 0:
                answer += hp
            
    return answer