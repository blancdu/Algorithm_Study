'''
 메모리: 116544 KB, 시간: 184 ms
 2022.05.02
 by Alub
'''
from collections import deque


def rotate_90(list_2d):
    return [list(x) for x in zip(*list_2d[::-1])]

def rotate_180(list_2d):
    return [x[::-1] for x in list_2d[::-1]]

def board_to_list(board):
    fish_list = []
    for c in range(len(board[-1])):
        for r in range(len(board)-1, -1, -1):
            try:
                fish_list.append(board[r][c])
            except IndexError:
                continue
    return fish_list

def fish_move(board):
    move_amount = [[0] * len(board[-1]) for _ in range(len(board))]
    for r in range(len(board)):
        for c in range(len(board[-1])):
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr and 0 <= nc:
                    try:
                        diff = (board[r][c] - board[nr][nc]) // 5
                        if diff > 0:
                            move_amount[r][c] -= diff
                            move_amount[nr][nc] += diff
                    except IndexError:
                        continue
    for r in range(len(board)):
        for c in range(len(board[-1])):
            if move_amount[r][c]:
                board[r][c] += move_amount[r][c]


dr, dc = (-1, 1, 0, 0), (0, 0, -1, 1)
N, K = map(int, input().split())
fish_list = deque([int(x) for x in input().split()])
answer = 1
while True:
    min_fish = min(fish_list)
    for i, v in enumerate(fish_list):
        if v == min_fish:
            fish_list[i] += 1
    # list to board
    board = [[fish_list.popleft()]]
    while len(fish_list) >= len(board):
        for i in range(len(board)-1, -1, -1):
            board[i].append(fish_list.popleft())
        board = rotate_90(board)
    board[-1].extend(fish_list)
    # fishmove
    fish_move(board)
    fish_list = board_to_list(board)
    # list to board
    board = [
        fish_list[(len(fish_list)//2)-1::-1],
        fish_list[len(fish_list)//2:]
    ]
    board = [
        *rotate_180([x[:len(board[0])//2] for x in board]),
        *[x[len(board[0])//2:] for x in board]
    ]
    # fishmove
    fish_move(board)
    fish_list = board_to_list(board)
    
    if max(fish_list) - min(fish_list) <= K:
        break
    else:
        fish_list = deque(fish_list)
        answer += 1
        
print(answer)