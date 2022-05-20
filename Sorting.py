def Sorting_Select():
    array = [7,5,9,0,3,1,6,2,4,8]

    for i in range(len(array)):
        min_index = i #가장작은 원소 인덱스
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index],array[i] #Swap
    print(array)

def Sorting_Insert():
    array = [7,5,9,0,3,1,6,2,4,8]

    for i in range(1,len(array)):
        for j in range(i, 0, -1): #index i 부타 1까지 감소하며 반복하는 문법
            if array[j] < array[j - 1]: #한 칸씩 왼쪽으로 이동
                array[j], array[j -1 ] = array[j -1], array[j]
            else:
                break
    print(array)

def UpDown():

    n = int(input())

    array = []
    for i in range(n):
        array.append(int(input()))

    #파이썬 정렬 라이브러리
    array = sorted(array, reverse=True)

    #결과 출력
    for i in array:
        print(i, end='')
    print('')

def Student():
    n = int(input())

    array = []
    for i in range(n):
        input_data = input().split()

        #이름은 문자열 점수를 정수령 변환저장
        array.append((input_data[0], int(input_data[1])))

    array =sorted(array, key=lambda student: student[1])

    for student in array:
        print(student[0], end='')
    print('')


def Change() :
    print('입력 예시')
    print('5 3')
    print('1 2 5 4 3')
    print('5 5 6 6 5')
    n, k = map(int, input().split()) # N과 K를 입력 받기
    a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력받기
    b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력받기

    a.sort() # 배열 A는 오름차순 정렬 수행
    b.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

    # 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
    for i in range(k):
        # A의 원소가 B의 원소보다 작은 경우
        if a[i] < b[i]:
            # 두 원소를 교체
            a[i], b[i] = b[i], a[i]
        else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
            break

    print(sum(a)) # 배열 A의 모든 원소의 합을 출력