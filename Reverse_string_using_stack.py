def createstack():
    stack = []
    return stack

def size(stack):
    return len(stack)

def isempty(stack):
    if size(stack) == 0:
        return True
    
def push(stack, item):
    stack.append(item)

def pop(stack):
    if isempty(stack):
        return
    return stack.pop()

def reverse(string):
    n = len(string)

    stack = createstack()

    for i in range(0, n, 1):
        push(stack, string[i])

    string = " "

    for i in range(0, n, 1):
        string = string + pop(stack)

    return string

string = "myschoolcode"
string = reverse(string)
print("Reversed string is:",string)
