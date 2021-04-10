print("Hello\n" * 3)
age = 26
print("저는 " + str(age) + "살입니다")
year, month, day = 2021, 4, 10
print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))
date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day + 1))

print("저는 {2}, {1}, {0}을 좋아합니다.".format("손흥민", "빌게이츠", "박찬호"))
num1, num2 = 1, 3
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num1, num2, num1 / num2))
print(f"{num1} 안녕 {num2}")

for i in range(2,5):
   print(i)
