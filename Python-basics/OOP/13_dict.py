""" 
案例：演示python内置的dict属性
__dict__属性介绍：
    它是python内置的属性，可以把对象转成字典形式
"""
#需求1：把学生对象-->字典形式，属名做键，属性值做值
from Student_Project.student import Student
s1=Student('dd','f',81,'1111','dfls')
print(s1)