def split_string_into_sets_of_3_lines(lines):
    sets_of_3_lines = []
    for i in range(0, len(lines), 3):
        sets_of_3_lines.append(lines[i:i + 3])
    return sets_of_3_lines


def find_common_item(list1, list2, list3):
    common_items = set(list1).intersection(set(list2), set(list3))
    return next(iter(common_items), None)


def prio(item: str) -> int:
    if item.isupper():
        return ord(item) - 38
    else:
        return ord(item) - 96


def main():
    with open('input/03.txt') as text_file:
        lines = text_file.read().split('\n')

        common_items = list()
        for rucksack in lines:
            first_compartment = set(rucksack[:len(rucksack) // 2])
            second_compartment = set(rucksack[len(rucksack) // 2:])
            for item in first_compartment.intersection(second_compartment):
                common_items.append(item)

        print(sum(map(prio, common_items)))

        badges = 0
        for group in split_string_into_sets_of_3_lines(lines):
            badges += prio(find_common_item(group[0],group[1],group[2]))
        print(badges)

if __name__ == '__main__':
    main()
