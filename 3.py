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
# import math 

# print(" 'a, b, c' 3개의 값을 입력하시오.")
# a = int(input("a의 값을 입력하시오.:  "))
# b = int(input("b의 값을 입력하시오.:  "))
# c = int(input("c의 값을 입력하시오.:  "))

# d = math.sqrt(b * b) - (4 * a * c)
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

# print("변경된 값", x, y, z)

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

# a = 1000
# b = a * 1130
# print(b)

# won = int(input("환전하고자 하는 금액을 입력하시오.:  "))
# usd = int(input("현재 us $의 환율금액을 입력하시오.:  "))
# change = won * usd

# print(change)

# a = 100
# b = a - 32
# b = b * 5
# b = b / 9

# print(b)

# 정수 합

# x = 0
# y = 0
# x = int(input("정수 x를 입력하시오.:  "))
# y = int(input("정수 y를 입력하시오.:  "))
# sum = x + y
# print(sum)

#부가세 계산

# price = int(input("상품의 가격을 입력하시오.:  "))
# vat = price * 0.1
# print(vat)

#사용자의 10년 후 나이

# age = int(input("현재 나이를 입력하시오.:  "))
# age = age + 10
# print("10년후면", age, "세가 되시는 군요")

# 배송료 계산

# print("####################")
# print("# 배송료 계산 프로그램 #")
# print("####################")
# price = int(input("상품의 가격을 입력하세요.: "))
# if price > 2000:
#    shipping_cost = 0
# else:
#    shipping_cost = 3000
# print(shipping_cost)    

# 성적 입력 합격 유무

# print("##########")
# print(" # 합격 불합격 프로그램 # ")
# print("##########")

# grade = int(input("성적을 입력하시오.: "))
# if grade >= 60 :
#     print("합격")
# else :
#     print("불합격")
   
# 근무시간에 따른 정상 및 초과유무

# print("근무 시간을 입력하시오.")
# work_hour=int(input("근무시간 입력:  "))

# if work_hour > 72 :
#     print("초과근무 하셨습니다.")
# else:
#     print("정상근무하셨습니다.")

# 홀짝 판별

# print("##########")
# print("# 짝수와 홀수 판별 앱 #")
# print("##########")

# x = int(input("x값 정수를 입력하시오.: "))
# if (x % 2) != 0:
#     print("홀수입니다")
# else:
#     print("짝수입니다.")


# 입력 값에 따라 다르게 작업

# print("정수를 입력하시오.")
# x= int(input("정수값 x를 입력하시오.: "))
# y= int(input("정수값 y를 입력하시오.: "))
# if x > y :
#     print(x)
# else:
#     print(y)
    
# 사용자의 이름과 나이 입력 후 답변

# print("#########")
# print("# 이름, 나이, 답변 앱 #")    
# print("##########")

# yu_name = str(input("이름: "))
# yu_age = int(input("나이: "))

# if yu_age <= 25 :
#     print("와우!!! 프로그래밍을 완벽하게 배울 수 있는 나이입니다.!")
# else:
#    print("포기하기에는 아직 늦지 않았습니다.")
# print("＼n")

# 배송료 계산

price = int(input("상품의 가격을 입력하세요.: "))

if price > 100000:
    shipping_cost = 0
else:
    if price > 2000:
         shipping_cost = 3000
    else:
        shipping_cost = 5000
        
print("배송료는", shipping_cost, "입니다.")
 