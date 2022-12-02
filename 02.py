def main():
    with open('input/02.txt') as text_file:
        lines = text_file.read().split('\n')

    point_mapping = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }
    points_a = 0
    points_b = 0
    b = ""
    for x in lines:
        opponent, you = x.split(" ")
        points_a += point_mapping[you]

        if opponent == "A" and you == "X":
            points_a += 3
            b = "Z"
        if opponent == "B" and you == "X":
            points_a += 0
            b = "X"
        if opponent == "C" and you == "X":
            points_a += 6
            b = "Y"
        if opponent == "A" and you == "Y":
            points_a += 6
            b = "X"
        if opponent == "B" and you == "Y":
            points_a += 3
            b = "Y"
        if opponent == "C" and you == "Y":
            points_a += 0
            b = "Z"
        if opponent == "A" and you == "Z":
            points_a += 0
            b = "Y"
        if opponent == "B" and you == "Z":
            points_a += 6
            b = "Z"
        if opponent == "C" and you == "Z":
            points_a += 3
            b = "X"

        if you == "Y":
            points_b += 3
        if you == "Z":
            points_b += 6
        points_b += point_mapping[b]

    print(points_a)
    print(points_b)


if __name__ == '__main__':
    main()
