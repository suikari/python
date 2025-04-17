t,a,b = (1,),2,3
#k,o,g = 1, ,2,3


a = (10,20,30,40)

print(a) 
print(type(a))

a = (30,40,50,60)

print(a)

menu=  {"김밥":2000,"라면":3500,"어묵":1000}

print(menu["김밥"])
print(menu.keys())
print(menu.values())
print(menu.items())


name = {100:"홍길동",200:"김철수",300 : "박영희"}

#print
del(name[300])

print(name)

print(name.pop(200))

print(name)

a = {10,20,30,10}


print(a)


# num = int(input("숫자 입력 : "))
# #입력값 >5 
# ## 들여쓰기로 구분 중괄호 x
# if num > 5 : 
#     print("입력값이 5보다 큽니다.")
# else :  
#     print("5보다 작거나 같습니다.")  





# 숫자 하나 받아서

# num1 = int(input("숫자를 입력하세요"))


# if num1 % 2 > 0  :
#     print("홀수입니다.")
# elif num1 == 0 :
#     print("0은 사용할 수 없습니다.")
# else : 
#     print("짝수입니다.")


pay = 20000


age = int(input('나이를 입력하세요 : '))

if 1 <= age < 6 :
    print("1세부터 5세까지는 입장료 무료")
elif 6 <= age < 60 :
    print(f'입장료는 {pay} 입니다.')
elif 61 < age < 100  : 
    print(f'입장료는 {pay * 0.5} 입니다')
else :
    print('값을 잘못입력하셨습니다.')