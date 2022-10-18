from stack import Stack

def isBalanced(stack) -> str:
    opening_stack = Stack('')
    for el in stack:
        if el in '([{':
            opening_stack.push(el)
        else:
            if opening_stack.isEmpty():
                return 'Несбалансированно'
            if el == ')' and opening_stack.peek() == '(':
                opening_stack.pop()
            if el == ']' and opening_stack.peek() == '[':
                opening_stack.pop()            
            if el == '}' and opening_stack.peek() == '{':
                opening_stack.pop()
    if opening_stack.size() == 0 and stack.size() % 2 == 0:
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'

if __name__ == '__main__':

    stack1, stack2, stack3 = Stack('(((([{}]))))'), Stack('[([])((([[[]]])))]{()}'), Stack('{{[()]}}')
    print(isBalanced(stack1), isBalanced(stack2), isBalanced(stack3))
    stack1, stack2, stack3 = Stack('}{}'), Stack('{{[(])]}}'), Stack('[[{())}]')
    print(isBalanced(stack1), isBalanced(stack2), isBalanced(stack3))