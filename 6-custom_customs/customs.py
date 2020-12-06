

def read_customs_file(file_name):
    return [
        a.split("\n")
        for a
        in open(file_name).read().split("\n\n")
    ]


def count_unique_answers(list_of_answers):
    return len(set(
        answer
        for sublist
        in list_of_answers
        for answer
        in sublist
        )
    )

def count_common_answers(list_of_answers):
    return len(set(list_of_answers[0]).intersection(*list_of_answers))

def answer_sum_counts(answers):
    return sum(count_unique_answers(a) for a in answers)

def answer_sum_common_counts(answers):
    return sum(count_common_answers(a) for a in answers)

if __name__ == "__main__":
    # part 1
    answers = read_customs_file('answers.txt')
    print('sum of answers: ' + str(answer_sum_counts(answers)))

    # part 2
    print('sum of common answers: ' + str(answer_sum_common_counts(answers)))