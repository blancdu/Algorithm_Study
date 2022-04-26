'''
 메모리: 115264 KB, 시간: 152 ms
 2022.04.26
 by Alub
'''
def calc_build_time(idx):
    if not dp[idx]:
        dp[idx] = build_time[idx] + max([calc_build_time(x) for x in pre_build[idx]], default=0)
    return dp[idx]

N = int(input())
build_time = [0] * (N+1)
dp = [0] * (N+1)
pre_build = [[] for _ in range(N+1)]
for i in range(1, 1 + N):
    t, *p = map(int, input().split())
    if p:
        p.pop()
    build_time[i], pre_build[i] = t, p
for i in range(1, 1 + N):
    print(calc_build_time(i))