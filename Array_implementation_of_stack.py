from sys import maxsize

def createstack():
    stack = []
    return stack

def isempty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack")

def pop(stack):
    if (isempty(stack)):
        return str(-maxsize -1)
    
    return stack.pop()

def peek(stack):
    if (isempty(stack)):
        return str(-maxsize -1)
    
    return stack[len(stack) - 1]

def size(stack):
    return len(stack)

stack = createstack()
push(stack, str(10))
push(stack, str(12))
push(stack, str(15))
print("Elements present in stack:",stack)
print(pop(stack), "popped from stack") 
print("Top element is:",peek(stack))
print("Is Empty?",isempty(stack))
print("Elements present in stack:", stack)
print("Stack Size:",size(stack))

