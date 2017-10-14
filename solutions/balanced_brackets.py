""" Stacks: Balanced Brackets """

MIRROR_PARENTHESIS = {
    ']': '[',
    '}': '{',
    ')': '('
}

def is_matched(expression):
    """ check if brackets are complete """

    expression_stack = list()

    for character in expression:
        if not expression_stack or \
                expression_stack[-1] != MIRROR_PARENTHESIS.get(character):
            expression_stack.append(character)
        else:
            expression_stack.pop()

    return not expression_stack

def main():
    """ Main function """
    number_of_expressions = int(input().strip())
    for _ in range(number_of_expressions):
        expression = input().strip()
        answer = "YES" if is_matched(expression) else "NO"
        print(answer)

if __name__ == '__main__':
    main()
