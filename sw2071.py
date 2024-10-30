t = int(input())

for i in range(t):
    n = map(int, input().split())
    avg=0
    for j in n:
        avg += j
    avg = avg/10
    print("#{} {}".format (i+1, round(avg)))

