

class PasswordRule:
    def __init__(self, min_letter_count, max_letter_count, letter):
        self.min_letter_count = min_letter_count
        self.max_letter_count = max_letter_count
        self.letter = letter

    def __eq__(self, other):
        return (
            self.min_letter_count == other.min_letter_count and
            self.max_letter_count == other.max_letter_count and
            self.letter == other.letter
        )

    def __hash__(self):
        return hash(self.min_letter_count, self.max_letter_count, self.letter)
    
    def __repr__(self):
        return '({}, {}, {})'.format(self.min_letter_count, self.max_letter_count, self.letter)

    def matches(self, password):
        return self.min_letter_count <= password.count(self.letter) <= self.max_letter_count