from stack_imp import Stack

'''
I'm going to define three functions:
    1) precedence() : Return priority of given argument(operator) in operation as integer type value. Arg => str / Return => int. If it's not operator, return False.
    2) pair() : Returns boolean result for whether brackets given as argument is pair with each other.
    3) to_postfix() : Convert infix notated expression to postfix notated one. Arg => str(infix expression) / Return => str
    4) eval_postfix() : Calculate postfix notated expression. Arg => str(expression) / Return => int

* Caution!
    I premise correctly balanced brackets for input operation expressions in this implementation.
    This means, as brackets in input expressions are correctly balanced, I won't consider for checking if they're wrong or their precedence.

'''
# 1. Defining precedence() for setting up opeerators order.
def precedence(term):
    if term in '*/':
        return 1
    elif term in '+-':
        return 0
    else:
        return False

# 2. Defininig to_postfix() for converting given infix notated expression to postfix notation.
def pair(br1, br2):
    if (br1 in '[]' and br2 in '[]') or (br1 in '{}' and br2 in '{}') or (br1 in '()' and br2 in '()'):
        return True
    else:
        False

def to_postfix(expression):
    #global stack
    stack = Stack()
    result = ""
    for _ in expression:
        if _ in '[{(':
            stack.push(_)
        elif _ in '+-*/':
             last = str(stack.peek())
             if precedence(last) <= precedence(_):
                 stack.push(_)
             else:
                 result += str(stack.pop())
                 stack.push(_)
        elif _ in ']})':
            while not stack.isEmpty():
                popped = stack.pop()
                if popped in '+-*/':
                    result += str(popped)
                    continue
                elif pair(popped, _) == True:
                    if stack.peek() in '+-*/':
                        result += stack.pop()
                    else:
                        break
                else:
                    continue
                    
        else:
            result += str(_)
    
    while not stack.isEmpty():
        result += str(stack.pop())
    
    return result

# 3. Defining eval_postfix() for postfix expression evaluation.
def eval_postfix(expression):