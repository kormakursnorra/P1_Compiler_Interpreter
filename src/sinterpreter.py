import sys

class SInterpreter:
    def __init__(self):
        self.stack = []
        self.variables = {} 

    def push(self, operand):
        if operand.isdigit():
            self.stack.append(int(operand)) 
        else:
            self.stack.append(operand)

    def get_value(self, item):
        if isinstance(item, int):
            return item
        return self.variables.get(item, 0)
    
    def add(self):
        if len(self.stack) < 2:
            print("Error for operator: ADD")
            sys.exit()
        
        val1 = self.get_value(self.stack.pop())
        val2 = self.get_value(self.stack.pop())
        self.stack.append(val1 + val2)

    def sub(self):
        if len(self.stack) < 2:
            print("Error for operator: SUB")
            sys.exit()

        val1 = self.get_value(self.stack.pop())
        val2 = self.get_value(self.stack.pop())
        self.stack.append(val2 - val1)

    def mult(self):
        if len(self.stack) < 2:
            print("Error for operator: MULT")
            sys.exit()

        val1 = self.get_value(self.stack.pop())
        val2 = self.get_value(self.stack.pop())
        self.stack.append(val1 * val2)

    def assign(self):
        if len(self.stack) < 2:
            print("Error for operator: ASSIGN")
            sys.exit()
        
        value = self.get_value(self.stack.pop())
        var_name = self.stack.pop()
        self.variables[var_name] = value

    def print_top(self):
        if len(self.stack) < 1:
            print("Error operator: PRINT")
            sys.exit()
        
        value = self.get_value(self.stack.pop())
        print(value)
    
    def cycle(self):
        for line in sys.stdin:
            operation = line.strip().split()

            if not operation:
                continue
            
            command = operation[0]

            if command == "PUSH":
                self.push(operation[1])
            
            elif command == "ADD":
                self.add()

            elif command == "SUB":
                self.sub()
            
            elif command == "MULT":
                self.mult()
            
            elif command == "ASSIGN":
                self.assign()
            
            elif command == "PRINT":
                self.print_top()
            
            else:
                print(f"Error for operator: {command}")
                sys.exit()

if __name__ == "__main__":
    interpreter = SInterpreter()
    interpreter.cycle()
