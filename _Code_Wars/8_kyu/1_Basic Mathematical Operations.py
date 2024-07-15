def basic_op(operator, value1, value2):

    if operator == '+':
        plus = value1 + value2
        return plus
    if operator == '-':
        minus = value1 - value2
        return minus
    if operator == '*':
        mult = value1 * value2
        return mult
    if operator == '/':
        div = value1 / value2
        return div

print(basic_op('+', 5 , 9))


def basic_op(operator, value1, value2):
    match operator:
        case '+':
            return value1 + value2
        case '-':
            return value1 - value2
        case '*':
            return value1 * value2
        case '/':
            return value1 / value2


def basic_op(operator, value1, value2):
    ops = {'+': lambda a, b: a + b,
           '-': lambda a, b: a - b,
           '*': lambda a, b: a * b,
           '/': lambda a, b: a / b}
    return ops[operator](value1, value2)


def basic_op(operator, value1, value2):
    op = {
        '+' : (value1 + value2),
        '-' : (value1 - value2),
        '*' : (value1 * value2),
        '/' : (value1 / value2),
    }

    return op[operator]