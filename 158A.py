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



def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())

        x = n
        ans = 0

        p = 2
        while p * p <= x:
            if x % p == 0:
                cnt = 0
                while x % p == 0:
                    x //= p
                    cnt += 1
                ans += cnt
            p += 1

        if x > 1:
            ans += 1

        print(ans)

solve()