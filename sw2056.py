t = int(input())

for i in range(1, t+1):

    yearMonthDay = input()
    year = int(yearMonthDay[0:4])
    strYear = yearMonthDay[0:4]
    month = int(yearMonthDay[4:6])
    strMonth = yearMonthDay[4:6]
    day = int(yearMonthDay[6:8])
    strDay = yearMonthDay[6:8]

    if((month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day <= 31):
        print("#{} {}/{}/{}".format(i, strYear, strMonth, strDay))
    elif((month == 4 or month == 6 or month == 9 or month == 11) and day <= 30):
        print("#{} {}/{}/{}".format(i, strYear, strMonth, strDay))
    elif(month == 2 and day <= 28):
        print("#{} {}/{}/{}".format(i, strYear, strMonth, strDay))
    else:
        print("#{} -1".format(i))

