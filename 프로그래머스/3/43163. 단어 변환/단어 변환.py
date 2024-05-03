from collections import deque
def solution(begin, target, words):
    answer = 0
    n = len(words)
    q = deque()
    q.append([begin, 0])
    visited = [0 for i in range(n)]
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(n):
            temp_cnt = 0
            if visited[i] == 0:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                        
                if temp_cnt == 1:
                    q.append([words[i], cnt+1])
                    visited[i] = 1
    
    return answer