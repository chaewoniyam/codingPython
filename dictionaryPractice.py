cabinet = {3 : "유재석", 100 : "김태호"}
print(cabinet[3])
print(cabinet.get(5, "사용 가능"))
print(3 in cabinet)
print(5 in cabinet)


cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20" ] = "조세호"
print(cabinet)

del cabinet["A-3"]
print(cabinet)


print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)