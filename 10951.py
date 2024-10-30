
while(1): # 무수히 더하는 반복문에서 
    try:
        a,b = map(int, input().split())
        print(a+b)
    except: # 다른 입력이 입력되면 종료
        break
# 문제에서 테스트 케이스에서 말한 조건이 (0 < A, B < 10) 라서 break문 조건으로 만들었으나,,
# 하지만 숫자 말고는 다른 입력 받으면 안 되기에 try except 문을 쓰나봐요
# 그럼 저 조건 왜 달아둠? 테스트 케이스 조건 자체가 틀렸는데..!