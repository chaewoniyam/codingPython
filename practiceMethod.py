def profile(name, age, *language): # *language 변동 많은 거? 다 받겠다는 의미 근데 반복문 써줘야겠쥬?
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end=" " 줄 바꿈 안 할 거임
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#,", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")