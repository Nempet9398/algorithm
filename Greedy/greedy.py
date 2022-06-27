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
