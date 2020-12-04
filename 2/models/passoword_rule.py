

class PasswordRule:
    def __init__(self, first_position, second_position, letter):
        self.first_position = first_position
        self.second_position = second_position
        self.letter = letter

    def __eq__(self, other):
        return (
            self.first_position == other.first_position and
            self.second_position == other.second_position and
            self.letter == other.letter
        )

    def __hash__(self):
        return hash(self.first_position, self.second_position, self.letter)
    
    def __repr__(self):
        return '({}, {}, {})'.format(self.first_position, self.second_position, self.letter)

    def matches(self, password):
        return (
            (password[self.first_position - 1] == self.letter) ^
            (password[self.second_position - 1] == self.letter)
        )