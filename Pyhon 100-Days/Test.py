import random
import math

'''
# T1:将华氏温度转摄氏温度。
#  F = 1.8C + 32

f = float(input("请输入温度："))
c =  (f - 32)/1.8
print(c)
print("摄氏温度为：{0}".format(c))

# T2：输入圆的半径计算计算周长和面积。
s1 = float(input("请输入圆的半径为："))
C = 3.14*2*s1
S = 3.14*s1**2
print(C)
print("圆的周长为：{0}".format(C))
print(S)
print("圆的面积为：{0}".format(S))


# T3：输入年份判断是不是闰年。
year = int(input("请输入一个年份:"))
leapyear = (year % 4 == 0)
print("{0}是闰年".format(leapyear))


# T4：英制单位英寸和公制单位厘米互换
s1 = float(input("请输入长度："))
unit = input("请输入单位:")
if unit == "inch" or unit == "英寸":
    print("转换成厘米为{0}".format((s1*2.54)))
elif unit == "cm" or unit == "厘米":
    print("转换成英寸为{0}".format((s1*2.54)))
else:
    print("请输入有效值")

# T5：掷骰子决定做什么
b = random.randint(1,6)
print(b)
if b == 1:
    result = "打印1"
elif b == 2:
    result = "打印2"
elif b == 3:
    result = "打印3"
elif b == 4:
    result = "打印4"
elif b == 5:
    result = "打印5"
else:
    result = "打印6"
print(result)
'''

# T6：百分制成绩转等级制
score = float(input("分数:"))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "E"
print("成绩的等级为{0}：".format(grade))
# T7：输入三条边长如果能构成三角形就计算周长和面积
c1 = float(input("第一条边长为："))
c2 = float(input("第二条边长为："))
c3 = float(input("第三条边长为："))
if c1 + c2 > c3 and c1 + c3 > c2 and c2 + c3 > c1:
    C = c1 + c2 + c3
    p = C/2
    area =math.sqrt(p * (p-c1) * (p-c2) * (p-c2))       # 海伦公式求三角形面积
    print("圆的周长为：{0}".format(C))
    print("圆的面积为：{0}".format(area))

# T8：个人所得税计算器。
salary = float(input("本月薪水为："))
insurance = float(input("五险一金为："))
diff = salary - insurance - 3500
if diff <= 0:
    rate = 0
    deduction  = 0
elif diff < 1500:
    rate = 0.03
    deduction = 0
elif diff < 4500:
    rate = 0.1
    deduction = 105
elif diff < 9000:
    rate = 0.2
    deduction = 555
elif diff < 35000:
    rate = 0.25
    deduction = 1005
elif diff < 55000:
    rate = 0.3
    deduction = 2755
elif diff < 80000:
    rate = 0.35
    deduction = 5505
else:
    rate = 0.45
    deduction = 13505
tax = abs(diff * rate - deduction)
print("个人所得税: {0}元".format(tax))
print("实际到手收入: {0}元" .format ((diff + 3500 - tax)))