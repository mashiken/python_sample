
def say_hello():
    print("hello world")

say_hello()
say_hello()
say_hello()

def say_hello2(greeting):
    print(greeting)

hello = say_hello2
hello("Good evening")

def add(num01,num02):
    print(num01 + num02)

add(6,2)

def add2(num01,num02):
    return(num01 + num02)

print(add2(4,2))

#3つの引数を受け取る関数作成 9、4、2の平均
def ave(num01,num02,num03):
    return(num01 + num02 + num03) / 3

average = ave(9,4,2)
print(avarage)
average = ave(29,24,22)
print(average)

def num(sum01,sum02,sum03):
    return(sum01 + sum02 + sum03)

sum = num(10,20,30)
print(sum)