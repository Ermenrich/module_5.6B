import random

def show_field(f):
    num ='  0 1 2 3 4'
    print(num)
    for row,i in zip(f,num.split()):
        print (f"{i} {' '.join(str(j) for j in row)}")

def users_input(f,user):
    while True:
        place=input(f"Ходит {user} .Введите координаты:").split()
        if len(place)!=2:
            print('Введите две координаты')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue
        x, y = map(int, place)
        if not(x>=0 and x<5 and y>=0 and  y<5):
            print('Вышли из диапазона')
            continue
        if  f[x][y]!='-':
            print('Клетка занята')
            continue
        break
    return x,y

def win_position(f,user):
    f_list=[]
    print(f)
    for l in f:
        f_list+=l
    print(f_list)
    positions=[[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24],
               [0,5,10,15,20],[1,6,11,16,21],[2,7,12,17,22],[3,8,13,18,23],[4,9,14,19,24],
               [0,6,12,18,24],[4,8,12,16,20]]
    indices = set([i for i, x in enumerate(f_list) if x == user])

    for p in positions:
        if len(indices.intersection(set(p)))==5:
            return True
    return False

def start(field):

    count=0
    while True:
        show_field(field)
        if count%2==0:
            user='x'
            x, y = users_input(field, user)
        else:
            user = 'o'
            print('Ходит 0')
            x, y = random.randint(0, 4), random.randint(0, 4)
        while field[x][y] != '-':
            x, y = random.randint(0, 4), random.randint(0, 4)
            continue
        if count<24:
            field[x][y] = user
        elif count==24:
            print ('Ничья')
            break
        if win_position(field,user):
            print(f"Выйграл {user}")
            break
        count+=1

field = [['-'] * 5 for _ in range(5)]

start(field)
















