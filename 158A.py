n, c = input().split(" ")
n, c = int(n), int(c)

a = []
b = []
a = [int(x) for x in input("Enter elements for a: ").split()]
b = [int(x) for x in input("Enter elements for b: ").split()]

time = 0
if a[0:]<b[0:]:
    print(-1)
else:
    while (a!=b):
        a.sort()
        time+=1
        
