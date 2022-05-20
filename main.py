import Greedy
import Implementation
import DFS_BFS
import Sorting
import Binary_Search
import Dynamic
import Shortest_path
import Graph

def main ():
    print('이 프로그램은 "이것이 취업을 위한 코딩테스트다 with 파이썬" 책의 내용을 프로그램화 한 내용입니다. ')
    while True:
        print('------------------Coding Test Run-------------------')
        print('1. Greedy(그리디)')
        print('2. Implementation(구현)')
        print('3. DFS/BFS(탐색 알고리즘)')
        print('4. Sorting(정렬)')
        print('5. 이진탐색')
        print('6. 다이나믹 프로그래밍')
        print('7. 최단 경로')
        print('8. 그래프 이론')
        n = int(input())

        if n == 1:
            print('-----------------------Greedy------------------------') #탐욕법
            print('1.거스름돈 예제')
            print('2.큰수의 법칙 예제')
            print('3.숫자 카드 게임')
            print('4.1이 될떄 까지')
            print('5.돌아가기')

            a=int(input())

            if a == 1:
                Greedy.change_money()
            elif a == 2:
                Greedy.law_of_great_numbers()
            elif a == 3:
                Greedy.number_card_game()
            elif a == 4:
                Greedy.one()
            elif a == 5:
                Greedy.turn()

        elif n == 2:
            print('-----------------------Implementation------------------------') #완전탐색, 시물레이션 문제
            print('1.상하좌우')
            print('2.시간')
            print('3.왕실나이트')
            print('4.게임개발')
            print('5.돌아가기')


            a =int(input())
            if a == 1:
                Implementation.Up_Down_Left_Right()
            elif a == 2:
                Implementation.Time()
            elif a == 3:
                Implementation.night()
            elif a == 4:
                Implementation.Game_Developer()
            elif a ==5:
                Greedy.turn()

        elif  n == 3:
            print('-----------------------DFS/BFS(탐색 알고리즘)------------------------')

            print('------basics--------')
            print('1.Stack')
            print('2.Queue')
            print('-------DFS(깊이 우선 탐색)---------')
            print('3.DFS_인접행렬_기초')
            print('4.DFS_인접리스트_기초')
            print('5.Stack DFS')
            print('-------BFS(너비 우선 탐색)---------')
            print('6.Queue BFS')
            print('')
            print('7. 음료수 얼려먹기')
            print('8. 미로탈출')
            print('99.돌아가기')
            a =int(input())
            if a == 1:
                DFS_BFS.Stack_ex()
            elif a ==2 :
                DFS_BFS.Queue_ex()
            elif a == 3:
                DFS_BFS.Adhacency_Matrix()
            elif a == 4:
                DFS_BFS.Adhacency_List()
            elif a == 5:
                DFS_BFS.DFS_Stack()
            elif a == 6:
                DFS_BFS.BFS_Que()
            elif a == 7:
                DFS_BFS.Drink()
            elif a == 8:
                DFS_BFS.Mirror()

            elif a == 99:
                Greedy.turn()

        elif n == 4:
            print('-----------------------Sorting------------------------')
            print('1. 선택정렬')
            print('2. 삽입정렬')
            print('3. 위에서 아래로 ')
            print('4. 성적인 낮은 순서로 학생 출력하기')
            print('5. 두 배열의 원소 교체')
            print('99.돌아가기')

            a =int(input())
            if a == 1:
                Sorting.Sorting_Select()
            elif a == 2:
                Sorting.Sorting_Insert()
            elif a == 3:
                Sorting.UpDown()
            elif a ==4:
                Sorting.Student()
            elif a ==5:
                Sorting.Change()        
            elif a ==99:
                Greedy.turn()
        
        elif n == 5:
            print('-----------------------이진 탐색------------------------')
            print('1. 순차 탐색')
            print('2. 이진 탐색')
            print('3. 부품 탐색')
            print('4. 떡볶이 떡 만들기')
            print('99.돌아가기')

            a =int(input())
            if a == 1:
                Binary_Search.sequence_input()
            elif a == 2:
                Binary_Search.binary_input()
            elif a == 3:
                Binary_Search.parts_input()
            elif a == 4:
                Binary_Search.rice_cake()
            elif a ==99:
                Greedy.turn()

        elif n == 6:
            print('-----------------------다이나믹 프로그래밍------------------------')
            print('1. 피보나치 수열')
            print('2. 개미 전사')
            print('3. 바닥 공사')
            print('4. 효율적인 화폐 구성')

            print('99.돌아가기')

            a =int(input())
            if a == 1:
                Dynamic.fibo_call()
            elif a == 2:
                Dynamic.ant()
            elif a == 3:
                Dynamic.floor()
            elif a == 4:
                Dynamic.money()
            elif a ==99:
                Greedy.turn()
        
        elif n == 7:
            print('-----------------------최단 경로------------------------')
            print('1. ')
            print()

            print('99.돌아가기')

            a =int(input())
            if a == 1:
                Dynamic.fibo_call()

            elif a ==99:
                Greedy.turn()

        elif n == 8:
            print('-----------------------그래프 이론------------------------')
            print('1. ')
            print()

            print('99.돌아가기')

            a =int(input())
            if a == 1:
                Dynamic.fibo_call()

            elif a ==99:
                Greedy.turn()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

