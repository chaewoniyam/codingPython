# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추천 프로그램을 작성하시오.

# 조건1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle과 sample을 활용


from random import *
lst = [1,2,3,4,5]
shuffle(lst)
print(lst)
print(sample(lst,1))


users = range(1,21)
#print(type(users))  타입이 range로 뜸 print만 하면 range(1,21)로 뜸 그 안의 값을 보고 싶으니 리스트로 형 변환을 해줘야겠쥬
users = list(users)
#print(type(users))  타입이 range로 뜸

print(users)
shuffle(users)
print(users)

# 중복되면 안 되니까 4개 먼저 뽑기
winners = sample(users, 4) 


print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")
