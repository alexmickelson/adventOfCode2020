import luggage

rules = {
    'light red':    {'bright white': 1, 'muted yellow': 2},
    'dark orange':  {'bright white': 3, 'muted yellow': 4},
    'bright white': {'shiny gold': 1},
    'muted yellow': {'shiny gold': 2, 'faded blue': 9},
    'shiny gold':   {'dark olive': 1, 'vibrant plum': 2},
    'dark olive':   {'faded blue': 3, 'dotted black': 4},
    'vibrant plum': {'faded blue': 5, 'dotted black': 6},
    'faded blue': {},
    'dotted black': {},
}

def test_load_rules():
    expected_rules = {
        'light red':    {'bright white': 1, 'muted yellow': 2},
        'dark orange':  {'bright white': 3, 'muted yellow': 4},
        'bright white': {'shiny gold': 1},
        'muted yellow': {'shiny gold': 2, 'faded blue': 9},
        'shiny gold':   {'dark olive': 1, 'vibrant plum': 2},
        'dark olive':   {'faded blue': 3, 'dotted black': 4},
        'vibrant plum': {'faded blue': 5, 'dotted black': 6},
        'faded blue': {},
        'dotted black': {},
    }
    actual_rules = luggage.load_rules('example_rules.txt')
    assert expected_rules == actual_rules


def test_get_inner_bag_counts():
    target_bag_name = 'shiny gold'
    expected_bag_counts = {
        'dark olive': 1,
        'vibrant plum': 2,
        'faded blue': 13,
        'dotted black': 16,
    }
    actual_bag_counts = luggage.get_inner_bag_counts(rules, target_bag_name)
    assert actual_bag_counts == expected_bag_counts


def test_get_bags_containing():
    target_bag_name = 'shiny gold'
    expected_bags = [
        'bright white',
        'muted yellow',
        'dark orange',
        'light red',
    ]
    assert luggage.get_bags_containing(rules, target_bag_name).sort() == expected_bags.sort()

def test_count_total_bags_required():
    rules_pt_2 = luggage.load_rules('example_pt_2.txt')
    assert luggage.count_required_bags(rules_pt_2, 'shiny gold') == 126