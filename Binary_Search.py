# 순차 탐색 소스코드 구현
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재의 위치 반환 (인덱스는 0부터 시작하므로 1 더하기)
    return -1 # 원소를 찾지 못한 경우 -1 반환



def sequence_input():
    print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
    print('입력 예시')
    print('5 3')
    input_data = input().split()
    n = int(input_data[0]) # 원소의 개수
    target = input_data[1] # 찾고자 하는 문자열

    print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
    print('입력 예시')
    print('1 2 3 4 5')  
    array = input().split()

    # 순차 탐색 수행 결과 출력
    print(sequential_search(n, target, array))



# 이진 탐색 소스코드 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

def binary_input():
    print('입력 예시')
    print('7 10')
    print('1 3 5 7 9 11 13')
    # n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
    n, target = list(map(int, input().split()))
    # 전체 원소 입력 받기
    array = list(map(int, input().split()))

    # 이진 탐색 수행 결과 출력
    result = binary_search(array, target, 0, n - 1)
    if result == None:
        print("원소가 존재하지 않습니다.")
    else:
        print(result + 1)


# 이진 탐색 소스코드 구현 (반복문)
def parts_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
        else:
            start = mid + 1
    return None


def parts_input():
    print('입력 예시')
    print('5 (매장의 부품 종류 개수)')
    print('8 3 7 9 2(부품 번호)')
    print('3(찾을 부품의 수)')
    print('5 7 9(찾을 부품의 번호)')
    # N(가게의 부품 개수) 입력
    n = int(input())
    # 가게에 있는 전체 부품 번호를 공백을 기준으로 구분하여 입력
    array = list(map(int, input().split()))
    array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행
    # M(손님이 확인 요청한 부품 개수) 입력
    m = int(input())
    # 손님이 확인 요청한 전체 부품 번호를 공백을 기준으로 구분하여 입력
    x = list(map(int, input().split()))

    # 손님이 확인 요청한 부품 번호를 하나씩 확인
    for i in x:
        # 해당 부품이 존재하는지 확인
        result = parts_search(array, i, 0, n - 1)
        if result != None:
            print(i,' : yes' )
        else:
            print(i,' : no')


def rice_cake():
    print('입력 예시')
    print('4 6(떡의 개수, 원하는 길이)')
    print('19 15 10 17(떡 4개의 길이)')
    # 떡의 개수(N)와 요청한 떡의 길이(M)을 입력
    n, m = list(map(int, input().split(' ')))
    # 각 떡의 개별 높이 정보를 입력
    array = list(map(int, input().split()))

    # 이진 탐색을 위한 시작점과 끝점 설정
    start = 0
    end = max(array)

    # 이진 탐색 수행 (반복적)
    result = 0
    while(start <= end):
        total = 0
        mid = (start + end) // 2
        for x in array:
            # 잘랐을 때의 떡볶이 양 계산
            if x > mid:
                total += x - mid
        # 떡볶이 양이 부족한 경우 더 많이 자르기 (오른쪽 부분 탐색)
        if total < m:
            end = mid - 1
        # 떡볶이 양이 충분한 경우 덜 자르기 (왼쪽 부분 탐색)
        else:
            result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
            start = mid + 1

    # 정답 출력
    print(result)