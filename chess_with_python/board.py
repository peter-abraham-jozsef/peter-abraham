# board.py
class ChessBoard:
    def __init__(self):
        # Initialize an 8x8 board with None (empty squares)
        self.board = [[None for _ in range(8)] for _ in range(8)]
        
    def setup_initial_pieces(self):
        # Place the initial pieces on the board
        # White pieces
        self.board[0][0] = "Rook"
        self.board[0][1] = "Knight"
        self.board[0][2] = "Bishop"
        self.board[0][3] = "Queen"
        self.board[0][4] = "King"
        self.board[0][5] = "Bishop"
        self.board[0][6] = "Knight"
        self.board[0][7] = "Rook"
        for i in range(8):
            self.board[1][i] = "Pawn"

        # Black pieces
        self.board[7][0] = "Rook"
        self.board[7][1] = "Knight"
        self.board[7][2] = "Bishop"
        self.board[7][3] = "Queen"
        self.board[7][4] = "King"
        self.board[7][5] = "Bishop"
        self.board[7][6] = "Knight"
        self.board[7][7] = "Rook"
        for i in range(8):
            self.board[6][i] = "Pawn"
        pass
        
    def get_piece(self, row, col):
        # Return the piece at a specific position
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        return None
        
    def place_piece(self, piece, row, col):
        """Place a piece at the specified grid position"""
        # Calculate the center position of the square in pixels
        x = col * self.square_size + (self.square_size // 2)
        y = row * self.square_size + (self.square_size // 2)
        
        # Create the image on the canvas
        self.canvas.create_image(x, y, image=self.piece_image)
        if 0 <= row < 8 and 0 <= col < 8:
            self.board[row][col] = piece