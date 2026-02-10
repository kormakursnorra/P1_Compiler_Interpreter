class LToken():
    def __init__(
            self, ID, ASSIGN, SEMICOL, INT, PLUS, MINUS,
            MULT, LPAREN, RPAREN, PRINT, END, ERROR
            ):
        self.ID = ID
        self.ASSIGN = ASSIGN
        self.SEMICOL = SEMICOL
        self.INT = INT
        self.PLUS = PLUS
        self.MINUS = MINUS
        self.MULT = MULT
        self.LPAREN = LPAREN
        self.RPAREN = RPAREN
        self.PRINT = PRINT
        self.END = END
        self.ERROR = ERROR

