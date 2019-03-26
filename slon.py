class Bishop(object):
 
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
 
 
    def set_position(self, row, col):
        self.row = row
        self.col = col
 
    def char(self):
        return 'B'
 
    def get_color(self):
        return self.color
 
    def can_move(self, row, col):
        if self.col == col and self.row == row:
            return False
        if self.col == row and self.row == col:
            return True
"""
WHITE=1
BLACK=2
        
row0 = 0
col0 = 2
bishop = Bishop(row0, col0, WHITE)
        
print('white' if bishop.get_color() == WHITE else 'black')
for row in range(7, -1, -1):
    for col in range(8):
        if row == row0 and col == col0:
            print(bishop.char(), end='')
        elif bishop.can_move(row, col):
            print('x', end='')
        else:
            print('-', end='')
    print()
"""