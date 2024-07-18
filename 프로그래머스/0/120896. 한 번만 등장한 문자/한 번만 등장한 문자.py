def solution(s):
    answer = ''
    ans = []
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            ans.append(s[i])
    ans.sort()
    for j in range(len(ans)):
        answer += ans[j]
    return answer