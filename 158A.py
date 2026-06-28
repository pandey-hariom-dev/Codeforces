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

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    dp = [[-10**9] * n for _ in range(n)]

    for i in range(n):
        if s[i] == 'T':
            dp[i][i] = -1
        elif s[i] == 'F':
            dp[i][i] = 1
        else:  # N
            dp[i][i] = 1

    for length in range(2, n + 1):
        for l in range(n - length + 1):
            r = l + length - 1

            if s[l] == 'T':
                left = -1
            elif s[l] == 'F':
                left = 1
            else:
                left = 1

            if s[r] == 'T':
                right = -1
            elif s[r] == 'F':
                right = 1
            else:
                right = 1

            dp[l][r] = max(
                left + dp[l + 1][r],
                right + dp[l][r - 1]
            )

    total = 0
    for c in s:
        if c == 'T':
            total += 1
        elif c == 'F':
            total -= 1

    best = 0
    for l in range(n):
        for r in range(l, n):
            best = max(best, dp[l][r])

    ans = (n - total - best) // 2
    print(ans)