import functools


def load_rules(file_name):
    unparsed_rules = open(file_name).readlines()
    rules = {}
    for unparsed_rule in unparsed_rules:
        outer_bag_name = unparsed_rule.split(" bags contain ")[0]
        inner_bags_raw = unparsed_rule.split(" bags contain ")[
            1].replace(".\n", "")

        inner_bags = {}
        if(inner_bags_raw != "no other bags"):
            for inner_bag in inner_bags_raw.split(", "):
                bag_count = int(inner_bag[0])
                # bag_name = inner_bag[2:len(inner_bag) - 5]
                bag_name = " ".join(inner_bag.split(" ")[1:3])
                inner_bags[bag_name] = bag_count

        rules[outer_bag_name] = inner_bags
    return rules


def get_inner_bag_counts(rules, root_bag_name):
    @functools.lru_cache(maxsize=None)
    def get_inner_bag_counts_memo(root_bag_name):
        bag_counts = {}
        for outer_bag_name, outer_bag_count in rules[root_bag_name].items():
            inner_bag_counts = get_inner_bag_counts(rules, outer_bag_name)
            inner_bag_counts_adjusted = {
                k: v * outer_bag_count
                for k, v
                in inner_bag_counts.items()
            }
            inner_bag_counts_adjusted[outer_bag_name] = outer_bag_count
            bag_counts = _sum_two_dictionaries(
                bag_counts, inner_bag_counts_adjusted
            )

        return bag_counts
    return get_inner_bag_counts_memo(root_bag_name)


def _sum_two_dictionaries(bag_counts_1, bag_counts_2):
    return {
        key:
            (bag_counts_1.get(key, 0) if bag_counts_2.get(key, 0) != {} else 1)
            +
            (bag_counts_2.get(key, 0) if bag_counts_2.get(key, 0) != {} else 1)
        for key
        in set(bag_counts_1) | set(bag_counts_2)
    }

def get_bags_containing(rules, root_bag):
    inner_bags = {
        bag_name: get_inner_bag_counts(rules, bag_name)
        for bag_name
        in rules.keys()
    }
    bags_that_contain_root = []
    for outer_name, inners in inner_bags.items():
        if(root_bag in inners.keys()):
            bags_that_contain_root.append(outer_name)
    return bags_that_contain_root

def count_required_bags(rules, root_bag):
    bags_containing = get_inner_bag_counts(rules, root_bag)
    return sum(count for count in bags_containing.values())
    # print(bags_containing)

if __name__ == "__main__":
    target_bag_name = 'shiny gold'
    rules = load_rules('rules.txt')
    bags_containing = get_bags_containing(rules, target_bag_name)
    print("count is: " + str(len(bags_containing)))
    print("required bags is: " + str(count_required_bags(rules, target_bag_name)))