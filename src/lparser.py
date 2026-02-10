from ltoken import LToken
from llexer import LLexer
import sys


class LParser():
    def __init__(self):
        self.token = LToken()
        self.lexer = LLexer()

    def error(self):
        pass

    def parse(self):
        self.next_token()
        self.statements()
        print('\n')  # Make sure it ends with newline

    def next_token(self):
        self.curr_token = self.lexer.get_next_token()
        if self.curr_token.token_code == LToken.ERROR:
            self.error()

    def statements(self):
        pass
