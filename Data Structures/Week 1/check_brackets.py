# python3

import sys


class Bracket:

    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    error_index = 0
    for i, next in enumerate(text, start=1):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if opening_brackets_stack:
                if not opening_brackets_stack.pop().Match(next):
                    error_index = i
                    break
            else:
                error_index = i
                break

    # Printing answer, write your code here
    if error_index != 0:
        print(error_index)
    elif opening_brackets_stack:
        print(opening_brackets_stack.pop().position)
    else:
        print("Success")
