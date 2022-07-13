## 큐 예제
from collections import deque

queue = deque()
queue.append(5)
queue.append(2)
queue.append(7)
print(queue) #deque([5, 2, 7])

queue.popleft() # 5가 빠져나감
queue.append(1)
queue.popleft() # 2가 빠져나감
print(queue) #deque([7, 1])

## 재귀함수를 이용한 팩토리얼

def factorial_number(n):
    if n <= 1:
        return 1

    return n * factorial_number(n-1) # n! = n * (n-1)! 구현

print(factorial_number(5))


#3 인접행렬

inf = 999999999

#0과 1은 7의 관계를
#0과 2는 5의 관계를
#1과 2는 연결되어있지 않음
graph = [
    [0,7,5],
    [7,0,inf],
    [5,inf,0]
]

#3-1 인접 리스트
