'''
 메모리: 161316 KB, 시간: 304 ms
 2022.04.27
 by Alub
'''
from collections import deque

tc = int(input())
for _ in range(tc):
    command, n, nums_list = input(), int(input()), input()[1:-1].split(',')
    nums = deque(nums_list if n else [])
    d = 1
    try:
        for cmd in command:
            if cmd == 'R':
                d *= -1
            else:
                if d == 1:
                    nums.popleft()
                else:
                    nums.pop()
        print(f"[{','.join(list(nums)[::d])}]")
    except:
        print('error')