import sys

sys.stdin = open('로또.txt', 'r')

N, M = map(int,input().split())

dp = [[0 for _ in range(M+1)] for __ in range(N+1)]
for i in range(M+1):
    dp[1][i] = i

for i in range(2, N+1):
    for j in range(1, M+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j//2]

print(dp[N][M])
