from collections import deque

def Stack_ex():
    stack= []

    print('Stack Push : 5')
    stack.append(5)
    print('Stack Push : 2')
    stack.append(2)
    print('Stack Push : 3')
    stack.append(3)
    print('Stack Push : 5')
    stack.append(5)
    print('Stack Pop')
    stack.pop()
    print('Stack Push : 1')
    stack.append(1)
    print('Stack Push : 4')
    stack.append(4)
    print('Stack Pop ')
    stack.pop()

    print(stack)


def Queue_ex():
    #큐 구현 라이브러리
    queue = deque()

    print('Queue Push : 5')
    queue.append(5)
    print('Queue Push : 2')
    queue.append(2)
    print('Queue Push : 3')
    queue.append(3)
    print('Queue Push : 7')
    queue.append(7)
    print('Queue Pop')
    queue.popleft()
    print('Queue Push : 1')
    queue.append(1)
    print('Queue Push : 4')
    queue.append(4)
    print('Queue Pop')
    queue.popleft()

    print(queue)

def Adhacency_Matrix(): #DFS_ 인접행렬

    INF = 99999999 #무한의 비용 선언

    #2차원 리스트르르이용해 인접행렬 표현
    graph = [
        [0,7,5],
        [7,0,INF],
        [5,INF,0]
    ]
    print(graph)

def Adhacency_List(): #DFS_인접 리스트
    #행 이 3개인 2차원 리스트로 인접 리스트 표현
    graph = [[] for _ in range(3)]

    #노드 0 에 연결된 노드 정보 저장(노드, 거리)
    graph[0].append((1, 7))
    graph[0].append((2, 5))

    #노드 1에 연결된 노드 정보 저장
    graph[1].append((0, 7))

    #노드 2에 연결된 노드 정보 저장
    graph[2].append((0 ,5))

    print(graph)


def DFS_Stack():

    print('재귀함수를 이용해 Stack DFS 구현하였습니다.')
    # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원)
    graph = [
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

    #각 노드가 방문된 정보를 시트 자료형으로 표현
    visited = [False] * 9

    #정의된 dfs 함수 호출
    stack_dfs(graph,1,visited)
    print('')

def stack_dfs(graph, v, visited):
    #현재 노드 방문 처리
    visited[v] =  True
    print(v, end='')

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            stack_dfs(graph,i,visited)

def BFS_Que():
    print('재귀함수를 이용해 큐 BFS 구현하였습니다.')
    # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원)
    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]

    # 각 노드가 방문된 정보를 시트 자료형으로 표현
    visited = [False] * 9

    # 정의된 dfs 함수 호출
    que_bfs(graph, 1, visited)
    print('')

def que_bfs(graph, start, visited):

    #큐 라이브 러리 사용
    queue = deque([start])
    #현재 노드 방문 처리
    visited[start] = True

    #큐가 빌때까지 반복
    while queue:
        #큐에서 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end='')
        #해당 원소와 연결된 아직 방문하지 않은 원소들을 큐에 삽입
        for  i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True




def Drink():
    print('DFS 활용')
    print('입력 조건')
    print('- 첫번째 줄에 얼음 틀의 세로 길이 N 과 가로 길이 M 이 주어진다(1 <= N, M <= 1,000)')
    print('- 두 번쨰 줄부터 N + 1 번쨰 줄까지 얼음 틀의 형태가 주어진다 ')
    print('- 이떄 구멍이 뚫혀있는 부분은 0, 그렇지 않은 부분은 1 이다.')
    #2차원 리스트맵 입력받기
    n, m = map(int, input().split())

    #2차원 리스트의 맵 정보 입력받기
    graph = []


    for i  in range(n):
        graph.append(list(map(int, input())))

    # 모든 노드에 대하여 음료수 채우기

    result = 0
    for i in range(n):
        for j in range(m):
            # DFS수행
            if Drink_dfs(i, j,n,m,graph) == True:
                result += 1
    print(result)


def Drink_dfs(x,y,n,m,graph):
    #주어진 범위를 벗어나면 종료
    drink_a = n
    drink_b = m
    drink_graph = graph

    if x <= -1 or x >= n or y <= -1 or y >= m:

        return False

    #현재노드를 방문하지않음
    if graph[x][y] == 0:
        #해당 노드 방문처리
        graph[x][y] = 1
        #상하좌우 재귀적 호출
        Drink_dfs(x - 1,y,drink_a,drink_b,drink_graph)
        Drink_dfs(x, y - 1,drink_a,drink_b,drink_graph)
        Drink_dfs(x + 1, y,drink_a,drink_b,drink_graph)
        Drink_dfs(x, y + 1,drink_a,drink_b,drink_graph)
        return True
    return False

def Mirror():
    print('BFS 활용')
    #2차원 리스트맵 입력받기
    n, m = map(int, input().split())

    #2차원 리스트의 맵 정보 입력받기
    graph = []

    for i  in range(n):
        graph.append(list(map(int, input())))


    #이동할 네 장향 정의
    dx = [-1, 1,0,0]
    dy = [0,0,-1,1]

    print(Mirror_BFS(0,0,dx,dy,n,m,graph))

def Mirror_BFS(x,y,dx,dy,n,m,graph):
    queue =deque()
    queue.append((x,y))

    #큐가 없을 때까지 반복
    while queue:
        x,y = queue.popleft()

        #현재 네 위치에서 네방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #미로 팢기 공간을 벗어난 경우 무시
            if nx < 0 or ny <0 or nx >=n or ny >= m:
                continue

            #해당 노드를 처음 방문하는 경우 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

            #가장 오른쪽 아래까지 최단 거리 반환
            return graph[n-1][m-1]