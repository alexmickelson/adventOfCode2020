import re


def create_passport_list_from_file(file_name):
    return [
        {
            attr.split(':')[0]: attr.split(':')[1]
            for attr
            in raw_passport.split(' ')
        }
        for raw_passport in
        [
            p.replace("\n", " ")
            for p
            in open(file_name).read().split("\n\n")
        ]
    ]


def passport_is_valid(passport):
    year_between_1920_and_2020 = r"^(19[2-9][0-9]|200[0-2])$"
    year_between_2010_and_2020 = r"^(201[0-9]|2020)$"
    year_between_2020_and_2030 = r"^(202[0-9]|2030)$"
    cm_between_150_and_193_or_in_between_59_and_76 = r"^(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)$"
    hex_color = r"^#[0-9,a-f]{6}$"
    eye_color = r"^(amb|blu|brn|gry|grn|hzl|oth)$"
    nine_digits = r"^[0-9]{9}$"

    each_attribute_valid = [
        bool(re.match(year_between_1920_and_2020,                     passport.get('byr') or 'invalid')),
        bool(re.match(year_between_2010_and_2020,                     passport.get('iyr') or 'invalid')),
        bool(re.match(year_between_2020_and_2030,                     passport.get('eyr') or 'invalid')),
        bool(re.match(cm_between_150_and_193_or_in_between_59_and_76, passport.get('hgt') or 'invalid')),
        bool(re.match(hex_color,                                      passport.get('hcl') or 'invalid')),
        bool(re.match(eye_color,                                      passport.get('ecl') or 'invalid')),
        bool(re.match(nine_digits,                                    passport.get('pid') or 'invalid')),
    ]
    return all(each_attribute_valid)

def count_valid_passports(passports):
    valid_passports = [p  for p in passports if passport_is_valid(p)]
    return sum(passport_is_valid(passport) for passport in passports)


passports = create_passport_list_from_file('passports.txt')
# count_valid_passports(passports)
print(count_valid_passports(passports))