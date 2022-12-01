def stars():
    file = open("calories.txt")
    elves = []
    food = []
    for line in file.readlines():
        if line != "\n":
            food.append(int(line))
        else:
            elves.append(sum(food))
            food = []
    print(f"First star:{max(elves)}")
    elves.sort(reverse=True)
    print(f"Second star:{elves[0] + elves[1] + elves[2]}")
    file.close()


if __name__ == "__main__":
    stars()
