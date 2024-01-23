import sys
sys.stdin = open('이모티콘.txt', 'r')

S = int(input())
visited = [[0]*1001 for _ in range(1001)]

def bfs():
    queue = [(1, 0)]  # start with one emoticon and empty clipboard
    while queue:
        s, c = queue.pop(0)
        if s == S:
            return visited[s][c]
        for ns, nc in [(s, s), (s+c, c), (s-1, c)]:  # copy all, paste, delete one
            if 0 < ns < 1001 and not visited[ns][nc]:
                visited[ns][nc] = visited[s][c] + 1
                queue.append((ns, nc))

#s는 현재 화면의 이모티콘 수, c는 클립보드에 복사된 이모티콘의 수

print(bfs())
