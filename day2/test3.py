
# 숫자 5개를 입력받아서 리스트에 저장해라

# 크기가 5인 리스트 모든값은 0으로

# list = [0] * 10

# print(list)

# list = [i for i in range(1,100+1)]

# print(list)


# list = [1,2,3,4,5]

# print(len(list))

# # for i in range(len(list)) :
# #     strval = int(input(f"{i}번째 숫자를 입력하세요 : "))
# #     list.insert(i,strval)
# #     list.pop()

# # print(list)



# print (max(list))


import random

print (random.randint(1,10))

#정답에 0을 입력하기 전까지 랜덤 구구단 문제 출력 정답, 오답 

while True :
    print("정답에 0을 입력하시면 종료됩니다..")

    num1 = random.randint(2,9)
    num2 = random.randint(1,9)

    ans  = num1 * num2 

    res = int(input(f'{num1} * {num2}  =  ')) 

    if res == 0 :
        print("종료합니다.")
        break
    elif ans == res : 
        print( "=" * 10 + "정답" + "=" * 10 )
    else :
        print( "=" * 10  + "오답" + "=" * 10 )