####函数--是组织好的，可重复是要的，用来实现特定功能的代码片段
####函数基础
#函数是组织好的，可重复使用的，用来实现特定功能的代码片段
#函数的定义与调用
#定义函数
"""def 函数名（参数列表）：
    函数体
    .....
    return 返回值
"""
#调用函数
"""
函数名(参数)
"""
# def out_line():
#     print("______________________")
#     print("______________________")
# out_line()

#案例：计算圆形的面积
# def area_circle(r):
#     area = 3.14*r**2
#     return area
# print(area_circle(2))

# #案例：计算长方形的面积
# def area_rectangle(a,b):
#     area=a*b
#     return area
# print(area_rectangle(7,8))

# 案例：计算圆形的面积--->如果返回值有多个--->多个返回值会封装到元组当中
def area_circle(r):
    area = 3.14*r**2
    length = round(3.14*2*r,1)#round()保留小数点
    return area,length
area,len=area_circle(5)
print(area)
print(len)
####函数进阶