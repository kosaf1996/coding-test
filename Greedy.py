def change_money(): #거스름돈
    n= 1260
    count =0

    coin_types = [500, 100, 50, 10]

    for coin in coin_types:
        count += n // coin
        n %= coin

    print('거스름돈 예제 결과 : ',count)


def law_of_great_numbers(): #큰수의 법칙

    print('큰수의 법칙 입력 예제')
    print('5 8 3')
    print('2 4 1 6 9')
    n, m, k = map(int, input().split())

    data = list(map(int, input().split()))

    data.sort() #입력받은 data 정렬
    first = data[n-1] #가장큰수
    second = data[n-2] #두번쨰 큰수

    #가장큰수가 더해지는 횟수
    count = int(m / (k + 1)) * k # (8 / (3+1)) * 3 = 6
    count += m % (k + 1) #8 % (3 +1 ) = 0

    result = 0
    result += (count) * first #가장 큰수 더하기 6 * 9 = 54
    result += (m-count) *second #두 번쨰로 큰수 더하기 (8-2) * 6 = 12

    print(result)

def number_card_game(): #숫자 카드 게임
    print('입력 예시')
    print('2 4')
    print('3 1 2 4')
    print('3 3 3 3')
    
    n, m = map(int,input().split())

    result =0
    #data 입력 받기
    for i in range(n):
        data = list(map( int,input().split()))
        #가장 작은수
        min_value = min(data)
        #가장 작은수 중 가장 큰 수
        result = max(result, min_value)
    print(result)

def one(): #1이 될떄 까지
    print('입력 예시')
    print('25 5')

    n, k = map(int,input().split())
    result = 0

    #N 이 K 이상이면 계속 나눔
    while n >= k:
        #N이 K 로 나누어 떨어지지 않는다면 1씩 뺴기
        while n % k != 0:
            n-=1
            result +=1

        n//=k
        result += 1

    #마지막 남은 수에 대해 1씩 뺴기
    while n>1:
        n-=1
        result +=1

    print(result)

def turn():
    return