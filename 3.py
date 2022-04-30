# import math
# from multiprocessing.spawn import import_main_path


# import_main_path

# print(" 'a, b, c' 3개의 값을 입력하시오.")
# a = int(input("a의 값을 입력하시오.:  "))
# b = int(input("b의 값을 입력하시오.:  "))
# c = int(input("c의 값을 입력하시오.:  "))

# d = math.sqrt(b * b) - (4 * a * c)
# x1 = (-b + d) / (2 * a)
# x2 = (-d + d) / (2 * a)
# print(x1, x2)

# from math import sqrt 

# print(" 'a, b, c' 3개의 값을 입력하시오.")
# a = int(input("a의 값을 입력하시오.:  "))
# b = int(input("b의 값을 입력하시오.:  "))
# c = int(input("c의 값을 입력하시오.:  "))

# d = sqrt(b * b) - (4 * a * c)
# x1 = (-b + d) / (2 * a)
# x2 = (-d - d) / (2 * a)

# print(x1, x2)

# 교안 5페이지

# total = 0
# counter = 1
# while counter <= 10:
#     grade = int(input("Enter grade:  "))
#     total = grade + total
#     counter = counter + 1
# average = total / 10

# print(average)

# x = int(input("x의 값을 입력하시오.:  "))
# y = int(input("y의 값을 입력하시오.:  "))
# z = int(input("z의 값을 입력하시오.:  "))

# x = x + 1
# y = y + 1
# z = z + 1

#print("변경된 값", x, y, z)

#16페이지 

# a = 10; b = 8750; c = a * b; print(c)

# pay_rate = 8750
# hours_worked = int(input("일을 한 전체 시간을 입력하시오.:  "))
# monthly_pay = hours_worked * pay_rate
# print(monthly_pay)

# pay_rate = int(input("시급을 입력하시오.:  "))
# hours_worked = int(input("일을 한 전체 시간을 입력하시오.:  "))
# monthly_pay = hours_worked * pay_rate
# print(monthly_pay)

#환율

a = 1000
b = a * 1130
print(b)

won = int(input("환전하고자 하는 금액을 입력하시오.:  "))
usd = int(input("현재 us $의 환율금액을 입력하시오.:  "))
change = won * usd

print(change)