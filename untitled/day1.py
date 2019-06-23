#!/usr/bin/python
# -*-  coding:utf-8 -*-
# import copy
# b=[5,6,6,7,2,]
# c=[100,200,300,b]
# ff=copy.deepcopy(c)
# b.append('你好')
# c.append('我很帅')
# print(c)
# print(ff)
#a=input()
#a=int(a)


#成绩评价
# if a>= 90 :
#     print('优')
# elif 90 > a >= 80:
#     print('良')
# elif 80 > a >= 70:
#     print('及格')
# else:
#     print('不及格')

# a=input('>>>')
# a=int(a)
# if a % 2 == 0:
#     if a % 3 == 0:
#         print('hello world')
#     else:
#         print('hello')
# elif a % 3 ==0:
#      print('word')
# else:
#    print('123')

# a=101
# b=0
# for i in range(a):
#    b=i+b
# print(b)

#100以内奇数-偶数
# b=0
# c=0
# for i in range(1,100):
#     if i%2==0:
#         b=i+b
#     else:
#         c=i+c
# print(c-b)

#三次猜数字
# import  random
# a = random.randrange(1,10)
# print(a)
# for  i in range(1,4):
#  b = input()
#  b=int(b)
#  if b == a:
#     print('恭喜，答对了')
#     break
#  elif b > a:
#      print('大了大了 还有{}次机会'.format(3-i))
#  else:
#     print('小了小了 还有{}次机会'.format(3-i))
# else:
#     print('菜')

#九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         a=i*j
#         print('{}*{}={}'.format(i, j, a),end='\t')
#     print()


#100以内质数之和
# c=input('请输入一个范围')
# c=int(c)
# b=0
# for i in range(2,c):
#     for j in range(2,i+1):
#         a=i%j
#         if a == 0:
#             break
#     if i == j:
#             b=b+i
# print(b)

#100-999以内的水仙花数
# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10
#     if i==a**3 + b**3 + c**3:
#        print(i)

#任意数以内的因数之和等于本身
# c=input('请输入一个数')
# c=int(c)
# for i in range(1,c+1):
#     b=0
#     for j in range(1,i):
#         a=i%j
#         if a == 0:
#             b=b+j
#     if b == i:
#          print(i)


#阶乘之和
# c=input('请输入一个数')
# c=int(c)
# a=1
# sum=0
# for i in range(1,c):
#     a=i*a
#     sum=a+sum
# print(sum)

#回环字符串
#!/usr/bin/python
# -*- coding:utf-8 -*-
# a=input('请输入一个字符串')
# for i in range(len(a)//2):
#     if a[i] != a[-(i+1)]:
#         print('不是回环字符串')
#         break
# else:
#     print('是回环字符串')


# 1到100之和
# i=0
# b=0
# while i < 101:
#     b+=i
#     i+=1
# print(b)



#从键盘输入若干个学生的成绩，统计出平均成绩并输出低于平均分的学生，输入负值结束输入
# while True:
#   a=input('请输入一组成绩')
#   a=a.split(',')
#   for i,j in enumerate(a):
#     a[i]=int(j)
#   b=sum(a)//len(a)
#   if a[0] < 0:
#       break
#   print('平均数为{}'.format(b))
#   for k in a:
#     if k < b:
#         print('低于平均分的成绩为{}'.format(k))


# while True:
#     a=input()
#     a=a.split(',')
#     a=[int(i) for i in a]
#     b=sum(a)//len(a)
#     if a[0] < 0:
#         break
#     print('平均数为{}'.format(b))
#     c=[k for k in a if k<b]
#     print(c)

#去重并排序
# a=input('请输入一组数')
# a=a.split(',')
# a=[int(y) for y in a]
# for i in a :
#     c=a.count(i)
#     if c>1:
#         for j in range(c-1):
#             a.remove(i)
# a.sort()
# print(a)
#或者
# b=[]
# for i in a:
#     if i not in b :
#         b.append(i)
# b.sort()
# print(b)


#九九乘法表写入a.out
# f=open('a.txt','w',encoding='utf-8')
# for i in range(1,10):
#     for j in range(1,i+1):
#         f.write('{}*{}={}\t'.format(i,j,i*j))
#     f.write('\n')
# f.close()

#
# f=open('a.txt','r',encoding='utf-8')
# b=f.readlines()
# for i in b:
#     if i[:3] == 'abc':
#         print(i)
#
# for i in range(1,21):
#    if i<15:
#     f.readline()
#    else:
#        print(f.readline())
# f.close()


#判断三角形
# a=input('请输入三边')
# a=a.split(',')
# a=[int(i) for i in a]
# a.sort()
# if a[0] +a[1]>a[2]:
#    if a[0] - a[1]<a[2]:
#        if a[0]**2+a[1]**2==a[2]**2:
#            print('这个三角形是直角三角形')
#        elif a[0]**2+a[1]**2>a[2]**2:
#            print('这个三角形是锐角三角形')
#        else:
#            print('这个三角形是顿角三角形')
# else:
#     print('这个不是三角形')


#选择排序法
# a=input('请输入一组数')
# b=a.split(',')
# b=[int(i) for i in b]
# c=len(b)
# for i in range(0,c):
#     for j in range(i+1,c):
#       if b[i]>b[j]:
#             t=b[i]
#             b[i]=b[j]
#             b[j]=t
# print(b)


#冒泡排序法
# a=input('请输入一组数')
# a=a.split(',')
# a=[int(c) for c in a]
# d=len(a)
# for j in range(1,d):
#   for i in range(0,d-1):
#      if a[i] > a[i+1]:
#         t=a[i]
#         a[i]=a[i+1]
#         a[i+1]=t
# print(a)


#打印列表中所有第一大和第二大的数
# a=input('请输入一组数')
# b=a.split(',')
# b=[int(i) for i in b]
# b.sort()
# print(b)
# c=[]
# d=b.count(b[-1])
# for j in range(1,d+1):
#     c.append(b[-1])
#     b.remove(b[-1])
# f=b.count(b[-1])
# for j in range(1,f+1):
#     c.append(b[-1])
# print(c)


#将列表中的元素向左挪一位
# a=input('请输入一组数')
# a=a.split(',')
# t=a[0]
# for i in range(len(a)-1):
#     a[i]=a[i+1]
# a[-1]=t
# print(a)



#自定义函数1到100的和
# def a():
#     b=0
#     for i in range(101):
#         b+=i
#     print(b)
# a()

#判断以什么开头以什么结尾
# with open('a.txt','r',encoding='utf-8') as f:
#     c=f.readlines()
#     print(c)
#     for j in range(len(c)):
#         b=c[j].startswith('df')
#         d=c[j].endswith('r\n')
#         if b==True and d==True:
#              print(c[j])


#用100元买100只鸡，公鸡2元一只，母鸡1元一只，小鸡0.5元一只，问买公鸡、母鸡、小鸡各几只
# for i in range(51):
#     for j in range(101):
#         if 2*i+j+(100-i-j)*0.5 == 100:
#             print('公鸡有{}只,母鸡有{}只,小鸡有{}只'.format(i,j,100-i-j))


#不用int将字符串变成整数
# a=input('请输入一个数')
# c=len(a)
# b=0
# for j in range(c):
#     for i in range(10):
#         if str(i) == a[j]:
#             b+=i*10**(c-j-1)
# print(b)
# print(type(b))


#任意4个数字,组成不同的三位数
# a=input('请输入四个数字')
# a=a.split(',')
# b=[int(i) for i in a]
# for j in range(len(b)):
#     for x in range(len(b)):
#         if b[x] != b[j]:
#             for y in range(len(b)):
#                 if b[y] != b[j] and b[y] != b[x]:
#                     c=b[j]*100+b[x]*10+b[y]
#                     print(c)

#将列表中最大的放在最后一位，最小的放在第一位
# a=input('请输入一组数')
# a=a.split(',')
# b=[int(i) for i in a]
# b.sort()
# a=[int(j) for j in a]
# a.remove(b[0])
# a.remove(b[-1])
# a.insert(0,b[0])
# a.append(b[-1])
# print(a)


# def d(x,y):
#      a=0
#      for i in range(x,y):
#          if i!=1:
#              for j in range(2,i):
#                  if i%j ==0 :
#                      break
#              else:
#                   a+=i
#      print(a)
#      return 10
# c=d(1,10)+2
# print(c)



# def a(j):
#     b=0
#     for i in range(1,j+1):
#           b+=i
#     return b
# for i in range(10,41,10):
#     c=a(i)+2
#     print(c)


# a=lambda x,y: x+y
# b=lambda x,y: x-y
# c=lambda x,y: x*y
# d=lambda x,y: x/y
# while True:
#   s=input('>>>')
#   if '-' in s:
#     s=s.split('-')
#     print(b(int(s[0]),int(s[1])))
#   elif '+' in s:
#     s=s.split('+')
#     print(a(int(s[0]),int(s[1])))
#   elif '*' in s:
#     s=s.split('*')
#     print(c(int(s[0]),int(s[1])))
#   elif '/' in s:
#     s=s.split('/')
#     print(d(int(s[0]),int(s[1])))
#   elif 'exit' in s:
#        break

#第一个参数是字符串，第二个和第三个都是数字
#删除这个字符串从第二个数字为下标位置，删除第三个数
# def a(x,y,z):
#     x=list(x)
#     d=y+z
#     if d>len(x):
#         d=len(x)
#     for i in range(y,d):
#           x.pop(y)
#     x=''.join(x)
#     print(x)
# a('dfdfdff',3,2)



#一个函数，传两个参数a,b，a是数组，b是一个数字，找出a数组中两数只和等于b，打印出来这两个数
# def a(x,y):
#     x=x.split(',')
#     x=[int(b) for  b in x]
#     for i in range(len(x)-1) :
#         for j in range(i+1,len(x)):
#                 c=x[i]+x[j]
#                 if c == y:
#                     print(x[i],x[j])
# a('12,13,14,15,14',28)




#统计.Cpp文件有多少行，统计的时候将文件中的空行、单行注释的行去除
# with open('a.txt','r',encoding='utf-8') as f :
#     a=f.readlines()
#     c=len(a)
#     print(c)
#     for i in range(len(a)-1):
#         b = a[i].startswith('#')
#         if a[i] == '\n':
#             c=c-1
#         elif b ==True:
#             c=c-1
#     print(c)



#一个有顺序的列表，随机加入一个数，加入的数在正确的位置
# import  random
# b=random.randrange(10)
# b=int(b)
# a=[2,3,5,9]
# a.append(b)
# for j in range(len(a)):
#     for i in range(len(a)-1):
#         if a[i] > a[i+1]:
#             t=a[i]
#             a[i]=a[i+1]
#             a[i+1]=t
# print(a)



#10进制转化成16进制
# a=100
# d=[str(i) for i in range(10)]+['a','b','c','d','e','f']
# c=''
# while True:
#     b=a%16
#     c=c+d[b]
#     a=a//16
#     if a == 0:
#         break
# print(c[::-1])

#1到100加入到文件中
# import xlwt
# f=xlwt.Workbook(encoding='utf-8')
# sheet=f.add_sheet('python_test')
# for i in range(0,100):
#     sheet.write(i,0,i+1)
# f.save('aaa.xls')



# import xlrd
# f=xlrd.open_workbook('aaa.xls')
# b=f.nsheets
#print(b)
# sheet=f.sheets([0])
# sheet=f.sheet_by_name('python_test')
# b=f.sheet_names()
# print(b)
#对行的操作
# x=sheet.nrows
# print(x)
# for i in range(x):
#     c=sheet.row_values(i)
#     print(c)
#对列的操作
# c=sheet.col_values(0)
# print(c)
# x=sheet.ncols
# print(x)
# for i in range(x):
#     c=sheet.col_values(i)
#     print(c)
# b=sheet.cell(1,0).value
# print(b)
# for i in range(14,20):
#     c=sheet.row_values(i)
#     print(c)

#将a.txt文件中的内容打印到excle表中
#!/usr/sbin/python
# -*- coding:utf-8 -*-
# import  xlwt
# with open('a.txt','r',encoding='utf-8') as  f:
#     a=f.readlines()
#     c=[]
#     for i in range(len(a)):
#         b=a[i]
#         b=b.split(',')
#         c.append(b)
# m=xlwt.Workbook(encoding='utf-8')
# sheet=m.add_sheet('test')
# for i in range(len(c)):
#     for j in range(len(b)):
#         sheet.write(i,j,'{}'.format(c[i][j]))
# m.save('aa.xls')



# import time
# b=time.time()
# print(b)
# a=time.localtime()
# print(a)
# c=time.strftime('%Y-%m-%d %H:%M:%S %w')
# print(c)
# a=time.strptime('2012-12-12','%Y-%m-%d')
# print(a)


#输入一个日期判断其是否为闰年，今天是第多少天，今天是星期几
# import time
# a=input('输入一个日期')
# b=time.strptime(a,'%Y-%m-%d')
# c=a.split('-')
# e=int(c[0])
# if c[0][2]=='0' and c[0][3]=='0':
#     d=e%400
#     if d==0:
#         print('{}年是闰年'.format(c[0]))
#     else:
#         print('{}年不是闰年'.format(c[0]))
# elif c[0][2]!='0' or c[0][3]!='0':
#       d=e%4
#       if d==0:
#           print('{}年是闰年'.format(c[0]))
#       else:
#           print('{}年不是闰年'.format(c[0]))
# print('今天是一年中的第{}天'.format(b[7]))
# print('今天是星期{}'.format(b[6]+1))




#将b.txt文件内容追加到aa.xls中
# from xlutils.copy import copy
# import xlrd
# with open('a.txt','r',encoding='utf-8') as  f:
#     a=f.readlines()
#     c=[]
#     for i in range(len(a)):
#         b=a[i]
#         b=b.split(',')
#         c.append(b)
# f=xlrd.open_workbook('aa.xls')
# sheett=f.sheets()[0]
# e=sheett.nrows
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# for i in range(len(c)):
#     for j in range(len(b)):
#         sheet.write(i+e,j,'{}'.format(c[i][j]))
# new_f.save('a.xls')


#输入一个日期，输出前一天日期
# import time
# a=input('输入一个日期')
# b=time.strptime(a,'%Y-%m-%d')
# c=[]
# for i in range(len(b)):
#     c.append(b[i])
# c=tuple(c)
# d=time.mktime(c)
# e=d-86400.0
# aa=time.localtime(e)
# bb=time.strftime('%Y-%m-%d',aa)
# print(bb)


#将列表内容添加到文档中
# import xlrd
# f=xlrd.open_workbook('b.xls')
# sheet=f.sheets()[0]
# a=sheet.nrows
# f=open('b.txt','w',encoding='utf-8')
# for i in range(a):
#     b=sheet.row_values(i)
#     c=','.join(b)
#     print(b)
#     f.write(c)
#     f.write('\n')
# f.close()


# import time
# sentence = "xiao,mei, I love you forever!"
# for char in sentence.split():
#    allChar = []
#    for y in range(12, -12, -1):
#        lst = []
#        lst_con = ''
#        for x in range(-30, 30):
#             formula = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
#             if formula <= 0:
#                 lst_con += char[(x) % len(char)]
#             else:
#                 lst_con += ' '
#        lst.append(lst_con)
#        allChar += lst
#    print('\n'.join(allChar))
#    time.sleep(1)



#将aa.xls内容打印到数据库中
# import pymysql
# import xlrd
# f=xlrd.open_workbook('aa.xls')
# sheet=f.sheets()[0]
# e=sheet.nrows
# coon=pymysql.connect(host='192.168.0.200',port=3306,user='root',passwd='123456')
# m=coon.cursor()
# #m.execute('create database python_xiao;')
# m.execute('use python_xiao')
# #m.execute('create table a(name char(20),age int,sex char(20))')
# for i in range(e):
#     bb=sheet.row_values(i)
#     if i==0:
#        m.execute('create table b({} char(20),{} char(20),{} char(20),{} char(20));'.format(bb[0],bb[1],bb[2],bb[3]))
#     else:
#         m.execute('insert into b values ("{}","{}","{}","{}");'.format(bb[0],bb[1],bb[2],bb[3]))
# # m.execute('delete from b')
# m.execute('select * from b')
# b=m.fetchall()
# print(b)
# coon.close()



#将a.txt文档内容加入数据库
# import pymysql
# with open('a.txt','r',encoding='utf-8') as f:
#     a=f.readlines()
# noon=pymysql.connect(host='192.168.0.200',port=3306,user='root',passwd='123456')
# m=noon.cursor()
# m.execute('use python_xiao')
# for i in range(len(a)):
#     c=a[i]
#     c=c.split(',')
#     if i==0:
#         m.execute('create table a({} char(255),{} char(255),{} char(255),{} char(255));'.format(c[0],c[1],c[2],c[3]))
#     else:
#         m.execute('insert into a values("{}","{}","{}","{}");'.format(c[0],c[1],c[2],c[3]))
# m.execute('select * from a')
# d=m.fetchall()
# print(d)
# noon.close()



#将数据库的内容打印到a.txt文件中
# import pymysql
# coon=pymysql.connect(host='192.168.0.200',port=3306,user='root',passwd='123456')
# m=coon.cursor()
# m.execute('use python_xiao;')
# m.execute('desc a;')
# d=m.fetchall()
# e=[]
# for j in range(len(d)):
#     e.append(d[j][0])
# e=','.join(e)
# m.execute('select * from a;')
# b=m.fetchall()
# f=open('a.txt','w',encoding='utf-8')
# for i in range(len(b)):
#     n = list(b[i])
#     n = ','.join(n)
#     if i ==0:
#         f.write(e)
#         f.write('\n')
#         f.write(n)
#     else:
#         f.write(n)
# f.close()
# coon.close()



#将数据库文件传到excel表中
# import pymysql
# from xlutils.copy import copy
# import xlrd
# coon=pymysql.connect(host='192.168.0.200',port=3306,user='root',passwd='123456')
# m=coon.cursor()
# m.execute('use python_xiao;')
# m.execute('desc a;')
# b=m.fetchall()
# c=[]
# for x in range(len(b)):
#     c.append(b[x][0])
# m.execute('select * from a')
# a=m.fetchall()
# f=xlrd.open_workbook('aa.xls')
# new_f=copy(f)
# sheet=new_f.get_sheet(0)
# for i in range(len(a)+1):
#     for j in range(len(a[0])):
#         if i == 0 :
#             sheet.write(i,j,'{}'.format(c[j]))
#         else:
#             sheet.write(i,j,'{}'.format(a[i-1][j]))
# new_f.save('a.xls')
# coon.close()



# import os
# print(os.getcwd())
# os.chdir(r'C:\Users\xiaozy\.idlerc')
# print(os.getcwd())

# b=os.popen('ping 192.168.0.1')
# print(b.read())

# print(os.listdir(r'C:\Users\xiaozy'))
# b=os.path.isdir(r'C:\Users\xiaozy\PycharmProjects\untitled')
# print(b)

#判断本目录下以.py结尾的文件的打印出来
# a=os.listdir()
# for i in a:
#     b = os.path.isfile(i)
#     d=os.path.splitext(i)
#     if b == True:
#         if d[1]=='.py':
#             print(i)


# import paramiko
# ssh123=paramiko.SSHClient()
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# ssh123.connect(hostname='192.168.0.200',port=22,username='root',password='123456')
# while True:
#     a=input('输入查询命令')
#     if a=='exit':
#         break
#     else:
#         a,b,c=ssh123.exec_command(a)
#         print(b.read().decode())
# ssh123.close()


# import paramiko
# qq=paramiko.Transport(('192.168.0.200',22))
# qq.connect(username='root',password='123456')
# sftp=paramiko.SFTPClient.from_transport(qq)
# sftp.get('/home/a.sh','a.sh')
# qq.close()



#发送邮件
# import smtplib
# import email.mime.multipart as mul
# import email.mime.text as text
# message=mul.MIMEMultipart()
# message['subject']='python_test'
# message['From']='17630171326@163.com'
# a=['17629712980@163.com','1287347397@qq.com','1754261121@qq.com']
# message['To']='.'.join(a)
# txt="""河南很美，小美更美,我爱小美"""
# tet=text.MIMEText(txt)
# message.attach(tet)
# # att1 = text.MIMEText(open('a.txt', 'rb').read(), 'base64', 'utf-8')
# # att1["Content-Type"] = 'application/octet-stream'
# # # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# # att1["Content-Disposition"] = 'attachment; filename="a.txt"'
# # message.attach(att1)
# smtp123=smtplib.SMTP_SSL('smtp.163.com',465)
# smtp123.login('17630171326@163.com','xiao123456')
# smtp123.sendmail('17630171326@163.com',a,message.as_string())


#tcp server 服务端
# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('192.168.0.42',3000))
# s.listen(3)
# while True:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind(('192.168.0.42', 3000))
#     s.listen(3)
#     msg = input('>>>')
#     if msg == 'exit':
#         break
#     else:
#         client,addr=s.accept()
#         reg = client.recv(1024)
#         print(reg.decode('utf-8'))
#         client.send(msg.encode('utf-8'))


# #tcp客户端
# import  socket
# #创建套接字
# while True:
#     sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #连接服务器
#
#     sock.connect(("192.168.0.88",3000))
# #将qq当做请求发送给服务器
#
#     qq =input(">>")
#     # if qq==exit:
#     #     break
#     sock.send(qq.encode("utf-8"))
# #接收响应
#     ww = sock .recv(1024)
#     print(ww.decode("utf-8"))


#基于udp的服务器
# import socket
# sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# sock.bind(('192.168.0.42',3000))
# while True:
#     # msg = input('>>>')
#     # if msg=='exit':
#     #     break
#     # else:
#         client,addr=sock.recvfrom(1024)
#         print(client.decode('utf-8'))
#         msg = input('>>>')
#         sock.sendto(msg.encode('utf-8'),addr)


# udp 的客户端
# import  socket
# s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# while True:
#     host=("192.168.0.88",3000)
#     msg=input(">>>")
#     s.sendto(msg.encode("utf-8"),host)
#     reg=s.recv(1024)
#     print(reg.decode("utf-8"))




# print(hex(22))
# print(int(0b110))
# print(oct(22))
# print(bin(10))
# a=[chr(i) for i in range(97,103)]
# print(min(a))
# a,b=divmod(100,16)


# class Ass():
#     def a(self,x):
#         a=0
#         for i in range(x+1):
#             a+=i
#         print(a)
#     def qwe(self):
#        self.a(10)
# class b():
#      def __init__(self,name,age):
#          self.name=name
#          self.msg=age
#      def a(self):
#          print('{}''{}'.format(self.name,self.msg))
# b('小美--','小哥哥爱你')


#爬标题
# import requests
# import re
# title=[]
# class Freebuf():
#     def send_request(self,page):
#         url='https://www.freebuf.com/page/{}'.format(page)
#         #发送请求
#         head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
#         res=requests.post(url,headers=head)
#         #读取结果 1.text 以文本的方式接收，结果是字符串   2.content 以字节的方式接收，结果是字节的类型
#         # print(res.text)
#         hh=res.content.decode('utf-8')
#         return hh
#     def guolv(self,x):
#         patt=re.compile(' <div class="news-info">(.*?)<dd>',re.S)
#         items=patt.findall(x)
#         for i in items:
#             aa=re.findall('title="(.*?)"',i)
#             title.append(aa[0])
#         return title
#     def save(self,y):
#         f=open('a.txt','w',encoding='utf-8')
#         for i in y:
#             f.write(i+'\n')
# fr=Freebuf()
# for j in range(1,5):
#     hh=fr.send_request(j)
#     b=fr.guolv(hh)
#     yy=fr.save(b)
# print(title)


#爬取图片
# import requests
# import re
# lianjie=[]
# class qiushi():
#     def send_request(self,page):
#         url='http://www.qiushibaike.com/imgrank/page/{}'.format(page)
#         #head = {
#          #   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
#         res=requests.post(url)
#         hh=res.content.decode('utf-8')
#         print(hh)
#         return hh
#     def guolv(self,x):
#         ppat=re.compile('<img src="//pic.qiushibaike.com/system/pictures/(.*?)jpg"')
#         items=ppat.findall(x)
#         for i in items:
#             i='https://pic.qiushibaike.com/system/pictures/'+i+'jpg'
#             lianjie.append(i)
#         print(lianjie)
#         return lianjie
#     def save(self,y):
#         for i in range(1,len(lianjie)+1):
#             msg=requests.get(y[i-1])
#             r=msg.content
#             f=open('{}.jpg'.format(i),'wb')
#             f.write(r)
# qi=qiushi()
# for j in range(1,2):
#     hh=qi.send_request(j)
#     c=qi.guolv(hh)
#     q=qi.save(c)


#爬取豆瓣网电影图片及标题
# import requests
# import re
# lianjie=[]
# title=[]
# class douban():
#     def send_request(self):
#         url='https://movie.douban.com/top250?qq-pf-to=pcqq.group'
#         head = {
#                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'}
#         res=requests.post(url,headers=head)
#         hh=res.content.decode('utf-8')
#         return hh
#     def guolv(self,x):
#         ppat=re.compile('<img width="100" alt="(.*)" src="https://img([0-9]+).doubanio.com/view/photo/s_ratio_poster/public/(.*?)jpg" class="">')
#         items=ppat.findall(x)
#         for i in range(len(items)):
#             title.append(items[i][0])
#             a='https://img'+items[i][1]+'.doubanio.com/view/photo/s_ratio_poster/public/'+items[i][2]+'jpg'
#             lianjie.append(a)
#         return lianjie
#     def save(self,y,bb):
#         for i in range(len(y)):
#             msg=requests.get(y[i])
#             r=msg.content
#             f=open('{}.jpg'.format(bb[i]),'wb')
#             f.write(r)
# dou=douban()
# hh=dou.send_request()
# aa=dou.guolv(hh)
# bb=title
# c=dou.save(aa,bb)



#抓取智联招聘
# import requests
# import json
# import pymysql
# coon = pymysql.connect(host='192.168.0.200', port=3306, user='root', passwd='123456')
# m = coon.cursor()
# m.execute('use test')
# m.execute('create table zhilian(`职位` char(255),`工作经验` char(255),`薪资` char(255),`工作地点` char(255),`公司` char(255),`更新日期` datetime)')
# class boss():
#     def request(self):
#         url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=软件测试工程师&kt=3&=0&_v=0.57473216&x-zp-page-request-id=34b42f4388654059b4d924c3edd85609-1557229284975-139120'
#         res=requests.get(url)
#         hh=res.content.decode('utf-8')
#         return hh
#     def guolv(self,x):
#         qq=json.loads(x)
#         aa=len(qq['data']['results'])
#         for i in range(aa):
#             c=[]
#             c.append(qq['data']['results'][i]['jobName'])
#             c.append(qq['data']['results'][i]['workingExp']['name'])
#             c.append(qq['data']['results'][i]['salary'])
#             c.append(qq['data']['results'][i]['city']['display'])
#             c.append(qq['data']['results'][i]['company']['name'])
#             c.append(qq['data']['results'][i]['endDate'])
#             m.execute('insert into zhilian values("{}","{}","{}","{}","{}","{}")'.format(c[0],c[1],c[2],c[3],c[4],c[5]))
#             print(c)
# boss=boss()
# hh=boss.request()
# boss.guolv(hh)
# coon.close()

