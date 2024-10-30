n = int(input())

if 1<= n & n <= 9:
    for num in range(1,10):
        rhq = n * num
        print("{0} * {1} = {2}".format(n, num, rhq))

else:
    print("1~9까지의 수만 입력해주세요")