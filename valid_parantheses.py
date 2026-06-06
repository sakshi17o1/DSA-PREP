def isvalid(s):
    stack=[]
    brack_map={ '(': ')', '{': '}', '[': ']' }
    for brack in s:
        if brack in brack_map:
            stack.append(brack)
        else:
            if (not stack or brack_map[stack.pop()] != brack):
                return False
    return not stack
print(isvalid("{[()]}"))
