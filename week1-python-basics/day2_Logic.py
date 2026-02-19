####数据和逻辑
####条件判断--if语句：只有满足指定条件，才会执行对应的代码逻辑//python中通过缩进来描述代码的归属的，使用tab或者4个空格来进行缩进
# #if语句的基本结构：
# # if 要判断的条件:
# #     满足条件时执行的代码逻辑
# # else:
# #     不满足条件时执行的代码逻辑
# score = int(input("请输入你的高考成绩："))
# if score >= 680:
#     print("恭喜你，考上了清华大学！")
# else:
#     print("很遗憾，你没有考上清华大学。")

# #案例：账号和密码验证
# account = input("请输入正确的账号:")
# password = input("请输入正确的密码：")
# if password == "666888" and account == "1888888888":
#     print("登入成功")
# elif password != "666888" and account != "1888888888":
#     print("账号和密码错误")
# elif password != "666888":
#     print("密码错误")
# elif account != "1888888888":
#     print("账号错误")

# #案例：判断年份是否为闰年
# years = int(input("请输入一个年份： "))
# if (years % 4 ==0 and years %100 != 0) or (years % 400 ==0):
#     print(f"{years}是闰年")
# else:
#     print(F"{years}不是闰年")

#案例：判断一个数是偶数还是奇数
number = int(input("Please enter a whole number: "))
if number % 2 == 0:
    print(f"{number} is an even number\n")
else:
    print(f"{number} is an odd nuymber\n")

#案例：判断年龄是否成年
age = int(input("Please enter your age: "))
if age >=18:
    print("You are an adult\n")
else:
    print("You are under age\n")

#案例：判断正负数
num = float(input("Please enter any number: "))
if num >0:
    print("It is a positive number\n")
elif num <0:
    print("It is a negative number\n")
else:
    print("It is zero\n")
#案例：判断考试成绩
grade = int(input("Enter your exam score: "))
if grade >= 60:
    print("Your are passed\n")  
else:    
    print("You are failed\n")  

####模式匹配

####循环