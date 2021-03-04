def Ai():
    while True:
        print('1.查詢')
        print('2.刪除')
        print('3.關閉')
        chear=int(input('請輸入數字:'))

        while chear not in range(0,4):
            print('請重新輸入')
            chear = int(input('請輸入數字:'))

        if chear == 3:
            print('謝謝')
            break
Ai()