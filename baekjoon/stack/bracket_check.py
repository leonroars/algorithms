from stack_imp import Stack
import sys

def bracket_check(sentence):
    stack = Stack()
    for _ in sentence:
        if _ in '([{':
            stack.push(_)
        elif _ in ')}]':
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (_ == ')' and left != '(') or (_ == '}' and left != '{') or (_ == ']' and left != '['):
                    return False
    
    return stack.isEmpty()


s = sys.stdin.readline().rstrip()
a = bracket_check(s)
print(s, ": Checking Brackets _ ", a)
