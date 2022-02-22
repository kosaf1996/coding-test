import Greedy
import Implementation
import DFS_BFS

def main ():
    print('이 프로그램은 "이것이 취업을 위한 코딩테스트다 with 파이썬" 책의 내용을 프로그램화 한 내용입니다. ')
    while True:
        print('------------------Coding Test Run-------------------')
        print('1. Greedy(그리디)')
        print('2. Implementation(구현)')
        print('3. DFS/BFS(탐색 알고리즘)')
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
            print('-------DFS---------')
            print('3.DFS_인접행렬_기초')
            print('4.DFS_인접리스트_기초')
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


            elif a == 99:
                Greedy.turn()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

