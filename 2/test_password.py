from password import read_input, count_good_passwords
from models.passoword_rule import PasswordRule

def test_file_input():
    expected_input = [
        (PasswordRule(1, 3, "a"), 'abcde'),
        (PasswordRule(1, 3, "b"), 'cdefg'),
        (PasswordRule(2, 9, "c"), 'ccccccccc'),
    ]
    actual_input = read_input('example.txt')
    assert len(actual_input) == len(expected_input)
    assert all([a == b for (a, b) in zip(actual_input, expected_input)])

def test_password_rule_equality():
    assert PasswordRule(1, 2, '1') == PasswordRule(1, 2, '1')
    assert (PasswordRule(2, 9, 'c'), 'ccccccccc') == (PasswordRule(2, 9, 'c'), 'ccccccccc')
    assert [(PasswordRule(2, 9, 'c'), 'ccccccccc')] == [(PasswordRule(2, 9, 'c'), 'ccccccccc')]

def test_password_rule_pass():
    rule1 = PasswordRule(1, 3, "a")
    assert rule1.matches('abcde') == True
    rule1 = PasswordRule(1, 3, "b")
    assert rule1.matches('cdefg') == False

def test_count_good_passwords():
    input_list = read_input('example.txt')
    assert count_good_passwords(input_list) == 2

def test_count_good_passwords_acutual():
    input_list = read_input('actual.txt')
    assert count_good_passwords(input_list) == 396
    