import random


# def reverse_string(s):
#     for str in range(1,len(s)+1,1) :
#         print(s[-str],end="")


# reverse_string('testsss')

###########22222##############

# count = 0
# lottoindex = [0] * 6
# flg = False

# while count < 6 :
#     lotoval = random.randint(1,45)

#     for i in range(len(lottoindex)) : 
#         if lotoval == lottoindex[i] :
#             flg = True

#     if flg == False :            
#         lottoindex[count] = lotoval
#         count += 1 
    
#     flg = False

# print(lottoindex)    

#############3333###################


# str = "this is a title"
# strlist = []

# strlist = str.split(" ")

# for str in range(len(strlist)) : 
#     strlist[str] = strlist[str].capitalize()
    
# print(' '.join(strlist))


###############444444#################


# liste = [1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,1,2,3,5,6,7]

# setlist = []

# def compree_list(list) :
#     for val in range(len(list)) :
#         if (val == 0 ) :
#             setlist.append(list[val])
#         elif (list[val-1] == list[val]) : 
#             continue
#         else:
#             setlist.append(list[val])

# compree_list(liste)

# print(setlist)

################5555555555######################

# 5. 자리수 분리 및 합계 구하기
# 정수 하나를 입력받아, 각 자리의 숫자를 분리해서 리스트로 반환하고,
# 그 자리수들의 합도 같이 반환하는 함수

# func(1234) → ([1, 2, 3, 4], 10)
# func(908) → ([9, 0, 8], 17)

# def split_sum(num) : 
#     setval = []
#     strnum = str(num)
#     for val in range(len(strnum)) :
#         setval.insert(val,int(strnum[val]))
#     sumval = sum(setval)
#     return setval , sumval

# print(split_sum(1234))
# print(split_sum(908))