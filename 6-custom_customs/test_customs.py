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
    
def test_counting_common_answers():
    assert customs.count_common_answers(["a"]) == 1
    assert customs.count_common_answers(["a", "b"]) == 0
    assert customs.count_common_answers(["a", "ab", "a",]) == 1

def test_summing_answer_counts():
    answers = customs.read_customs_file('example_answers.txt')
    assert customs.answer_sum_counts(answers) == 11

def test_summing_common_answer_counts():
    answers = customs.read_customs_file('example_answers.txt')
    assert customs.answer_sum_common_counts(answers) == 6
