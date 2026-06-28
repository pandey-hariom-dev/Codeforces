n = int(input())
c = int(input())

a = []
b = []
a = [int(x) for x in input("Enter elements for a: ").split()]
b = [int(x) for x in input("Enter elements for b: ").split()]

if a[0:]<b[0:]:
    print(-1)
