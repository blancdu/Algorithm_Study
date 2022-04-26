'''
 메모리: 159848 KB, 시간: 680 ms
 2022.04.26
 by Alub
'''
import sys
input = sys.stdin.readline

def make_tree(left, right, idx=1):
    if left == right:
        tree[idx] = nums[left-1]
        return tree[idx]
    mid = (left + right) // 2
    tree[idx] = make_tree(left, mid, 2 * idx) + make_tree(mid + 1, right, 2 * idx + 1)
    return tree[idx]

def change_num(b, c, left, right, idx=1):
    if left==right:
        diff = c - tree[idx]
        tree[idx] += diff
        return diff
    mid = (left + right) // 2
    if b <= mid:
        diff = change_num(b, c, left, mid, 2*idx)
    else:
        diff = change_num(b, c, mid+1, right, 2*idx+1)
    tree[idx] += diff
    return diff

def part_sum(b, c, left, right, idx=1):
    if c < left or b > right:
        return 0
    elif b <= left <= right <= c:
        return tree[idx]
    else:
        mid = (left+right) // 2
        return part_sum(b, c, left, mid, 2*idx) + part_sum(b, c, mid+1, right, 2*idx+1)

N, M, K = map(int, input().split())
tree = [0] * (4 * N)
nums = [int(input()) for _ in range(N)]
make_tree(1, N)
for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        change_num(b, c, 1, N)
    else:
        print(part_sum(b, c, 1, N))
        
