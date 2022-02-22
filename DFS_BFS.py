
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

from collections import deque
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