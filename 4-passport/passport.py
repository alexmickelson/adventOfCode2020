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
    required_attributes = [
        'ecl',
        'pid',
        'eyr',
        'hcl',
        'byr',
        'iyr',
        # 'cid',
        'hgt',
    ]
    present_attributes = [k for k in passport.keys()]
    return all([req in present_attributes for req in required_attributes])

def count_valid_passports(passports):
    return sum(passport_is_valid(passport) for passport in passports)