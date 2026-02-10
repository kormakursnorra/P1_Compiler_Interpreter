import sys


class LLexer():
    def __init__(self):
        pass

    def get_next_token(self, stdin: str):
        sys.stdin.read(stdin)