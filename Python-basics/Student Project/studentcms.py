""" 
该文件用于 完成学生系统的 具体业务的操作，即：增删改查，保存学生信息。。。
"""
#导包
from student import Student
class StudentCMS:
    def __init__(self):
        self.stu_list=[]
    def show_menu(self):
        menu=""" 
************************************
本学员管理系统V2.0可完成如下操作:
    1.添加学员
    2.修改学员
    3.删除学员
    4.查询某个学员
    5.显示所有学员
    6.保存信息
    7.退出系统
*************************************

        """
        print(menu)
    def add(self):
        pass





    
#测试
if __name__ == "__main__":
    s1=StudentCMS()
    print(s1.show_menu())