def solution(k, score):
    answer = [score[0]]
    honor = [score[0]]
    for i in range(1, len(score)):
        honor.append(score[i]) # 현재 점수를 무조건 honor에 추가
        # honor에 k+1개의 점수가 있다면, 가장 낮은 점수를 제거
        if len(honor) > k:
            honor.remove(min(honor))
        answer.append(min(honor))
    return answer
