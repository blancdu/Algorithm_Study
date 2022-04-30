'''
 메모리: 117948 KB, 시간: 296 ms
 2022.04.30
 by Alub
'''
# 탐색 가능
def safe(r, c, d):
    if 0 <= r < R and 0 <= c < C:
        if d == 0 and 0 <= r-1 < R and 0 not in walls[r][c]:
            return True
        elif d == 1 and 0 <= c+1 < C and 1 not in walls[r][c]:
            return True
        elif d == 2 and 0 <= r+1 < R and 0 not in walls[r+1][c]:
            return True
        elif d == 3 and 0 <= c-1 < C and 1 not in walls[r][c-1]:
            return True
    return False

# 난방효과
def heat(heater, r, c, d, v):
    heater[r][c] += v
    if v > 1:
        # 정면
        nr, nc = r + dr[d], c + dc[d]
        if safe(r, c, d) and not visited[nr][nc]:
            visited[nr][nc] = True
            heat(heater, nr, nc, d, v-1)
        # 대각1
        nd = (d - 1) % 4
        nr1, nc1 = r + dr[nd], c + dc[nd]
        nr2, nc2 = nr1 + dr[d], nc1 + dc[d]
        if safe(r, c, nd) and safe(nr1, nc1, d) and not visited[nr2][nc2]:
            visited[nr2][nc2] = True
            heat(heater, nr2, nc2, d, v-1)
        # 대각2
        nd = (d + 1) % 4
        nr1, nc1 = r + dr[nd], c + dc[nd]
        nr2, nc2 = nr1 + dr[d], nc1 + dc[d]
        if safe(r, c, nd) and safe(nr1, nc1, d) and not visited[nr2][nc2]:
            visited[nr2][nc2] = True
            heat(heater, nr2, nc2, d, v - 1)

# main
dr, dc = (-1, 0, 1, 0), (0, 1, 0, -1)
R, C, K = map(int, input().split())
board = [[int(x) for x in input().split()] for _ in range(R)]
W = int(input())
walls = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(W):
    r, c, t = map(int, input().split())
    walls[r-1][c-1].append(t)

# board 수정
conv = (-1, 1, 3, 0, 2, -1)
check_area = []
for r in range(R):
    for c in range(C):
        if board[r][c] == 5:
            check_area.append((r, c))
        board[r][c] = conv[board[r][c]]

# 난방
heater = [[0] * C for _ in range(R)]
for r in range(R):
    for c in range(C):
        if board[r][c] != -1:
            visited = [[False] * C for _ in range(R)]
            d = board[r][c]
            if safe(r, c, d):
                nr, nc = r + dr[d], c + dc[d]
                heat(heater, nr, nc, d, 5)

heat_board = [[0] * C for _ in range(R)]
answer = 0
for _ in range(101):
    #1.
    for r in range(R):
        for c in range(C):
            heat_board[r][c] += heater[r][c]
    #2.
    temp_board = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            temp_board[r][c] += heat_board[r][c]
            for d in range(4):
                if safe(r, c, d):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < R and 0 <= nc < C and heat_board[r][c] - heat_board[nr][nc] > 0:
                        diff = (heat_board[r][c] - heat_board[nr][nc]) // 4
                        temp_board[r][c] -= diff
                        temp_board[nr][nc] += diff
    heat_board = temp_board
    #3.
    for r in range(R):
        for c in range(C):
            if r == 0 or r == R-1 or c == 0 or c == C-1:
                if heat_board[r][c] >= 1:
                    heat_board[r][c] -= 1
    #4.
    answer += 1
    #5.
    for r, c in check_area:
        if heat_board[r][c] < K:
            break
    else:
        break

print(answer)