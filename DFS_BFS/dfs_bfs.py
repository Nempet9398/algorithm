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
# 행이 3개인 2차원 인접리스트
graph = [[] for _ in range(3)]
graph[0].append((1,7))
graph[0].append((2,5))
graph[1].append((0,7))
graph[2].append((0,5))

print(graph)

#4 DFS 예제

graph =[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

def DFS(graph,v,visited):
    visited[v] = factorial_number
    print(v, end=' ')
    #다른 노드 재귀방문
    for i in graph[v]:
        if not visited[i]:
            DFS(graph,i,visited)

visited = [False] * 9

DFS(graph,1,visited)
