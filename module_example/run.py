import calculator as calc
import math
import random
import os
import datetime

# 불러온 모듈
print(calc.add(1, 2))
print(calc.subtract(4, 2))
print(calc.multiply(3, 2))
print(calc.divide(9, 3))

# math 모듈
print(math.log10(100))
print(math.log2(4))
print(math.cos(0))

# random 모듈
print(int(random.random() * 10))
print(random.randint(20, 30))

# os 모듈
print(os.getlogin())
print(os.getcwd())

# datetime 모듈
pi_day = datetime.datetime(2020, 3, 10, 17, 27, 5)
print(pi_day)
today = datetime.datetime.now()
print(today)
print(today - pi_day)