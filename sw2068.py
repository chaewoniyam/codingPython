t = int(input())

for i in range(1, t+1):
    n = list(map(int, input().split()))
    num = max(n)
    print("#{} {}".format(i, num))