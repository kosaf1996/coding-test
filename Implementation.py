


def Up_Down_Left_Right():
    print('입력예시')
    print('5')
    print('L L L D')
    print('-------맵의 크기를 입력하시오--------')
    n = int(input())
    x, y = 1 , 1
    plans = input().split()

    #L R U D 의 따른 이동 방향
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types=['L','R', 'U','D']

    #이동 확인
    for plan in plans:
        #이동후 좌표 구하기
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx =x + dx[i]
                ny =y + dy[i]
        #공간을 벗어날 경우 무시 처리
        if nx < 1 or ny <1 or nx >n or ny > n :
            continue

        x, y = nx, ny

    print('x축 :',x ,'y축 :',y)

def Time():
    print('입력예시')
    print('N: 5')
    print('Num : 3')

    print('N :', end='')
    h = int(input())
    print('num : ', end='')
    num = input()

    count = 0
    for i in range(h + 1):
        for j in range(60):
            for k in range(60):
                #매 시각에 num 이 포함 된걸 count
                if num in str(i) + str(j) + str(k):
                    count +=1

    print(num,'의 갯수는 :',count)

def night():
    # 현재 나이트의 위치 입력받기
    input_data = input()
    row = int(input_data[1])
    #column 은 열을 위치를 반환해 준다.
    column = int(ord(input_data[0])) - int(ord('a')) + 1 #ord() a 를 넣으면 아스키코드를 반환
    # 나이트가 이동할 수 있는 8가지 방향 정의
    steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
    result = 0
    for step in steps:
    # 이동하고자 하는 위치 확인
        next_row = row + step[0]
        next_column = column + step[1]
        # 해당 위치로 이동이 가능하다면 카운트 증가
        if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
            result += 1
    print(result)

# 왼쪽으로 회전
def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3

    return direction



def Game_Developer():
    print('입력 예시')
    print('맵 생성 : 4 4')
    print('(1,1) 에 (0) 을 바로보고 서 있는 캐릭터 : 1 1 0')
    print('1 1 1 1 첫줄은 모두 바다')
    print('1 0 0 1 둘쨰 줄은 바다/육지/육지/육지')
    print('1 1 0 1 셋쨰 줄은 바다/바다/육지/바다')
    print('1 1 1 1 넷쨰 줄은 모두 바다 ')

    #N,M 공백으로 구분하여 입력받기
    n,m = map(int, input().split())

    #방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
    d = [[0] * m for _ in range(n)]

    #캐릭터의 X, Y , 방향을 입력받기
    x,y, direction = map(int, input().split())
    d[x][y] =1 #현재 좌표를 방문 처리

    #전체 맵 정보를 입력받기
    array =[]
    for i in range(n):
        array.append(list(map(int,input().split())))

    #북, 동. 남 ,서 Code 화
    dx =[-1, 0,1,0]
    dy =[0,1,0,-1]

    #시뮬레이션 시작
    count = 1
    turn_time = 0
    while True:
        #왼쪽으로 회전
        direction = turn_left(direction)
        nx =x + dx[direction]
        ny =y + dy[direction]
        #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
        if d[nx][ny] == 0 and array[nx][ny] == 0:
            d[nx][ny] = 1
            x = nx
            y = ny
            count += 1
            turn_time = 0
            continue

        #회전한 이후 정면에 가보지않은 칸이 없거나 바다인 경우
        else:
            turn_time +=1

        #네 방향 모두 갈 수 없는 경우
        if turn_time ==4:
            nx = x - dx[direction]
            ny = y - dy[direction]
            #뒤로 갈 수 있다면 이동
            if array[nx][ny] == 0:
                x = nx
                y = ny
            #뒤가 바다로 막혀있는 경우
            else:
                break
            turn_time =0

    print(count)




