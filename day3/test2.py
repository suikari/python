

# def score(kor, eng, math) :
#     sum = kor + eng + math
#     avg = sum / 3
#     return sum, avg



# total, average = score(50,88,77)

# print(f'총 {total} 점, 평균 {average:.2f}점')



# import statistics


# def score(*testval) :
#     sum1 = sum(testval)
#     #avg1 = sum1 / len(testval)
#     avg1 = statistics.mean(testval)
    
#     return sum1, avg1


# asw = score(60,87,70)

# print(asw)


# x = 10

# def test() :
#     # global x
#     x = 20


# test()
# print(x)


fac_val = 1

# def fac(val) :
#     global fac_val 
#     if val > 0 :
#         fac_val *= val
#         fac(val-1)
#     else  :
#         print(fac_val)
    
# fac(5)

# def fac(val) :
#     global fac_val 
#     if val < 1 :
#         return 1    
#     else :
#         return  val * fac(val-1)

# print(fac(5))

# fac_val = 1
# def refac(val) : 
#     global fac_val
    
#     for i in range(val,0,-1) :
#         fac_val *= i

#     print(fac_val)
    
# refac(5)



def fib(val) :
    if val == 1 :
        return 1
    elif val == 0 :
        return 0
    else :
        return fib(val-1) + fib(val-2)


