#程序1：变量与打印(变量赋值、f-string格式化)
name="小马"
age=18
print(f"我叫{name},今年{age}岁了")

#条件判断(if/elif/else分支)
score=95
if score>=90:
    print("优秀")
elif score>=70:
    print("还行")
else:
    print("糟糕")

#for循环(range()、for循环)
for a in range(1,5):
    print(f"第{a}次循环")

#while循环(while循环、自增)
count=0
while count<6:
    print(f"count={count}")
    count+=1

#列表循环(list的append、遍历、len())
fruits=["apple","banana","orange","mango"]
fruits.append("葡萄")
for fruit in fruits:
    print(fruit)
    print(f"有{len(fruit)}种水果")

# 字典操作(dict的增改查、items()遍历)
user={"name":"小马","age":18,"city":"西安"}
print(user["name"])
user["email"]="979710528@qq.com"
for key,value in user.items():
    print(user["{key};{value}"])

# 函数定义(def 定义函数、参数、默认值、return)
def add(a, b):
    return a + b

result = add(3, 5)
print(f"3+5={result}")

def greet(name="朋友"):
    return f"你好，{name}！"

print(greet())
print(greet("小红"))

# 文件读写(with 上下文管理器、文件读写模式)
# 写入文件
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("这是第一行\n")
    f.write("这是第二行\n")

# 读取文件
with open("test.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# 异常处理(try/except/finally、常见异常)
try:
    num = int(input("请输入一个数字："))
    result = 10 / num
    print(f"10/{num}={result}")
except ValueError:
    print("输入的不是数字！")
except ZeroDivisionError:
    print("不能除以0！")
finally:
    print("程序执行完毕")

# 综合小项目——自动化测试数据生成器(综合运用：函数、循环、列表推导式、字典、random 模块)
import random

def generate_test_users(count):
    """生成测试用户数据"""
    users = []
    for i in range(1, count + 1):
        user = {
            "id": i,
            "username": f"user_{i}",
            "email": f"user_{i}@test.com",
            "age": random.randint(18, 60),
            "is_active": random.choice([True, False])
        }
        users.append(user)
    return users

# 生成5个测试用户
test_users = generate_test_users(5)
for user in test_users:
    print(user)

# 统计活跃用户
active_users = [u for u in test_users if u["is_active"]]
print(f"\n活跃用户数：{len(active_users)}")