year = 2024

if year % 4 == 0 and year % 100 != 0:
    print('윤년')
elif year % 400 == 0:
    print('윤년')
else:
    print("평년")