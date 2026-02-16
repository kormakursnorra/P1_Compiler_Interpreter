import sys
from ltoken import LToken


class LLexer():
    def __init__(self):
        self.current_char = None

    def skip_whitespace(self):
        while self.current_char and self.current_char in " \t\n":
            self.current_char = sys.stdin.read(1)

    def read_integer(self):
        result = ""
        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.current_char = sys.stdin.read(1)
        return result
    
    def read_indentifier(self):
        result = ""
        while self.current_char and self.current_char.isalpha():
            result += self.current_char
            self.current_char = sys.stdin.read(1)
        return result
    
    def get_next_token(self):
        if not self.current_char:
            self.current_char = sys.stdin.read(1)
        
        self.skip_whitespace()
        
        if self.current_char == "=":
            self.current_char = None
            return LToken("=", LToken.ASSIGN)
        
        elif self.current_char == ";":
            self.current_char = None
            return LToken(";", LToken.SEMICOL)
        
        elif self.current_char == "+":
            self.current_char = None
            return LToken("+", LToken.PLUS)

        elif self.current_char == "-":
            self.current_char = None
            return LToken("-", LToken.MINUS)

        elif self.current_char == "*":
            self.current_char = None
            return LToken("*", LToken.MULT)

        elif self.current_char == "(":
            self.current_char = None
            return LToken("(", LToken.LPAREN)

        elif self.current_char == ")":
            self.current_char = None
            return LToken(")", LToken.RPAREN)

        elif self.current_char.isdigit():
            lexeme = self.read_integer()
            return LToken(lexeme, LToken.INT)

        elif self.current_char.isalpha():
            lexeme = self.read_indentifier()

            if lexeme == "end":
                return LToken(lexeme, LToken.END)

            elif lexeme == "print":
                return LToken(lexeme, LToken.PRINT)

            else:
                return LToken(lexeme, LToken.ID)
            
        else:
            illegal_char = self.current_char
            self.current_char = None
            return LToken(illegal_char, LToken.ERROR)
