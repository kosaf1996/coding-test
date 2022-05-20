# 피보나치 함수(Fibonacci Function)을 재귀함수로 구현
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

def fibo_call():
    print('입력예시')
    print('8 (Num 입력)')
    n = int(input())

    print(fibo(n))


def ant():
    print('입력예시')
    print('4')
    print('1 3 1 5')
    # 정수 N을 입력 받기
    n = int(input())
    # 모든 식량 정보 입력 받기
    array = list(map(int, input().split()))

    # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
    d = [0] * 100

    # 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
    d[0] = array[0]
    d[1] = max(array[0], array[1]) 
    for i in range(2, n):
        d[i] = max(d[i - 1], d[i - 2] + array[i])

    # 계산된 결과 출력
    print(d[n - 1])

def floor():
    print('입력예시')
    print('3')
    # 정수 N을 입력 받기
    n = int(input())

    # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
    d = [0] * 1001

    # 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
    d[1] = 1
    d[2] = 3
    for i in range(3, n + 1):
        d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

    # 계산된 결과 출력
    print(d[n])

def money():
    print('입력예시')
    print('2 500 (화폐종류, 금액의 합)')
    print('10 (10원)')
    print('100 (100원)')
    # 정수 N, M을 입력 받기
    n, m = map(int, input().split())
    # N개의 화폐 단위 정보를 입력 받기
    array = []
    for i in range(n):
        array.append(int(input()))

    # 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
    d = [10001] * (m + 1)

    # 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
    d[0] = 0
    for i in range(n):
        for j in range(array[i], m + 1):
            if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
                d[j] = min(d[j], d[j - array[i]] + 1)

    # 계산된 결과 출력
    if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
        print(-1)
    else:
        print(d[m])