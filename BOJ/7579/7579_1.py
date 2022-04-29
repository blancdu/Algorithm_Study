'''
 메모리: 122692 KB, 시간: 152 ms
 2022.04.30
 by Alub
'''
N, M = map(int, input().split())
m = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
dp = [[0] * (sum(c)+1) for _ in range(N)]
answer = float('inf')
for i in range(N):
    for j in range(sum(c)+1):
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-c[i]]+m[i]
                       ) if j - c[i] >= 0 else dp[i-1][j]
        if dp[i][j] >= M:
            answer = min(answer, j)
            break
print(answer)