# for _ in range(int(input())):
#     n, c = map(int, input().split())
#     a = [int(x) for x in input().split()]
#     b = [int(x) for x in input().split()]
    
#     o1 = all(x >= y for x, y in zip(a, b))
#     c1 = sum(x - y for x, y in zip(a, b)) if o1 else float('inf')
    
#     sa, sb = sorted(a), sorted(b)
#     o2 = all(x >= y for x, y in zip(sa, sb))
#     cost2 = c + sum(x - y for x, y in zip(sa, sb)) if o2 else float('inf')
    
#     time = min(c1, cost2)
#     print(time if time != float('inf') else -1)


import sys

MOD = 1000000007
MAXK = 200000

fac = [1] * (MAXK + 5)
for i in range(1, MAXK + 5):
    fac[i] = fac[i - 1] * i % MOD

ifac = [1] * (MAXK + 5)
ifac[MAXK + 4] = pow(fac[MAXK + 4], MOD - 2, MOD)
for i in range(MAXK + 4, 0, -1):
    ifac[i - 1] = ifac[i] * i % MOD


def C(n, r):
    if r < 0 or r > n:
        return 0
    return fac[n] * ifac[r] % MOD * ifac[n - r] % MOD


t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())

    if k == 1:
        print(1)
        continue

    bits = []
    x = k

    while x:
        bits.append(x & 1)
        x >>= 1

    m = len(bits) - 1

    if n < m:
        print(0)
        continue

    ans = 1
    rem = n - m

    ones = 0
    for i in range(m):
        if bits[i]:
            ones += 1

    ans = C(rem + ones, ones)

    print(ans % MOD)