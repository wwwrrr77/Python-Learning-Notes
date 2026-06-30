# s=[1,2,3,4,5,6,7,8,9]
# print(s[0])
# del s[3]
# print(s)
#  # 遍历
# for i in s:
#     print(i)
# s=[1,2,3,4,5,6,7,8,9]
# # print(s[0:5:1])
# # print(type (s[0:5:1]))
# s.append(188)
# s.insert(1,80)
# print(s)
# 定义一个空列表
s=[]
for i in range(10):
    num=int(input("请输入一个整数"))
    s.append(num)
s.sort()
print(s)
print("最小值为：",s[0])
print("最大值为：",s[9])
sum=0
for i in s:
    sum+=i
print(sum/10)



