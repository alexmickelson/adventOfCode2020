import new_math

def test_read_expression():
    expected_expression = ['1', '+', '(', '2', '*', '3', ')', '+', '(', '4', '*', '(', '5', '+', '6', ')', ')']
    actual_expression = new_math.read_expression('example.txt')
    assert actual_expression[0] == expected_expression

def test_get_next_number():
    expression = '1 + ( 2 * 3 ) + ( 4 * ( 5 + 6 ) )'.split(' ')
    expected_next_number = 1
    actual_next_number, _expression = new_math.get_next_number(expression)
    assert actual_next_number == expected_next_number

def test_get_next_number_parenthesis():
    expression = '( 2 * 3 ) + ( 4 * ( 5 + 6 ) )'.split(' ')
    expected_next_number = 6
    actual_next_number, _expression = new_math.get_next_number(expression)
    assert actual_next_number == expected_next_number

def test_evaluate_expression():
    expression = new_math.read_expression('example.txt')
    expected_answer = 51
    actual_answer = new_math.evaluate_expression(expression[0])
    assert actual_answer == expected_answer

def test_sum_multiple_expressions():
    expressions = new_math.read_expression('example2.txt')
    expected_sum = 693942
    actual_sum = new_math.sum_multiple_expressions(expressions)
    assert actual_sum == expected_sum

def test_new_precidence_rules():
    expressions = new_math.read_expression('example.txt')
    expected_answer = 231
    actual_answer = new_math.evaluate_expression(expressions[1])
    assert actual_answer == expected_answer