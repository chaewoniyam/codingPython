from random import *

cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if(5<=time & time<=15):
        print("[O]"+ str(i)+"번째 손님 (소요시간 : "+ str(time) +"분)")
        cnt += 1
    else:
        print("[ ]"+ str(i)+"번째 손님 (소요시간 : "+ str(time) +"분)")
print("총 탑승 승객 : " +str(cnt)+ "분")