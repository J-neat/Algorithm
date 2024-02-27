def solution(n, words):
    check = [words[0]] # 첫 번째 단어는 미리 체크에 넣어둡니다.
    for i in range(1, len(words)): # 두 번째 단어부터 체크합니다.
        if words[i] in check or words[i-1][-1] != words[i][0]: # 이미 말한 단어를 다시 말하거나, 끝말잇기 규칙을 어기면
            return [(i % n) + 1, (i // n) + 1] # 순서와 차례를 반환합니다.
        check.append(words[i]) # 단어를 체크리스트에 추가합니다.
    return [0, 0] # 모두 통과하면 [0, 0]을 반환합니다.
