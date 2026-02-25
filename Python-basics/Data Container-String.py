####字符串:字符的容器，一个字符串中可以存放任意的字符
#特点：不可变性（无法修改），有序性，可迭代性
#字符串中的每个字符都有其对应的下标(索引)

#可以切片，和列表切片一样
s = 'Hello -World'
# print(s[4])
# print(s[-4])#字符串可以进行正向索引和反向索引
# # s[4]='b'
# # print(s[4])#TypeError: 'str' object does not support item assignment---字符串具有不可变性
# for i in s:
#     print(i)#字符串具有可迭代性

#切片
# print(s[0:6:1])
# print(s[0:6:])
# print(s[0:6])
# print(s[:6])#都是print out hello

# print(s[6:12:1])
# print(s[6:12:])
# print(s[6::])#print out -world

print(s[::6])#步长为正，是从前往后
print(s[::-6])#步长为负，是从后往前