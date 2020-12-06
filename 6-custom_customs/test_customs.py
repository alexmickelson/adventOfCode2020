import customs

def test_file_input():
    expected_answers = [
        ['abc'],
        [ 'a', 'b', 'c',],
        [ 'ab', 'ac',],
        [ 'a', 'a', 'a', 'a',],
        ['b']
    ]
    actual_answers = customs.read_customs_file('example_answers.txt')
    assert actual_answers == expected_answers

def test_counting_unique_answers():
    assert customs.count_unique_answers(["a"]) == 1
    assert customs.count_unique_answers(["a", "b"]) == 2
    assert customs.count_unique_answers(["a", "b", "a"]) == 2

def test_summing_answer_counts():
    answers = customs.read_customs_file('example_answers.txt')
    assert customs.answer_sum_counts(answers) == 11
