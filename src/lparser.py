import sys
from ltoken import LToken
from llexer import LLexer


class LParser():
    def __init__(self, lexer):
        self.lexer: LLexer = lexer
        self.curr_token: LToken  = None

    def error(self):
        print("Syntax error")
        sys.exit(1)

    def parse(self):
        self.next_token()
        self.statements()
        print('\n')  # Make sure it ends with newline

    def next_token(self):
        self.curr_token = self.lexer.get_next_token()
        if self.curr_token.token_code == LToken.ERROR:
            self.error()

    def statements(self):
        if self.curr_token.token_code == LToken.END:
            return
        
        else:
            self.statement()

            if self.curr_token.token_code != LToken.SEMICOL:
                self.error()
        
            self.next_token()
            self.statements()

    
    def statement(self):
        if self.curr_token.token_code == LToken.ID:
            id_lexeme = self.curr_token.lexeme
            self.next_token()

            if self.curr_token.token_code == LToken.ASSIGN:
                print(f"PUSH {id_lexeme}")
                self.next_token()
                self.expr()
                print("ASSIGN")
            else:
                self.error()
            
        elif self.curr_token.token_code == LToken.PRINT:
            self.next_token()

            if self.curr_token.token_code != LToken.ID:
                self.error()
            
            print(f"PUSH {self.curr_token.lexeme}")
            print("PRINT")
            self.next_token()
        
        else:
            self.error()
    
    def expr(self):
        self.term()

        if self.curr_token.token_code == LToken.PLUS:
            self.next_token()
            self.expr()
            print("ADD")
        
        elif self.curr_token.token_code == LToken.MINUS:
            self.next_token()
            self.expr()
            print("SUB")

    def term(self):
        self.factor()

        if self.curr_token.token_code == LToken.MULT:
            self.next_token()
            self.term()
            print("MULT")
    
    def factor(self):
        if self.curr_token.token_code == LToken.INT:
            print(f"PUSH {self.curr_token.lexeme}")
            self.next_token()
        
        elif self.curr_token.token_code == LToken.ID:
            print(f"PUSH {self.curr_token.lexeme}")
            self.next_token()
        
        elif self.curr_token.token_code == LToken.LPAREN:
            self.next_token()
            self.expr()

            if self.curr_token.token_code != LToken.RPAREN:
                self.error()
            
            self.next_token()
        
        else:
            self.error()