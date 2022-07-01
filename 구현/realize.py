##1 상하좌우

n = 5
x=1
y=1
plans = "R R R U D D L".split()


# L R U D
dx =[-1,1, 0,0]
dy =[0,0,-1,1]
direction = ['L','R','U','D']
for i in plans:
    di_index = direction.index(i)

    x += dx[di_index]
    y += dy[di_index]

    if (x > n) or (x< 1) or (y <1) or (y >n):
        x -= dx[di_index]
        y -= dy[di_index]


print('x좌표는',x,'y좌표는',y)

##2 시각 3이들어간

# 0시00분00초부터 3시 59분 59초까지
n = 3
count = 0
for i in range(0,n+1):
    for j in range(0,60):
        for k in range(0,60):

            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)

##3 왕실의 나이트

input_data = 'd4'

y = int(ord(input_data[0])) - int(ord('a')) + 1
x = int(input_data[1])

go = [(-2,-1),(-2,1),(2,1),(2,-1),(-1,2),(1,2),(-1,-2),(1,-2)]


result = 0

for g in go:
    xx = x + g[0]
    yy = y + g[1]

    if (xx > 0) and (xx <= 8) and  (yy > 0) and (yy <= 8):
        result += 1

print(result)
