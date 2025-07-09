from operator import eq
from colorama import Fore, Back, Style
import pandas as pd

counting = 1
move = 0
x1 = 0
y1 = 0
AI_count = 1
turn = 1

#board Setting
board = [["NON" for j in range(8)] for i in range(8)]
#black
board[0][0] = "BR1"
board[0][1] = "BN1"
board[0][2] = "BB1"
board[0][3] = "BK1"
board[0][4] = "BQ1"
board[0][5] = "BB2"
board[0][6] = "BN2"
board[0][7] = "BR2"
for i in range(8):
    board[1][i] = "BP" + str(i+1)

#white
board[7][0] = "WR1"
board[7][1] = "WN1"
board[7][2] = "WB1"
board[7][3] = "WQ1"
board[7][4] = "WK1"
board[7][5] = "WB2"
board[7][6] = "WN2"
board[7][7] = "WR2"
for i in range(8):
    board[6][i] = "WP" + str(i+1)

#AI
class educating1:
    def setdata(self, move, place):
        self.move = move
        self.place = place

openning1 = educating1()
openning2 = educating1()
openning3 = educating1()
openning4 = educating1()
openning5 = educating1()
openning6 = educating1()
openning7 = educating1()
openning8 = educating1()
openning9 = educating1()
openning10 = educating1()

class educating2:
    def setdata(self, move, place):
        self.move = move
        self.place = place

openning2_1 = educating2()
openning2_2 = educating2()
openning2_3 = educating2()
openning2_4 = educating2()
openning2_5 = educating2()
openning2_6 = educating2()
openning2_7 = educating2()
openning2_8 = educating2()
openning2_9 = educating2()
openning2_10 = educating2()

def AI_educating():
    global counting
    if turn == 1:
        if counting == 1:
            openning1.move = move
            openning1.place = [xp, yp]

        elif counting == 2:
            openning2.move = move
            openning2.place = [xp, yp]

        elif counting == 3:
            openning3.move = move
            openning3.place = [xp, yp]

        elif counting == 4:
            openning4.move = move
            openning4.place = [xp, yp]

        elif counting == 5:
            openning5.move = move
            openning5.place = [xp, yp]

        elif counting == 6:
            openning6.move = move
            openning6.place = [xp, yp]

        elif counting == 7:
            openning7.move = move
            openning7.place = [xp, yp]

        elif counting == 8:
            openning8.move = move
            openning8.place = [xp, yp]

        elif counting == 9:
            openning9.move = move
            openning9.place = [xp, yp]

        elif counting == 10:
            openning10.move = move
            openning10.place = [xp, yp]

        counting += 1

#Searching function
def searching(b):
    tester = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == b:
                x = int(i)
                y = int(j)
                tester = 1
            else:
                tester = tester

    if tester == 1:
        print(b + " is at (" + str(x + 1) + ", " + str(y + 1) + ")")
        return x, y
    else:
        print(b + " is not in defined")
        return 100, 100

def searching_end(b):
    tester = 0
    for i in range(8):
        for j in range(8):
            if board[i][j] == b:
                tester = 1
            else:
                tester = tester

    if tester == 0:
        return 0
    else:
        return 1

#WP
#forward
def wp_forward(a, b, c):
    if eq(board[b - 1][c],'NON'):
        board[b][c] = "NON"
        board[b - 1][c] = a
        AI_educating()

    else:
        print("can't move")

#p_forward
def wp_p_forward(a, b, c):
    if b == 6:
        if eq(board[b - 2][c], 'NON'):
            board[b][c] = "NON"
            board[b - 2][c] = a
            AI_educating()

        else:
            print("can't move")
    else:
        print("can't move")

#eat_left
def wp_eat_left(a, b, c):
    if eq(board[b - 1][c - 1],'NON'):
        print("can't move")
    else:
        board[b][c] = "NON"
        board[b - 1][c-1] = a
        AI_educating()

#eat_right
def wp_eat_right(a, b, c):
    if eq(board[b - 1][c + 1],'NON'):
        print("can't move")
    else:
        board[b][c] = "NON"
        board[b - 1][c + 1] = a
        AI_educating()

#BP
#forward
def bp_forward(a, b, c):
    if eq(board[b + 1][c],'NON'):
        board[b][c] = "NON"
        board[b + 1][c] = a
        AI_educating()
    else:
        print("can't move")

#p_forward
def bp_p_forward(a, b, c):
    if b == 1:
        if eq(board[b + 2][c], 'NON'):
            board[b][c] = "NON"
            board[b + 2][c] = a
            AI_educating()
        else:
            print("can't move")
    else:
        print("can't move")

#eat_left
def bp_eat_left(a, b, c):
    if eq(board[b + 1][c - 1],'NON'):
        print("can't move")
    else:
        board[b][c] = "NON"
        board[b + 1][c-1] = a
        AI_educating()

#eat_right
def bp_eat_right(a, b, c):
    if eq(board[b + 1][c + 1],'NON'):
        print("can't move")
    else:
        board[b][c] = "NON"
        board[b + 1][c + 1] = a
        AI_educating()

#WR
#forward
def wr_h(a, b, c, d):
    tester = 0
    if b-d > 1:
        for i in range(d+1, b-1):
            if board[i][c] == 'NON':
                tester = tester
            else:tester = 1
    elif b-d < -1:
        for i in range(b+1, d-1):
            if board[i][c] == 'NON':
                tester = tester
            else:
                tester = 1

    if "W" in board[d][c]:
        tester = 1
    else:
        tester = tester

    if tester == 1:
        print("can't move")
    else:
        board[d][c] = a
        board[b][c] = "NON"
        AI_educating()

#side
def wr_v(a, b, c, d):#move, x, y, yp
    tester = 0
    if d-c > 1:
        for i in range(c+1,d-1):
            if board[b][i] == 'NON':
                tester = tester
            else:tester = 1
    elif d-c < -1:
        for i in range(d+1,c-1):
            if board[b][i] == 'NON':
                tester = tester
            else:
                tester = 1

    if "W" in board[b][d]:
        tester = 1
    else:
        tester = tester

    if tester == 1:
        print("can't move")
    else:
        board[b][d] = a
        board[b][c] = "NON"
        AI_educating()

#BR
#forward
def br_h(a, b, c, d):
    tester = 0
    if b-d > 1:
        for i in range(d+1, b-1):
            if board[i][c] == 'NON':
                tester = tester
            else:
                tester = 1
    elif b-d < -1:
        for i in range(b+1, d-1):
            if board[i][c] == 'NON':
                tester = tester
            else:
                tester = 1

    if "B" in board[d][c]:
        tester = 1
    else:
        tester = tester

    if tester == 1:
        print("can't move")
    else:
        board[d][c] = a
        board[b][c] = "NON"
        AI_educating()

#side
def br_v(a, b, c, d): #move, x, y, yp
    tester = 0
    if d-c > 1:
        for i in range(c+1,d-1):
            if board[b][i] == 'NON':
                tester = tester
            else:
                tester = 1
    elif d-c < -1:
        for i in range(d+1,c-1):
            if board[b][i] == 'NON':
                tester = tester
            else:
                tester = 1

    if "B" in board[b][d]:
        tester = 1
    else:
        tester = tester

    if tester == 1:
        print("can't move")
    else:
        board[b][d] = a
        board[b][c] = "NON"
        AI_educating()

#WB
def wb(a, b, c, d, e): #(move, x1, y1, xp, yp)
    tester = 0
    if abs(b-d) == abs(c-e):
        if b-d > 1:
            if c-e > 1:
                for i in range(abs(b-d)-1):
                    if board[b-i-1][c-i-1] == 'NON':
                        tester = tester
                    else:
                        tester = 1
            elif c-e < -1:
                for i in range(abs(b-d)-1):
                    if board[b-i-1][c+i+1] == 'NON':
                        tester = tester
                    else:
                        tester = 1
        elif b-d < -1:
            if c-e > 1:
                for i in range(abs(b-d)-1):
                    if board[b+i+1][c-i-1] == 'NON':
                        tester = tester
                    else:tester = 1
            elif c-e < -1:
                for i in range(abs(b-d)-1):
                    if board[b+i+1][c+i+1] == 'NON':
                        tester = tester
                    else:tester = 1

        if "W" in board[d][e]:
            tester = 1
        else:
            tester = tester

        if tester == 1:
            print("can't move")
        else:
            board[d][e] = a
            board[b][c] = "NON"
            AI_educating()
    else:
        print("can't move")

#BB
def bb(a, b, c, d, e): #(move, x1, y1, xp, yp)
    tester = 0
    if abs(b-d) == abs(c-e):
        if b-d > 1:
            if c-e > 1:
                for i in range(abs(b-d)-1):
                    if board[b-i-1][c-i-1] == 'NON':
                        tester = tester
                    else:
                        tester = 1
            elif c-e < -1:
                for i in range(abs(b-d)-1):
                    if board[b-i-1][c+i+1] == 'NON':
                        tester = tester
                    else:tester = 1
        elif b-d < -1:
            if c-e > 1:
                for i in range(abs(b-d)-1):
                    if board[b+i+1][c-i-1] == 'NON':
                        tester = tester
                    else:
                        tester = 1
            elif c-e < -1:
                for i in range(abs(b-d)-1):
                    if board[b+i+1][c+i+1] == 'NON':
                        tester = tester
                    else:
                        tester = 1

        if "B" in board[d][e]:
            tester = 1
        else:
            tester = tester

        if tester == 1:
            print("can't move")
        else:
            board[d][e] = a
            board[b][c] = "NON"
            AI_educating()
    else:
        print("can't move")

#WN
def wn(a, b, c, d, e): #(move, x1, y1, xp, yp)
    tester = 0
    if "W" in board[d][e]:
        tester = 1
    if b-d == 2:
        if c-e == 1 or e-c == 1:
            for i in range(2):
                if board[b-i-1][c] == 'NON' or "W" in board[b-i-1][c]:
                    tester = tester
                else:
                    tester = 1
        else:
            tester = 1
    elif b-d == -2:
        if c-e == 1 or e-c == 1:
            for i in range(2):
                if board[b+i+1][c] == 'NON' or "W" in board[b+i+1][c]:
                    tester = tester
                else:tester = 1
        else:
            tester = 1
    elif c-e == 2:
        if b-d == 1 or d-b == 1:
            for i in range(2):
                if board[b][c-i-1] == 'NON' or "W" in board[b][c-i-1]:
                    tester = tester
                else:
                    tester = 1
        else:
            tester = 1
    elif c-e == -2:
        if b-d == 1 or d-b == 1:
            for i in range(2):
                if board[b][c+i+1] == 'NON' or "W" in board[b][c+i+1]:
                    tester = tester
                else:
                    tester = 1
        else:
            tester = 1
    else:
        tester = 1

    if tester == 1:
        print("can't move")
    else:
        board[d][e] = a
        board[b][c] = "NON"
        AI_educating()

#BN
def bn(a, b, c, d, e): #(move, x1, y1, xp, yp)
    tester = 0
    if "B" in board[d][e]:
        tester = 1
    if b-d == 2:
        if c-e == 1 or e-c == 1:
            for i in range(2):
                if board[b-i-1][c] == 'NON' or "B" in board[b-i-1][c]:
                    tester = tester
                else:
                    tester = 1
        else:
            tester = 1
    elif b-d == -2:
        if c-e == 1 or e-c == 1:
            for i in range(2):
                if board[b+i+1][c] == 'NON' or "B" in board[b+i+1][c]:
                    tester = tester
                else:
                    tester = 1
        else:
            tester = 1
    elif c-e == 2:
        if b-d == 1 or d-b == 1:
            for i in range(2):
                if board[b][c-i-1] == 'NON' or "B" in board[b][c-i-1]:
                    tester = tester
                else:
                    tester = 1
        else:
            tester = 1
    elif c-e == -2:
        if b-d == 1 or d-b == 1:
            for i in range(2):
                if board[b][c+i+1] == 'NON' or "B" in board[b][c+i+1]:
                    tester = tester
                else:
                    tester = 1
        else:
            tester = 1
    else:tester = 1

    if tester == 1:
        print("can't move")
    else:
        board[d][e] = a
        board[b][c] = "NON"
        AI_educating()

#WK
def wk(a, b, c, d, e): #(move, x1, y1, xp, yp)
    tester = 0
    if b == d:
        if abs(e-c) == 1:
            if "W" in board[d][e]:
                tester = 1
            else:
                tester = tester
    elif c == e:
        if abs(d-b) == 1:
            if "W" in board[d][e]:
                tester = 1
            else:
                tester = tester
    else:
        if abs(e-c) == 1 and abs(d-b) == 1:
            if "W" in board[d][e]:
                tester = 1
            else:
                tester = tester

    if tester == 1:
        print("can't move")
    else:
        board[d][e] = a
        board[b][c] = "NON"
        AI_educating()

#BK
def bk(a, b, c, d, e): #(move, x1, y1, xp, yp)
    tester = 0
    if b == d:
        if abs(e-c) == 1:
            if "B" in board[d][e]:
                tester = 1
            else:
                tester = tester
    elif c == e:
        if abs(d-b) == 1:
            if "B" in board[d][e]:
                tester = 1
            else:tester = tester
    else:
        if abs(e-c) == 1 and abs(d-b) == 1:
            if "B" in board[d][e]:
                tester = 1
            else:
                tester = tester

    if tester == 1:
        print("can't move")
    else:
        board[d][e] = a
        board[b][c] = "NON"
        AI_educating()

#WQ
def wq(a, b, c, d, e):
    tester = 0
    if b == d or c == e:
        if b == d:
            if c < e:
                for i in range(c+1, e):
                    if board[b][i] != 'NON':
                        tester = 1
            else:
                for i in range(e+1, c):
                    if board[b][i] != 'NON':
                        tester = 1
        else:
            if b < d:
                for i in range(b+1, d):
                    if board[i][c] != 'NON':
                        tester = 1
            else:
                for i in range(d+1, b):
                    if board[i][c] != 'NON':
                        tester = 1
    elif abs(b-d) == abs(c-e):
        if b < d and c < e:
            for i in range(1, abs(b-d)):
                if board[b+i][c+i] != 'NON':
                    tester = 1
        elif b < d and c > e:
            for i in range(1, abs(b-d)):
                if board[b+i][c-i] != 'NON':
                    tester = 1
        elif b > d and c < e:
            for i in range(1, abs(b-d)):
                if board[b-i][c+i] != 'NON':
                    tester = 1
                elif b > d and c > e:
                    for i in range(1, abs(b-d)):
                        if board[b-i][c-i] != 'NON':
                            tester = 1
    else:
        tester = 1

    if "W" in board[d][e]:
        tester = 1

    if tester == 1:
        print("can't move")
    else:
        board[d][e] = a
        board[b][c] = "NON"
        AI_educating()

#BQ
def bq(a, b, c, d, e):
    tester = 0
    if b == d or c == e:
        if b == d:
            if c < e:
                for i in range(c+1, e):
                    if board[b][i] != 'NON':
                        tester = 1
            else:
                for i in range(e+1, c):
                    if board[b][i] != 'NON':
                        tester = 1
        else:
            if b < d:
                for i in range(b+1, d):
                    if board[i][c] != 'NON':
                        tester = 1
            else:
                for i in range(d+1, b):
                    if board[i][c] != 'NON':
                        tester = 1

    elif abs(b-d) == abs(c-e):
        if b < d and c < e:
            for i in range(1, abs(b-d)):
                if board[b+i][c+i] != 'NON':
                    tester = 1
        elif b < d and c > e:
            for i in range(1, abs(b-d)):
                if board[b+i][c-i] != 'NON':
                    tester = 1
        elif b > d and c < e:
            for i in range(1, abs(b-d)):
                if board[b-i][c+i] != 'NON':
                    tester = 1
        elif b > d and c > e:
            for i in range(1, abs(b-d)):
                if board[b-i][c-i] != 'NON':
                    tester = 1
    else:
        tester = 1

    if "B" in board[d][e]:
        tester = 1

    if tester == 1:
        print("can't move")
    else:
        board[d][e] = a
        board[b][c] = "NON"
        AI_educating()

#main loop
print("규칙 및 약속")
print("board : 열(세로) - 1~8, 행(가로) - 1~8")
print("Choice : 움질일 말 입력")
print("board : '열,행' 으로 입력(','로 구분)")

#Play With Human
while AI_count <= 1:
    check = searching_end("WK1")
    if check == 0:
        print("black win")
        AI_count = 2

        # board Setting
        board = [["NON" for j in range(8)] for i in range(8)]
        # black
        board[0][0] = "BR1"
        board[0][1] = "BN1"
        board[0][2] = "BB1"
        board[0][3] = "BK1"
        board[0][4] = "BQ1"
        board[0][5] = "BB2"
        board[0][6] = "BN2"
        board[0][7] = "BR2"
        for i in range(8):
            board[1][i] = "BP" + str(i + 1)

        # white
        board[7][0] = "WR1"
        board[7][1] = "WN1"
        board[7][2] = "WB1"
        board[7][3] = "WQ1"
        board[7][4] = "WK1"
        board[7][5] = "WB2"
        board[7][6] = "WN2"
        board[7][7] = "WR2"
        for i in range(8):
            board[6][i] = "WP" + str(i + 1)
        continue
    else:
        pass

    check = searching_end("BK1")
    if check == 0:
        print("white win")
        AI_count = 2

        # board Setting
        board = [["NON" for j in range(8)] for i in range(8)]
        # black
        board[0][0] = "BR1"
        board[0][1] = "BN1"
        board[0][2] = "BB1"
        board[0][3] = "BK1"
        board[0][4] = "BQ1"
        board[0][5] = "BB2"
        board[0][6] = "BN2"
        board[0][7] = "BR2"
        for i in range(8):
            board[1][i] = "BP" + str(i + 1)

        # white
        board[7][0] = "WR1"
        board[7][1] = "WN1"
        board[7][2] = "WB1"
        board[7][3] = "WQ1"
        board[7][4] = "WK1"
        board[7][5] = "WB2"
        board[7][6] = "WN2"
        board[7][7] = "WR2"
        for i in range(8):
            board[6][i] = "WP" + str(i + 1)
        continue
    else:
        pass

    # printing board
    f = 0
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j == 7:
                    print(Back.WHITE + Style.BRIGHT + Fore.BLACK + " " + str(board[i][j]) + " " + Style.RESET_ALL)
                elif j % 2 == 0:
                    print(Back.BLACK + Style.BRIGHT + Fore.WHITE + " " + str(board[i][j]), end=" " + Style.RESET_ALL)
                else:
                    print(Back.WHITE + Style.BRIGHT + Fore.BLACK + " " + str(board[i][j]), end=" " + Style.RESET_ALL)
            elif i % 2 != 0:
                if j == 7:
                    print(Back.BLACK + Style.BRIGHT + Fore.WHITE + " " + str(board[i][j]) + " " + Style.RESET_ALL)
                elif j % 2 != 0:
                    print(Back.BLACK + Style.BRIGHT + Fore.WHITE + " " + str(board[i][j]), end=" " + Style.RESET_ALL)
                else:
                    print(Back.WHITE + Style.BRIGHT + Fore.BLACK + " " + str(board[i][j]), end=" " + Style.RESET_ALL)

    #searching
    while True:
        move = input("Choice : ")
        x1, y1 = searching(move)

        if x1 != 100:
            break
        else:
            print("Try again")

    xp, yp = map(int, input("board : ").split(','))

    #p
    for i in range(8):
        # wp
        if move == "WP" + str((i+1)):
            xp -= 1
            yp -= 1

            if x1-1 == xp and y1 == yp:
                wp_forward(move, x1, y1)
            elif x1-2 == xp and y1 == yp:
                wp_p_forward(move, x1, y1)
            elif x1-1 == xp and y1-1 == yp:
                wp_eat_left(move, x1, y1)
            elif x1-1 == xp and y1+1 == yp:
                wp_eat_right(move, x1, y1)

        #bp
        if move == "BP" + str((i+1)):
            xp -= 1
            yp -= 1

            if x1+1 == xp and y1 == yp:
                bp_forward(move, x1, y1)
            elif x1+2 == xp and y1 == yp:
                bp_p_forward(move, x1, y1)
            elif x1+1 == xp and y1-1 == yp:
                bp_eat_left(move, x1, y1)
            elif x1+1 == xp and y1+1 == yp:
                bp_eat_right(move, x1, y1)

    #r
    for i in range(2):
        #wr
        if move == "WR" + str((i+1)):
            xp = xp-1
            yp = yp-1

            if yp == y1:
                wr_h(move, x1, y1, xp)
            elif xp == x1:
                wr_v(move, x1, y1, yp)

        #br
        elif move == "BR" + str((i+1)):
            xp = xp-1
            yp = yp-1

            if yp == y1:
                br_h(move, x1, y1, xp)
            elif xp == x1:
                br_v(move, x1, y1, yp)

    #b
    for i in range(2):
        #wb
        if move == "WB" + str((i+1)):
            xp = xp-1
            yp = yp-1
            wb(move, x1, y1, xp, yp)

        if move == "BB" + str((i+1)):
            xp = xp-1
            yp = yp-1
            bb(move, x1, y1, xp, yp)

    #n
    for i in range(2):
        #wn
        if move == "WN" + str((i+1)):
            xp = xp-1
            yp = yp-1
            wn(move, x1, y1, xp, yp)

        #bn
        if move == "BN" + str((i+1)):
            xp = xp-1
            yp = yp-1
            bn(move, x1, y1, xp, yp)

    #k
    if move == "WK1":
        xp = xp - 1
        yp = yp - 1
        wk(move, x1, y1, xp, yp)

    elif move == "BK1":
        xp = xp - 1
        yp = yp - 1
        bk(move, x1, y1, xp, yp)

    #Q
    if move == "WQ1":
        xp = xp - 1
        yp = yp - 1
        wq(move, x1, y1, xp, yp)

    if move == "BQ1":
        xp = xp - 1
        yp = yp - 1
        bq(move, x1, y1, xp, yp)

df = pd.DataFrame([[openning1.move, openning2.move, openning3.move, openning4.move, openning5.move, openning6.move, openning7.move, openning8.move, openning9.move, openning10.move],[openning1.place, openning2.place, openning3.place, openning4.place, openning5.place, openning6.place, openning7.place, openning8.place, openning9.place, openning10.place]],index = ["move", "place"],columns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
df.to_csv("C:/Users/dataframe/df1.csv")
