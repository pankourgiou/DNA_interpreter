#So let's try to make a DNA/python based programming language--->We use letters as commands so we give command A:Add 1 variable to 'x' where A is Adenine.
class DNAInterpreter:
    def __init__(self):
        self.x = 0  # Initialize variable x

    def interpret(self, code):
        for command in code:
            if command == 'A':
                self.x += 1
            elif command == 'C':
                # Compare x to a specific value (for simplicity, let's say 5)
                if self.x == 5:
                    print("Equal")
                else:
                    print("Not Equal")
            elif command == 'T':
                # Transfer a value (for simplicity, let's say we set it to 10)
                self.x = 10
            elif command == 'G':
                print(f"x = {self.x}")
            else:
                print(f"Unknown command: {command}")

# Example usage
if __name__ == "__main__":
    interpreter = DNAInterpreter()
    code = "ATAATA"  # Example program
    interpreter.interpret(code)
class DNAInterpreter:
    def __init__(self):
        self.x = 0  # Initialize variable x

    def interpret(self, code):
        for command in code:
            if command == 'A':
                self.x += 1
            elif command == 'C':
                # Compare x to a specific value (for simplicity, let's say 5)
                if self.x == 5:
                    print("Equal")
                else:
                    print("Not Equal")
            elif command == 'T':
                # Transfer a value (for simplicity, let's say we set it to 10)
                self.x = 10
            elif command == 'G':
                print(f"x = {self.x}")
            else:
                print(f"Unknown command: {command}")

# Example usage
if __name__ == "__main__":
    interpreter = DNAInterpreter()
    code = "TCTTCTTCTATA"  # Example program
    interpreter.interpret(code)
