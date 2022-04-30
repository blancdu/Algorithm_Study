'''
 메모리: 118192 KB, 시간: 244 ms
 2022.05.01
 by Alub
'''
from collections import Counter


def can_move(r, c):
    if 0 <= r < 4 and 0 <= c < 4 and not smell[r][c] and (r != shark[0] or c != shark[1]):
        return True
    return False

def shark_move(r, c, cnt = 0, route = [], depth = 0):
    global eat_fish, shark_route
    if depth == 0:
        for d in (2, 0, 6, 4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < 4 and 0 <= nc < 4:
                shark_move(nr, nc, 0, [], depth + 1)
        return
    elif depth == 3:
        sub_ans = cnt + sum(after_move[r][c].values())
        if sub_ans > eat_fish:
            eat_fish = sub_ans
            shark_route = route + [(r, c)]
        return
    for d in (2, 0, 6, 4):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < 4 and 0 <= nc < 4:
            after_move[r][c], temp = Counter(), after_move[r][c]
            shark_move(nr, nc, cnt + sum(temp.values()), route + [(r, c)], depth + 1)
            after_move[r][c] = temp


dr, dc = (0, -1, -1, -1, 0, 1, 1, 1), (-1, -1, 0, 1, 1, 1, 0, -1)
M, S = map(int, input().split())
fish = [[Counter() for _ in range(4)] for _ in range(4)]
for _ in range(M):
    r, c, d = map(int, input().split())
    fish[r-1][c-1] += Counter([d-1])
shark = [int(x) - 1 for x in input().split()]

smell = [[0] * 4 for _ in range(4)]
for _ in range(S):
    # fish move
    after_move = [[Counter() for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            for f, cnt in fish[r][c].items():
                for i in range(8):
                    d = (f - i) % 8
                    nr, nc = r + dr[d], c + dc[d]
                    if can_move(nr, nc):
                        after_move[nr][nc] += Counter({d:cnt})
                        break
                else:
                    after_move[r][c] += Counter({f:cnt})

    # shark move
    eat_fish = -1
    shark_route = []
    shark_move(*shark)
    shark = shark_route[-1]
    for r, c in shark_route:
        if after_move[r][c]:
            smell[r][c] = 3
            after_move[r][c] = Counter()

    # smell down & copy fish
    for r in range(4):
        for c in range(4):
            # smell down
            if smell[r][c]:
                smell[r][c] -= 1
            # copy fish
            if after_move[r][c]:
                fish[r][c] += after_move[r][c]

answer = 0
for r in range(4):
    for c in range(4):
        answer += sum(fish[r][c].values())
print(answer)