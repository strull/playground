#!/usr/bin/python3
import string

class Board:
    """A board is always quadratic. ;-)
    Biggest board is 26x26.
    """
    alphabet = list(string.ascii_lowercase)

    def __init__(self, boardsize):
        """Constructor"""
        self.board = []
        self.x = []
        for i in range(0, boardsize):
            tempboard = []
            for j in range(0, boardsize):
                if i & 1 and j & 1 or not i & 1 and not j & 1:
                    tempboard += ['X']
                else:
                    tempboard += [' ']
            self.board += [tempboard]
            self.x += Board.alphabet[i]
        self.boardsize = boardsize

    def print(self):
        """Prints the board."""
        for i in range(self.boardsize - 1, -1, -1):
            print(str(i + 1) + "\t", end='')
            print(*self.board[i], sep='')
        print("\t", end='')
        print(*self.x, sep='')

    def put_piece(self, x, y):
        """Puts a chesspiece on a board.
        :param x:
        :param y:
        """
        self.board[y][x] = "P"

    def horizontal_squares(self, x, y):
        """returns a list of horizontal squares/coordinates P can visit except its own position.
        :param x: x coordinate where the piece is put, beginning at 0
        :param y: y coordinate where the piece is put, beginning at 0
        :return: a list with lists of horizontal coordinates the piece can visit except its own position
        """
        horizontalSquares = []
        for i in range(0, self.boardsize):
            horizontalSquares.append([i, y])
        del horizontalSquares[x]
        print("\nhorizontal squares/coordinates P can visit:\n" + str(horizontalSquares))
        return horizontalSquares

    def vertical_squares(self, x, y):
        """returns a list of vertical squares/coordinates P can visit except its own position.
        :param x: x coordinate where the piece is put, beginning at 0
        :param y: y coordinate where the piece is put, beginning at 0
        :return: a list with lists of vertical coordinates the piece can visit except its own position
        """
        verticalSquares = []
        for i in range(0, self.boardsize):
            verticalSquares.append([x, i])
        del verticalSquares[y]
        print("\nvertical squares/coordinates P can visit:\n" + str(verticalSquares))
        return verticalSquares

    def diagonal_squares(self, x, y):
        """returns a list of diagonal squares/coordinates P can visit except its own position.
        :param x: x coordinate where the piece is put, beginning at 0
        :param y: y coordinate where the piece is put, beginning at 0
        :return: a list with lists of diagonal coordinates the piece can visit except its own position
        """
        xtemp = x
        ytemp = y
        diagonalSquaresRightUp = []
        while xtemp < self.boardsize - 1 and ytemp < self.boardsize -1:
            xtemp += 1
            ytemp += 1
            diagonalSquaresRightUp.append([xtemp, ytemp])
        print("\ndiagonal squares/coordinates RIGHT UP P can visit:\n" + str(diagonalSquaresRightUp))

        xtemp = x
        ytemp = y
        diagonalSquaresLeftDown = []
        while xtemp > 0 and ytemp > 0:
            xtemp -= 1
            ytemp -= 1
            diagonalSquaresLeftDown.append([xtemp, ytemp])
        print("\ndiagonal squares/coordinates LEFT DOWN P can visit:\n" + str(diagonalSquaresLeftDown))

        xtemp = x
        ytemp = y
        diagonalSquaresLeftUp = []
        while xtemp > 0 and ytemp < self.boardsize - 1:
            xtemp -= 1
            ytemp += 1
            diagonalSquaresLeftUp.append([xtemp, ytemp])
        print("\ndiagonal squares/coordinates LEFT UP P can visit:\n" + str(diagonalSquaresLeftUp))

        xtemp = x
        ytemp = y
        diagonalSquaresRightDown = []
        while (xtemp >= 0 and xtemp < self.boardsize - 1)  and ytemp > 0:
            xtemp += 1
            ytemp -= 1
            diagonalSquaresRightDown.append([xtemp, ytemp])
        print("\ndiagonal squares/coordinates RIGHT DOWN P can visit:\n" + str(diagonalSquaresRightDown))

        diagonalSquares = diagonalSquaresRightUp + diagonalSquaresLeftDown + diagonalSquaresLeftUp + diagonalSquaresRightDown
        print("\ndiagonal squares/coordinates P can visit:\n" + str(diagonalSquares))
