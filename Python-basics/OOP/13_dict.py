""" 
案例：演示python内置的dict属性
__dict__属性介绍：
    它是python内置的属性，可以把对象转成字典形式
"""
#需求1：把学生对象-->字典形式，属名做键，属性值做值
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from Student_Project.student import Student
s1=Student('dd','f',81,'1111','dfls')
s2=Student('dd','f',81,'1111','dfls')
print(s1)
my_dict=s1.__dict__
print(my_dict)
print(type(my_dict))
stu_list=[s1,s2]
#列表推导式
list_dict=[stu.__dict__ for stu in stu_list]
print(list_dict)