import sys
input = sys.stdin.readline

while 1:
    x, y, z = map(int, input().split())

    if x==0 and y == 0 and z == 0:
        break
    tri = [x,y,z]
    tri = sorted(tri)

    if (tri[0]**2 + tri[1]**2) == tri[2]**2:
        print('right')
    else:
        print('wrong')

