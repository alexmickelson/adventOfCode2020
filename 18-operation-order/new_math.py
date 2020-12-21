

def read_expression(file_name):
    return [ e.replace('\n', '').replace('(', '( ').replace(')', ' )').split(' ') for e in open(file_name).readlines() ]

def evaluate_expression(expression):
    answer, remainding_expression = get_next_number(expression)
    while len(remainding_expression) != 0:
        if remainding_expression[0] == '+':
            next_number, remainding_expression = get_next_number(remainding_expression[1:])
            answer += next_number
        elif remainding_expression[0] == '*':
            next_number = evaluate_expression(remainding_expression[1:])
            remainding_expression = []
            # part 1
            # next_number, remainding_expression = get_next_number(remainding_expression[1:])
            answer *= next_number
    return answer

def get_closing_parenthesis_index(expression):
    open_parenthesis_count = 0
    for i, symbol in enumerate(expression):
        if symbol == '(':
            open_parenthesis_count += 1
        elif symbol == ')':
            open_parenthesis_count -= 1
        if(open_parenthesis_count == 0):
            return i

def get_next_number(expression):
    if expression[0] == '(' :
        end_parath_index = get_closing_parenthesis_index(expression)
        value = evaluate_expression(expression[1:end_parath_index])
        return value, expression[end_parath_index + 1: ]
    else:
        return int(expression[0]), expression[1:]

def sum_multiple_expressions(expressions):
    return sum([evaluate_expression(e) for e in expressions])

if __name__ == "__main__":
    expressions = read_expression('input.txt')
    sum = sum_multiple_expressions(expressions)
    print(f'Sum of homework is: {sum}')

