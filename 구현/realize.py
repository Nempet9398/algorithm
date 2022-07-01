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
