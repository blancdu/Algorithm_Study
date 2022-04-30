'''
 메모리: 115136 KB, 시간: 124 ms
 2022.04.30
 by Alub
'''
def find_area(y, x, visited):
    ret = [(y, x)]
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == board[y][x] and not visited[ny][nx]:
            visited[ny][nx] = True
            ret += find_area(ny, nx, visited)
    return ret


dy, dx = (0, 1, 0, -1), (1, 0, -1, 0)
N, M, K = map(int, input().split())
board = [[int(x) for x in input().split()] for _ in range(N)]
score_board = [[0] * M for _ in range(N)]
for y in range(N):
    for x in range(M):
        if not score_board[y][x]:
            visited = [[False] * M for _ in range(N)]
            visited[y][x] = True
            area = find_area(y, x, visited)
            for y1, x1 in area:
                score_board[y1][x1] = len(area) * board[y][x]

dice = [1, 2, 3, 4, 5, 6]
right = (3, 1, 0, 5, 4, 2)
down = (1, 5, 2, 3, 0, 4)
left = (2, 1, 5, 0, 4, 3)
up = (4, 0, 2, 3, 5, 1)
roll = [right, down, left, up]

y, x = 0, 0
d = 0
answer = 0
for _ in range(K):
    # 1. 이동 & 주사위 회전
    ny, nx = y + dy[d], x + dx[d]
    if 0 <= ny < N and 0 <= nx < M:
        y, x = ny, nx
    else:
        d = (d + 2) % 4
        y, x = y + dy[d], x + dx[d]
    dice = [dice[roll[d][i]] for i in range(6)]

    # 2. 점수 획득
    answer += score_board[y][x]

    # 3. 이동 방향 결정
    A, B = dice[-1], board[y][x]
    if A > B:
        d = (d + 1) % 4
    elif A < B:
        d = (d - 1) % 4

print(answer)