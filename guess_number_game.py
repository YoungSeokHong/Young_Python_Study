import random

min, max = 1, 20
collect = False
random_num = random.randint(1, 20)

for i in range(4):
   x = int(input(f"기회가 {4 - i}번 남았습니다. {min}-{max} 사이의 숫자를 맞혀 보세요: "))
   if x == random_num:
      print(f"축하합니다. {i + 1}번만에 숫자를 맞히셨습니다.")
      collect = True
      break
   elif x > random_num:
      print("Down")
   else:
      print("Up")

if collect != True:
   print(f"아쉽습니다. 정답은 {random_num}였습니다.")