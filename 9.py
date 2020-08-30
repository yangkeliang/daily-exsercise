# i=1
# while i<=10:
#     print(i,end="   ")
#     i=i+1

# s=0
# for i in range(1,101):
#     s=s+i
# print(s)

# for i in range(1,101,2):
#     print(i)

# for i in range(2,101,2):
#     print(i)

# # s=0
# # for i in range(1,100):
# #     if i%2==0:
# #         i=-i
# #     s=s+i
# # print(s)

# n=0
# while(n<3):
#     a=int(input("请输入密码:"))
#     n=n+1
#     if a==1234:
#         print('yes')
#         break
#     elif a!=1234 and n!=2:
#         print("input again")
#     else:
#         print("没机会了")

a=int(input("层数："))
for i in range(1,a+1):
    print(" "*(a-i)+"*"*(2*i-1)+" "*(a-i))

