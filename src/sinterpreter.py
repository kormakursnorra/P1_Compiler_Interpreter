import sys

class SInterpreter:
    def __init__(self):
        self.stack = []
        self.variables = {} 

    def push(self, operand):
        if operand.lstrip('-').isdigit():
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
            sys.exit(1)
        
        val2 = self.get_value(self.stack.pop())
        val1 = self.get_value(self.stack.pop())
        self.stack.append(val1 + val2)

    def sub(self):
        if len(self.stack) < 2:
            print("Error for operator: SUB")
            sys.exit(1)

        val1 = self.get_value(self.stack.pop())
        val2 = self.get_value(self.stack.pop())
        self.stack.append(val2 - val1)

    def mult(self):
        if len(self.stack) < 2:
            print("Error for operator: MULT")
            sys.exit(1)

        val2 = self.get_value(self.stack.pop())
        val1 = self.get_value(self.stack.pop())
        self.stack.append(val1 * val2)

    def assign(self):
        if len(self.stack) < 2:
            print("Error for operator: ASSIGN")
            sys.exit(1)
        
        value = self.get_value(self.stack.pop())
        var_name = self.stack.pop()

        if not isinstance(var_name, str):
            print("Error for operator: ASSIGN")
            sys.exit(1)
        
        self.variables[var_name] = value

    def print_top(self):
        if len(self.stack) < 1:
            print("Error operator: PRINT")
            sys.exit(1)
        
        value = self.get_value(self.stack[-1])
        print(value)
    
    def cycle(self):
        for line in sys.stdin:
            line = line.strip()

            if not line:
                continue
            
            parts = line.split(maxsplit=1)
            command = parts[0]

            if command == "PUSH":
                if len(parts) < 2:
                    print(f"Error for operator: PUSH")
                    sys.exit(1)
                operand = parts[1]
                self.push(operand)
            
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
                sys.exit(1)

if __name__ == "__main__":
    interpreter = SInterpreter()
    interpreter.cycle()
