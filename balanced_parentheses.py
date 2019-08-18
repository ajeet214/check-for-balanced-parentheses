open_parentheses_list = ["[", "{", "("]
close_parentheses_list = ["]", "}", ")"]


def check_balanced_parentheses(exp):
    stack = []
    for i in exp:
        if i in open_parentheses_list:
            stack.append(i)
        elif i in close_parentheses_list:
            pos = close_parentheses_list.index(i)
            if (len(stack) > 0) and (open_parentheses_list[pos] == stack[len(stack)-1]):
                stack.pop()
            else:
                return "Unbalanced"

    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


if __name__ == '__main__':
    expression = "{(a)}[(x)](){{{()}}}"
    print(check_balanced_parentheses(expression))
