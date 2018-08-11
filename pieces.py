from gmpy2 import xmpz

'''
NOTES:
movePiece method inside each piece could be moved to the piece class because the code is identical, but maybe
not because of the getMoves function call which is different for every piece

'''



class GameBoard:
    def __init__(self):
        # set pieces
        self.board = [[0]*8 for i in range(8)]  # set board to 0's

        self.blackSquad = []
        self.whiteSquad = []

    def newGame(self):
        self.board[0:1] = [[1] * 8 for i in range(2)]  # 1 is a white piece
        self.board[6:7] = [[-1] * 8 for i in range(2)]  # -1 is a black piece
        for i in range(8):
            self.blackSquad.append(Pawn([i,6],'b'))
            self.whiteSquad.append(Pawn([i,1], 'w'))
        # set rooks
        self.blackSquad.append([Rook([0,7], 'b'), Rook([7,7], 'b')])
        self.whiteSquad.append([Rook([0,0], 'w'), Rook([7,0], 'w')])

        # set knights
        self.blackSquad.append([Knight([1,7], 'b'), Knight([6,7], 'b')])
        self.blackSquad.append([Knight([1, 0], 'w'), Knight([6, 0], 'w')])

        # set bishops
        self.blackSquad.append([Bishop([2,7], 'b'), Bishop([5,7], 'b')])
        self.whiteSquad.append([Bishop([2, 7], 'w'), Bishop([5, 7], 'w')])

        # set kings/queens


    def isOccupied(self, piece, guess):
        team = piece.team
        if not inBounds(guess):
            return False
        return (team == 'b' and self.board[guess[0],guess[1]] == -1) or (team == 'w' and self.board[guess[0], guess[1]] == 1)

    def inBounds(self, guess):
        return guess[0] in range(8) and guess[1] in range[8]

    # return all possible horizontal and vertical moves
    def crossMoves(self, piece):
        moves = []
        x = piece.pos[0]
        y = piece.pos[1]
        tempx = x+1
        tempy = y
        while self.inBounds([tempx, tempy]) and not self.isOccupied(piece, [tempx, tempy]):
            moves.append([tempx, tempy])
            tempx += 1
        tempx = x-1
        tempy = y
        while self.inBounds([tempx, tempy]) and not self.isOccupied(piece, [tempx, tempy]):
            moves.append([tempx, tempy])
            tempx -= 1
        tempx = x
        tempy = y+1
        while self.inBounds([tempx, tempy]) and not self.isOccupied(piece, [tempx, tempy]):
            moves.append([tempx, tempy])
            tempy += 1
        tempx = x
        tempy = y-1
        while self.inBounds([tempx, tempy]) and not self.isOccupied(piece, [tempx, tempy]):
            moves.append([tempx, tempy])
            tempy -= 1
        return moves

    # return all diagonal moves
    def diagonalMoves(self, piece):
        moves = []
        x = piece.pos[0]
        y = piece.pos[1]
        tempx = x+1
        tempy = y+1
        while self.inBounds([tempx, tempy]) and not self.isOccupied(piece, [tempx, tempy]):
            moves.append([tempx, tempy])
            tempx += 1
            tempy += 1
        tempx = x-1
        tempy = y-1
        while self.inBounds([tempx, tempy]) and not self.isOccupied(piece, [tempx, tempy]):
            moves.append([tempx, tempy])
            tempx -= 1
            tempy -= 1
        tempx = x+1
        tempy = y-1
        while self.inBounds([tempx, tempy]) and not self.isOccupied(piece, [tempx, tempy]):
            moves.append([tempx, tempy])
            tempx += 1
            tempy -= 1
        tempx = x-1
        tempy = y+1
        while self.inBounds([tempx, tempy]) and not self.isOccupied(piece, [tempx, tempy]):
            moves.append([tempx, tempy])
            tempx -= 1
            tempy += 1
        return moves

    def knightMoves(self, piece):
        moves = []
        x = piece.pos[0]
        y = piece.pos[1]
        potential_moves = [[x+2,y+1], [x+2,y-1], [x+1,y+2], [x+1,y-2], [x-1,y+2], [x-1,y-2], [x-2,y+1], [x-2,y-1]]
        for pair in potential_moves:
            if self.inBounds(pair) and not self.isOccupied(piece, pair):
                moves.append(pair)
        return moves

    def pawnMoves(self, piece):
        moves = []
        movement = 1
        if piece.team == 'b':
            movement = -1

        # check vertical
        x = piece.pos[0]
        y = piece.pos[1]
        if self.inBounds([x, y + movement]) and self.board[x, y + movement] == 0:
            moves.append([x, y + movement])
        if self.inBounds([x, y + 2 * movement]) and self.board[x, y + 2 * movement] == 0:
            moves.append([x, y + 2 * movement])
        if self.inBounds([x + 1, y + 2 * movement]) and self.board[x + 1, y + 2 * movement] == 0:
            moves.append([x + 1, y + 2 * movement])
        if self.inBounds([x - 1, y + 2 * movement]) and self.board[x - 1, y + 2 * movement] == 0:
            moves.append([x - 1, y + 2 * movement])
        return moves

    def makeMove(self, piece, move):
        curr_spot = piece.pos
        if piece.team == 'b'
            self.board[move[0], move[1]] = -1
        else:
            self.board[move[0], move[1]] = 1
        board[curr_spot[0],curr_spot[1]] = 0



class Piece:

    def __init__(self, pos, team, name):
        self.pos = pos
        self.team = team
        self.name = name
        self.moves = []



class King(Piece):

    def __init__(self, pos, team):
        Piece.__init__(self, pos, team, 'K')



class Pawn(Piece):

    def __init__(self, pos, team):
        Piece.__init__(self, pos, team, 'P')

    def getMoves(self, gameboard):
        self.moves = gameboard.pawnMoves(self)

    def movePiece(self, gameboard, move):
        self.getMoves(gameboard)
        if move in self.moves:
            gameboard.makeMove(self, move)


class Knight(Piece):

    def __init__(self, pos, team):
        Piece.__init__(self, pos, team, 'N')

    def getMoves(self, gameboard):
        self.moves = gameboard.knightMoves(self)

    def movePiece(self, gameboard, move):
        self.getMoves(gameboard)
        if move in self.moves:
            gameboard.makeMove(self, move)


class Bishop(Piece):

    def __init__(self, pos, team):
        Piece.__init__(self, pos, team, 'B')

    def getMoves(self, gameboard):
        self.moves = gameboard.diagonalMoves(self)

    def movePiece(self, gameboard, move):
        self.getMoves(gameboard)
        if move in self.moves:
            gameboard.makeMove(self, move)




class Queen(Piece):

    def __init__(self, pos, team):
        Piece.__init__(self, pos, team, 'Q')

    def getMoves(self, gameboard):
        self.moves = gameboard.crossMoves(self) + gameboard.diagonalMoves(self)

    def movePiece(self, gameboard, move):
        self.getMoves(gameboard)
        if move in self.moves:
            gameboard.makeMove(self, move)


class Rook(Piece):

    def __init__(self, pos, team):
        Piece.__init__(self, pos, team, 'R')

    def getMoves(self, gameboard):
        self.moves = gameboard.crossMoves(self)

    def movePiece(self, gameboard, move):
        self.getMoves(gameboard)
        if move in self.moves:
            gameboard.makeMove(self, move)















