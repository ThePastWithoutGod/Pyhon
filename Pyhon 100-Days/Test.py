# T1:将华氏温度转摄氏温度。
#  F = 1.8C + 32
'''
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

'''
# T3：输入年份判断是不是闰年。
year = int(input("请输入一个年份:"))
leapyear = (year % 4 == 0)
print("{0}是闰年".format(leapyear))