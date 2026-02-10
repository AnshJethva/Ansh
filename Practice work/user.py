
def findCube(n):
    return n * n * n

def largest(a, b, c):
    return max(a, b, c)

def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    
def reverse_string(s):
    return s[::-1]

def remove_duplicates(lst):
    return list(set(lst))

def remove_spaces(s):
    return s.replace(" ", "")

def swap(a, b):
    return b, a

def replace_word(s, old, new):
    return s.replace(old, new)

















def bye(name):
    print(f"Goodbye, Mr/Mrs {name}. Have a nice day!")