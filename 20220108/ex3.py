x = float(input())
y = float(input())

if x == 0 and y == 0:
    print(f'diem ({x},{y}) la goc toa do')
elif x > 0 and y > 0:
    print(f'diem ({x},{y}) nam o go I')
elif x < 0 and y > 0:
    print(f'diem ({x},{y}) nam o go II')
elif x < 0 and y < 0:
    print(f'diem ({x},{y}) nam o go III')
elif x > 0 and y < 0:
    print(f'diem ({x},{y}) nam o go IV')