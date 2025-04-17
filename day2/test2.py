

fruits = ["apple","orange","banana"]

# if "apple" in fruits : 
#     print("사과는 포함되어있습니다.")
# else :
#     print("사과 없다 ")



# txt = "Hello Python"

# if "Python" in txt :
#     print("파이썬 있네")


# hong =  { "name" : "길동" , "age" : "30" , "addr" : "인천" }


# if "name" in hong : 
#     print("이름 있다")

# if "길동" in hong.values() :
#     print("길동 있다")

# if "name" in hong.keys() :
#     print("이름 있다")

# count = 0
# for i in range(1,10+1,1) :  
#     count = count + i
#     #pass
#     #print(i, end=" ")

# print(count)


# for i in range(2,10) :
#     for j in range(1,10) :
#         print(f'{i} * {j} = {i*j}')


# list = ["banana","orange","apple"]

# for fruit in list :
#     print(fruit)


# text = "Hello Python"

# for char in text :
#     print(char, end="")


# list = ["banana","orange","apple"]

# for idx, fruit in enumerate(list) :
#     print(f"{idx+1} : {fruit}")


hong = {"name" : "홍길동" , "age" : 30, "addr" : "인천" }

for key, value in hong.items() :
    print(f'{key} : {value}')

for key in hong :
    print(f'{key} : {hong[key]}')

# print("갉" * 10)

