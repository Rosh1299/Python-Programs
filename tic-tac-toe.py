class TicTacToe:
    def __init__(self):
        # creating game
        self.sign_list = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append("_")
            self.sign_list.append(row)

    # displaying game
    def show(self):
        print("="*15)
        for i in range(len(self.sign_list)):
            print("|", end=" ")
            for j in self.sign_list[i]:
                print(j, "|", end=" ")
            print()
            print("|___|___|___|")

    # function to check row
    def check_row(self, list1):
        n = len(list1)
        i = 0
        while i < n:
            j = 0
            if list1[i][j] == list1[i][j+1] == list1[i][j+2] != "_":
                return True
            i += 1

    # function to check column
    def check_col(self, list1):
        n = len(list1)
        i = 0
        while i < n:
            j = 0
            if list1[j][i] == list1[j+1][i] == list1[j+2][i] != "_":
                return True
            i += 1
        else:
            return False

    # function to check diagonal
    def check_diagonal(self, list1):
        if list1[0][0] == list1[1][1] == list1[2][2] != "_":
            return True
        elif list1[0][2] == list1[1][1] == list1[2][0] != "_":
            return True
        else:
            return False

    # checking game filled with marks or not
    def is_board_filled(self):
        for row in self.sign_list:
            for sym in row:
                if sym == "_":
                    return False
        else:
            return True

    # function to check winner conditions
    def winner(self):
        row = self.check_row(self.sign_list)
        col = self.check_col(self.sign_list)
        diagonal = self.check_diagonal(self.sign_list)
        if row:
            return True
        elif col:
            return True
        elif diagonal:
            return True
        else:
            return False

    # function to place the mark for given row and column
    def place_mark(self, row, col, count):
        if self.is_board_filled:
            if count % 2 == 0:
                self.sign_list[row-1][col-1] = "X"
                self.show()
            else:
                self.sign_list[row-1][col-1] = '0'
                self.show()

    # main function to start the game
    def start(self):
        cnt = 0
        while cnt < 9:
            try:
                player = (cnt % 2)+1
                win = self.winner()
                if not win:
                    print("="*15)
                    print(f"Player-{player} Turn")
                    row, col = int(input("Enter row:")), int(
                        input("Enter column:"))
                    if self.sign_list[row-1][col-1] == "_":
                        self.place_mark(row, col, cnt)
                        cnt += 1
                    else:
                        print("Place is occupied by ",
                              self.sign_list[row-1][col-1])
                else:
                    print("="*15)
                    print("Game over")
                    player = cnt % 2
                    if player == 1:
                        print("Player-1 won.")
                    else:
                        print("player-2 won.")
                    break

            except ValueError as e:
                print("You entered wrong input,Please enter valid number.")

        else:
            print("Match Draw.")


print("~x~x~x~x~Tic-Tac-Toe~x~x~x~x~")
print("Player-1: X\nPlayer-2: O")
print("~~Let's Start The Game~~")
game = TicTacToe()
game.show()
game.start()
