def is_fully_included(range1, range2):
    # Convert the ranges to sets
    range1 = set(range(range1[0], range1[1]+1))
    range2 = set(range(range2[0], range2[1]+1))

    # Check if range1 is a subset of range2, or vice versa
    return range1.issubset(range2) or range2.issubset(range1)

def is_partially_included(range1, range2):
    # Convert the ranges to sets
    range1 = set(range(range1[0], range1[1]+1))
    range2 = set(range(range2[0], range2[1]+1))

    # Check if range1 is a subset of range2, or vice versa
    # or if there is any overlap between the two ranges
    return range1.issubset(range2) or range2.issubset(range1) or bool(range1 & range2)


def main():
    with open('input/04.txt') as text_file:
        lines = text_file.read().split('\n')

    count = 0
    count_2 = 0
    for line in lines:
        elf_1, elf_2 = line.split(',')

        e1_s, e1_e = elf_1.split('-')
        e2_s, e2_e = elf_2.split('-')

        if is_fully_included(
            [int(e1_s), int(e1_e)],
            [int(e2_s), int(e2_e)],):
            count += 1

        if is_partially_included(
            [int(e1_s), int(e1_e)],
            [int(e2_s), int(e2_e)],):
            count_2 += 1



    print(count)
    print(count_2)


if __name__ == '__main__':
    main()

