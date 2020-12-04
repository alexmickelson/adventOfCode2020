from models.passoword_rule import PasswordRule

def read_input(filename):
    input_file = open(filename);
    password_list = []
    for line in input_file.readlines():
        min_letter_count = int(line.split(' ')[0].split('-')[0])
        max_letter_count = int(line.split(' ')[0].split('-')[1])
        letter = line.split(' ')[1].split(':')[0]
        password = line.split(' ')[2].split('\n')[0]
        password_list.append(
            (PasswordRule(min_letter_count, max_letter_count, letter), password)
            )
    return password_list

def count_good_passwords(password_list):
    return sum([rule.matches(password) for rule, password in password_list])
