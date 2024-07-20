def isoperator(c):
    return (not c.isalpha()) and (not c.isdigit())

def  getPriority(c):
    if c == "-" or c == "+":
        return 1
    elif c == "*" or c == "/":
        return 2
    elif c == "^":
        return 3
    return 0

def infixtopostfix(infix):
    infix = "(" + infix + ")"
    l = len(infix)
    char_stack = []
    output = ""

    for i in range(l):
        if infix[i].isalpha() or infix[i].isdigit():
            output = output + infix[i]

        elif infix[i] == '(':
            char_stack.append(infix[i])

        elif infix[i] == ')':
            while char_stack[-1] != '(':
                output += char_stack.pop()
            char_stack.pop()

        else:
            if isoperator(char_stack[-1]):
                if infix[i] == '^':
                    while getPriority(infix[i]) <= getPriority(char_stack[-1]):
                        output += char_stack.pop()
                else:
                    while getPriority(infix[i]) < getPriority(char_stack[-1]):
                        output += char_stack.pop()
                char_stack.append(infix[i])

    while len(char_stack) != 0:
        output += char_stack.pop()
    return output

def infixtoprefix(infix):
    l = len(infix)
 
    infix = infix[::-1]
 
    for i in range(l):
        if infix[i] == '(':
            infix[i] = ')'
        elif infix[i] == ')':
            infix[i] = '('
 
    prefix = infixtopostfix(infix)
    prefix = prefix[::-1]
 
    return prefix

if __name__ == '__main__':
    s = "x+y*z/w+u"
     
    print(infixtoprefix(s))
    #print(infixtopostfix(s))