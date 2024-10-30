N = int(input())

if 4 <= N & N <= 1000:
    for long in range(N//4):
        print("long ", end="")
    print("int")

else:
    print("4~1000까지의 수만 입력 가능합니다.")