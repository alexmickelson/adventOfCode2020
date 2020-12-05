import passport as p

def test_read_input():
    expected_passports = [
        {
            'ecl': 'gry',
            'pid': '860033327',
            'eyr': '2020',
            'hcl': '#fffffd',
            'byr': '1937',
            'iyr': '2017',
            'cid': '147',
            'hgt': '183cm',
        },
        {
            'iyr': '2013',
            'ecl': 'amb',
            'cid': '350',
            'eyr': '2023',
            'pid': '028048884',
            'hcl': '#cfa07d',
            'byr': '1929',
        },
        {

            'hcl': '#ae17e1',
            'iyr': '2013',
            'eyr': '2024',
            'ecl': 'brn',
            'pid': '760753108',
            'byr': '1931',
            'hgt': '179cm',
        },
        {
            'hcl': '#cfa07d',
            'eyr': '2025',
            'pid': '166559648',
            'iyr': '2011',
            'ecl': 'brn',
            'hgt': '59in',
        }
    ]
    assert p.create_passport_list_from_file('example_passports.txt') == expected_passports

def test_count_valid_passports():
    passports = p.create_passport_list_from_file('example_passports.txt')
    assert p.count_valid_passports(passports) == 2

def test_do_pt_1():
    passports = p.create_passport_list_from_file('passports.txt')
    assert p.count_valid_passports(passports) == 245
