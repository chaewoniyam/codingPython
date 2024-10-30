N, M = map(int, input().split())
Nlist = [0 for t in range(N)] # 입력받은 숫자 크기만큼 0으로 리스트 채우기

for u in range(M):
    i, j, k = map(int, input().split())
    for num in range(i-1,j):
        Nlist[num] = k

print(*Nlist)
