def solution(s):
    last_seen = {}  # 문자를 key로, 마지막으로 나타난 위치를 value로 하는 dictionary
    answer = []  # 결과를 저장할 list

    for i in range(len(s)):
        if s[i] in last_seen:  # 문자가 이전에 나타났다면
            answer.append(i - last_seen[s[i]])  # 현재 위치와 마지막으로 나타난 위치의 차이를 추가
        else:  # 문자가 처음 나타났다면
            answer.append(-1)  # -1을 추가
        last_seen[s[i]] = i  # 문자의 마지막 위치를 업데이트

    return answer
