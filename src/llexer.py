import sys
from ltoken import LToken


class LLexer():
    def __init__(self):
        self.current_char = None
        self.read_next_char()

    def read_next_char(self):
        self.current_char = sys.stdin.read(1)

    def skip_whitespace(self):
        while self.current_char and self.current_char in ' \t\n\r':
            self.read_next_char()

    def read_integer(self):
        result = ''
        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.read_next_char()
        return result
    
    def read_indentifier(self):
        result = ''
        while self.current_char and self.current_char.isalpha():
            result += self.current_char
            self.read_next_char()
        return result
    
    def get_next_token(self):

        self.skip_whitespace()

        if not self.current_char:
            return LToken('', LToken.END)
        
        if self.current_char == '=':
            self.read_next_char()
            return LToken('=', LToken.ASSIGN)
        
        if self.current_char == ';':
            self.read_next_char()
            return LToken(';', LToken.SEMICOL)
        
        if self.current_char == '+':
            self.read_next_char()
            return LToken('+', LToken.PLUS)

        if self.current_char == '-':
            self.read_next_char()
            return LToken('-', LToken.MINUS)

        if self.current_char == '*':
            self.read_next_char()
            return LToken('*', LToken.MULT)

        if self.current_char == '(':
            self.read_next_char()
            return LToken('(', LToken.LPAREN)

        if self.current_char == ')':
            self.read_next_char()
            return LToken(')', LToken.RPAREN)

        if self.current_char.isdigit():
            lexeme = self.read_integer()
            return LToken(lexeme, LToken.INT)

        if self.current_char.isalpha():
            lexeme = self.read_indentifier()

            if lexeme == 'end':
                return LToken(lexeme, LToken.END)

            elif lexeme == 'print':
                return LToken(lexeme, LToken.PRINT)

            else:
                return LToken(lexeme, LToken.ID)
            
        illegal_char = self.current_char
        self.read_next_char()
        return LToken(illegal_char, LToken.ERROR)
