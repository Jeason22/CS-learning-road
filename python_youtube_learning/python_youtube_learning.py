# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:42:37 2020
python 学习记录 
@author: Jeason Wu

#数据结构(字符串、数字、布尔值)
character_name = "Tom"
character_age = 50  
is_male = True    #\False

#打印函数用法
phrase = "Giraffe Academy"
print(phrase + "is cool ")
print(phrase.upper())#转换字符串都为大写
print(phrase.lower())#转换字符串都为小写
print(phrase.upper().isupper())#转换字符串都为大写后判断字符串都为大写（函数组合）
print(phrase.islower())#判断字符串都为小写
print("This is a "+ phrase,"")
print(len(phrase))#求字符串长度
print(phrase[0])#索引字符串首元素
print(phrase.index("a"))#按照参数索引元素位置
print(phrase.replace("Giraffe","Elephant"))#替换字符串内容

#数字类型
my_num = -5
print(my_num)
print(str(my_num) + " is my favorite number")#强制类型转换
print(2)
print(-2.4287)#可打印浮点数、小数、复数
print(3 + 4.5)#基本运算+-*/%（具有运算优先级）
print(abs(my_num))#求绝对值
print(pow(2,3))#求次方幂
print(sqrt(36))#求平方根
print(max(4,7))#打印较大的数
print(min(4,7))#打印较小的数
print(round(3.5))#四舍五入近似
from math import*#可以获取跟多的数学函数
print(floor(3.7))#向下取整
print(ceil(3.7))#向上取整

#来自用户的输入
name = input("Enter your name:")
age = input("Enter your age:")
print("Hello " + name + "! You are " + age + "!")
#Building a basic calculator(加法运算计算器)
num1 = input("enter a number:")
num2 = input("enter another number:")
result = float(num1) + float(num2)
print(result)
#mad a lib(输入颜色、复数名词、名人)
color = input("enter a color:")
plural_noun = input("enter a plural noun:")
celebrity = input("enter a celebrity:")
print("rose are " + color)
print(plural_noun + " are blue")
print("i love " + celebrity)

#list(列表)
friends = ["Kevin","Karen","Jim","Oscar","Toby","Mike"]#里面也可以写数字、borl值。例如：  friends = ["Kevin",2,False]
print(friends)
print(friends[0])#索引列表中的元素，从零开始
print(friends[1])
print(friends[2])
print(friends[-1])#表示从后往前索引倒数第一个
print(friends[1:])#索引第二个到所有的元素
print(friends[1:3])#索引第一个和第二个元素
friends[2] = "Bob" #替换列表种的元素
print(friends)
#list functions（列表功能）
lucky_numbers = [4,24,432,16,23,42]
friends = ["Kevin","Karen","Jim","Oscar","Jim","Toby","Mike"]#里面也可以写数字、borl值。例如：  friends = ["Kevin",2,False]
friends.extend(lucky_numbers)#两个列表扩展成一个列表
friends.append("Cread") #列表最好添加元素
friends.insert(1,"Kelly")#插入
friends.remove("Oscar")#移除
friends.pop()#删除最后一个元素
friends.clear()#删除列表所有元素
print(friends)
print(friends.index("Kevin"))#索引元素的位置
print(friends.count("Jim"))#查找元素出现的次数
lucky_numbers.sort()#升序排列
print(lucky_numbers)
lucky_numbers.reverse()#降序排列
print(lucky_numbers)
friends2 = friends.copy()#复制列表副本
print(friends2)

#tuples（元组）
coordinates = (4,5)#元组一旦创建，其内元素不可改变
coordinates2 = [(4,5),(24,34)]#列表内镶嵌元组
print(coordinates[0])#索引第一个元素
print(coordinates2)

#functions（功能）
def say_hi():#创建一个函数
    print("hello user")
say_hi()#调用执行函数

def say_hi(name,age):#创建一个函数,形参
    print("hello " + name + ", you are "+age +".")
say_hi("mike","28")#调用执行函数，输入实际参数

def say_hi(name,age):#创建一个函数,形参
    print("hello " + name + ", you are "+ str(age) +".")
say_hi("mike",28)#调用执行函数，输入实际参数

#return statement
def cube(num):
    return num*num*num
print(cube(4))

def cube(num):
    return num*num*num
result = cube(4)
print(result)

#if statements（如果语句）
is_male = False
is_tall = True
if is_male and is_tall:#逻辑条件为真则执行下面缩进的语句
    print("you are a male or tall or both! ")
elif is_male and not(is_tall):
    print("you are a short male!")
elif not(is_male) and is_tall:
    print("you are not a male but are tall")
else:#逻辑条件为假则执行下面缩进的语句you are a short male
    print("you are neither male nor tall!")

#if statements& comparisons(如果语句与比较)
def max_num(num1,num2,num3):
     if num1 >= num2 and num1 >= num3:
         return  num1
     elif num2 >= num1 and num2 >= num3:
         return  num2
     else:
         return num3   
print(max_num(3,2,1))

#building a better calculator(加减乘除计算器)
num1 = float(input("enter first number:"))
op = input("enter operator:")
num2 = float(input("enter second number:"))
if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("invalid operator")

#Dictionaries(字典){"键":"值"} 键可以为数字、字符串
month_conversions = {"Jan":"January",
                     "Feb":"February",
                     "Mar":"March",
                     "Apr":"April",
                     5:"May",
                     "Jun":"June",
                     "Jul":"July",
                     "Aug":"August",
                     "Sep":"September",
                     "Oct":"October",
                     "Nov":"November",
                     "Dec":"December",
                     }
print(month_conversions["Jun"])
print(month_conversions.get(5))
print(month_conversions.get("Lv","not the valid key"))

#While loop(while 循环)
i = 1
while i <= 100:
     print(i)
     i = i + 5
print("done  with loop")

#Building a guessing game（建立一个猜谜游戏）
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter guess:")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("out of guesses,you lose!")
else:
    print("you win!")

#For loop(for 循环)（多用来遍历）
for letter in "giraffe academy":
    print(letter)
print("     ")#打印空格

friends = ["Jim","Karen","Kevin"]
for friend in friends:
    print(friend)
print("     ")#打印空格

for index in range(len(friends)):
    print(friends[index])
print("     ")#打印空格
    
for index in range(10):
    print(index)
print("     ")#打印空格

for index in range(3,10):
    print(index)
print("     ")#打印空格

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("not first")

#Exponent Function(指数函数)
print(2**3)#之间打印实现
print("现在开始指数计算，接下来按照提示输入两个值！")
a = int(input("enter a base_num:"))
b = int(input("enter a pow_num:"))
def raise_to_power(base_num,pow_num):#采用for循环实现
    result = 1
    for index in range(pow_num):
        result = result*base_num
    return    result
print(raise_to_power(a,b))

#2D lists &nested loops(2维列表和镶嵌循环)
number_grid = [#定义了一个4x3的数组
[1,2,3],
[4,5,6],
[7,8,9],
[0,0,0]
        ]
print(number_grid[1][2])#打印2行3列的元素
print("     ")#打印空格

for row in number_grid:
    print(row)
    for col in row:
        print(col)

#Build a Translator(a.e.i.o.u变成g)
def translate(phrase):
    translation = ""
    for letter in phrase:    
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
print(translate(input("enter a prrase:")))

#Comments(注释)
print("comments are fun!you can use # to comments!")

#try&except(捕获项目中的错误)
try:
    number = int(input("enter a number:"))
    print(number)
    sum = 10/0
except ValueError:
    print("invalid input")
except ZeroDivisionError:#(第一种形式)
    print("divided by zero")
except ZeroDivisionError as err:#（第二张形式）
    print(err)

#Reading Files(文件操作相关命令函数)
employee_file = open("python.txt",encoding="gb18030", errors='ignore')
#r代表读，w代表写,擦除原先的内容，a代表可末尾添加内容,'r+':表示对文件进行可读写操作（删除以前的所有数据）
#'r+a'：表示对文件可进行读写操作（添加到当前文件尾部）,'b':表示要读写二进制数据
print(employee_file.readable())#检测文件可读性
print(employee_file.read())#读取文档内容
print(employee_file.readlines())#读取文档以数组方式输出
print(employee_file.readlines()[1])#读取文档以数组方式输出第一行
print(employee_file.readline())#读取文档第一行
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

#Writing to Files
employee_file = open("python.txt","a")
employee_file.write("\nyou successly write a word!")
employee_file.close()

employee_file = open("python.html","w")
employee_file.write("welcome my html")
employee_file.close()

#Modules and Pip
import useful_tools#调用useful_tools.py模块
print(useful_tools.roll_dice(3))

#Class and Objects(类（定义自己的数据类型）和对象(对数据类型的概况))
from student import students
student1 = students("wushunquan","aut",3.5,False)
print(student1.name)
"""
#building a multiple choice quiz(建立多项选择测验)

#Object Functions(对象函数)

#Inheritance(继承)

