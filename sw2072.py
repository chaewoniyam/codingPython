# t = int(input())
 
# for i in range(1, t+1):
#     num = map(int, input().split())
#     sum=0
#     for j in num:
#         if(j % 2 != 0):
#             sum += j
#     print("#{} {}".format(str(i),str(sum)))   



t = int(input())

for i in range (t):
    n = map(int, input().split())
    sum = 0
    for j in n:
        if(j%2!=0):
            sum += j
    print("#{} {}".format(str(i+1), str(sum)))
















    

