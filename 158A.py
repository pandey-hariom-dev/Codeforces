n = int(input())
c = int(input())

a = []
b = []
for z in range(0, n):
    row_a = [int(x) for x in input(f"Enter space-separated elements for a{z}: ").split()]
    row_b = [int(x) for x in input(f"Enter space-separated elements for b{z}: ").split()]
    # Append the completed list (row) to your main matrices
    a.append(row_a)
    b.append(row_b)


if a[0:]<b[0:]:
    print(-1)
