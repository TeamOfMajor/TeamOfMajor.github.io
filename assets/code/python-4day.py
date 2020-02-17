# 1
x = 1
y = 2
print(x)
print(y)
z = "안녕"
print(z)
# 2
x = 1
y = 2
z = 1.2
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y) #제곱
print(x % y) #나머지
# 3
x = "hello"
y = 'bye'
z = """
이것은
혁신이다
"""
print ( x + y)
# 4
x = 4 # 숫자 타입
y = "4" #문자열 타입
print((str(x)) + y)
print(x + (int(y)))
# 5
x = True
y = False
print(x)
print(y)
# 6
if 2 > 1:
    print("hello")
if 2 > 1 and 3 > 2:
    print("AND 는 둘다 참인것!")
if 2 > 1 or 3 > 4:
    print("OR은 둘중 하나만 참이면 노출!")
x = 5
if x > 5:
    print("if 1단계")
elif x == 3:
    print("if 2단계")
else:
    print("if 3단계")
# 7
def chat():
    print("Moon: 안녕 몇살이니?")
    print("Kim: 나의 나이는 20")
chat()
def chat(name1, name2, age):
    print("%s: 안녕 몇살이니?" % name1)
    print("%s: 나의 나이는 %d" % (name2, age))
chat("M", "K", 30)
def dsum(a, b):
    result = a + b
    return (result)
d = dsum(2, 3)
print(d)
# 8
def study(name, age):
    if age < 10:
        print("%s 안녕" % name)
    elif age > 10 and age < 20:
        print("%s 안녕하세요" % name)
    else:
        print("%s 안녕하십니까" % name)
study("Moon", 11)