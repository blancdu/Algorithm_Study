'''
 메모리: 115420 KB, 시간: 140 ms
 2022.04.30
 by Alub
'''
N, M = map(int, input().split())
m = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
dp = [0] * (sum(c)+1)
answer = float('inf')
for i in range(N):
    for j in range(sum(c), -1, -1):
        if j - c[i] >= 0:
            dp[j] = max(dp[j], dp[j-c[i]]+m[i])
        if dp[j] >= M and j < answer:
            answer = j
print(answer)