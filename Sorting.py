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