
def std_weight(height, gender):
    if (gender == "남자"):
        weight = height * height * 22
        return weight
        
    elif (gender == "여자"):
        weight = height * height * 21
        return weight

height = 175
gender = "남자"
weight = round(std_weight(height/100, gender),2)
print("키 {0}cm {1}의 표준 체중은 {2} 입니다.".format(height, gender, weight))
