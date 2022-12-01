def main():
    with open('input/01.txt') as text_file:
        lines = text_file.read().split('\n')

    elves = []
    calories = 0
    for x in lines:
        if x == '':
            elves.append(calories)
            calories = 0
            continue
        calories += int(x)

    print(max(elves))
    print(sum(sorted(elves)[-3:]))


if __name__ == '__main__':
    main()
