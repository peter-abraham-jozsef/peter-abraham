from PIL import Image, ImageTk
import tkinter as tk
from board import ChessBoard

class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game")
        self.board = ChessBoard()
        
        
        self.square_size = 60
        self.board_size = self.square_size * 8
           
        # Load a single piece image as an example
        image = Image.open("chess_pieces/white_knight.png")  # Your image path
        image = image.resize((self.square_size, self.square_size))  # Resize to fit square
        self.piece_image = ImageTk.PhotoImage(image)  # Convert for Tkinter
        
        
        self.canvas = tk.Canvas(root, width=self.board_size, height=self.board_size)
        self.canvas.pack()
        
        
        self.draw_board()
        
        
        
    def draw_board(self):
        for row in range(8):
            for col in range(8):
                # Calculate position
                x1 = col * self.square_size
                y1 = row * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                
                # Set color (alternating pattern)
                color = "#FFFFFF" if (row + col) % 2 == 0 else "#5D8AA8"
                
                # Draw square
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
    
    

root = tk.Tk()
game = ChessGame(root)
root.mainloop()