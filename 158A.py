t = int(input())

for _ in range(t):
    n, c = map(int, input().split())

    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    cost_without_reorder = 0
    possible_without_reorder = True
    for i in range(n):
        if a[i] < b[i]:
            possible_without_reorder = False
            break
        cost_without_reorder += (a[i] - b[i])
        
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    
    possible_with_reorder = True
    for i in range(n):
        if a_sorted[i] < b_sorted[i]:
            possible_with_reorder = False
            break
        cost_with_reorder += (a_sorted[i] - b_sorted[i])
        
    if not possible_with_reorder:
        print(-1)
    elif not possible_without_reorder:
        print(cost_with_reorder)
    else:
        print(min(cost_without_reorder, cost_with_reorder))