'''
 메모리: 113112 KB, 시간: 108 ms
 2022.04.29
 by Alub
'''
N = int(input())
q = N
expo = 0
answer = [0] * 10
while q >= 1:
    q, mod = q // 10, q % 10
    for i in range(10):
        answer[i] += q * (10**expo)
        if i < mod:
            answer[i] += (10**expo)
        elif i == mod:
            answer[i] += (N % (10**expo)) + 1
    expo += 1
answer[0] -= int('1'*expo)
print(*answer)