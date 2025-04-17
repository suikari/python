num = "10"

chk = True

count = 0
reCount = 1
print('Hello Python');

def test(i) :
    global count
    if (i > 0) : print("*" * i + " " * (count)   + "*" * i) ;  i = i-1 ; count = count + 2 ; test(i);

def testre(i) :
    global count
    global reCount
    if ( reCount <= i) : count = count - 2 ;  print("*" * ( reCount ) + " " * (count) + "*" * ( reCount )) ;  reCount = reCount + 1 ;  testre(i);

testindex = int(input("반복횟수 : "));

test(testindex);
testre(testindex);


print(type(num));


print(f'{testindex}만큼 반복한 {chk} 상태입니다.')

print(chk)


str1 = "abcdefg"

print(str1[::2])


str2 = [1,2,3,4,5,6]

print(str2)

print (str2[::2])
print (str2[1::2])



