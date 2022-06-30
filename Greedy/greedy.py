## 1번 - 거스름돈 문제

n = 1260 ## 거스름돈

count = 0 ## 거스름돈의 개수

coin_type = [500,100,50,10]

for coin in coin_type:
    count += n // coin ## 몫으로 큰 동전 개수 구하기
    n %= coin

print(count)


## 2번 -큰수의 법칙

## basic 풀이
n = 5
m = 8
k = 3
data = [2,4,5,4,6]
data.sort()

result = 0
temp = 0

for i in range(0,m):
    if temp != k:
        result += data[n-1]
        temp += 1
    else:
        result += data[n-2]
        temp = 0

print(result)

## 효율적 코드

n = 5
m = 8
k = 3
data = [2,4,5,4,6]
data.sort()

## 연산 줄이기 위한 방법
result = (data[n-1] * 3 + data[n-2]) * (m//(k+1)) + data[n-1] * (m%(k+1))

print('효율적인 결과', result)


## 3번 숫자 카드 게임

## input data
n = 3
m = 3
first = [3,1,2]
second = [4,1,4]
third = [2,2,2]
data_list = [first,second,third]

result = 0
for i in range(n):
    data = data_list[i]

    min_value = min(data)
    result = max(result,min_value)

print('this is the max value' ,result)

##4번 1이될 때까지

n= 623
k = 12
rep = 0

while n != 1:
    ## 나머지가 0이면 k로 나누고 rep 1 추가
    if n % k == 0:
        n = n / k
        rep += 1
    ## 나머지가 0이 아니면 k로 나누고 나머지만큼 n에서 빼고 횟수 n 증가
    else:
        if n > k:
            na = n % k
            n = n - na
            rep += na
        ## n < k 가 되면 n이 1이 될 때까지 배주기
        else:
            rep += (n-1)
            n = 1
print(rep)
