from stack import Stack
from node import Node


def is_balanced(brackets: str) -> str:
    '''Проверяет количество скобок в строке'''
    stack = Stack()
    brackets_dict = {')': '(', ']': '[', '}': '{'}
    
    for char in brackets:
        if char in '([{':
            stack.push(Node(char))
        else:
            if stack.is_empty():
                return "Несбалансированно"
            top = stack.pop()
            if brackets_dict[char] != top:
                return "Несбалансированно"
    
    if stack.is_empty():
        return "Сбалансированно"
    return "Несбалансированно"

print(is_balanced("(((([{}]))))"))
print(is_balanced("[([])((([[[]]])))]{()}"))
print(is_balanced("{{[()]}}"))

print(is_balanced("}{}"))
print(is_balanced("{{[(])]}}"))
print(is_balanced("[[{())}]"))