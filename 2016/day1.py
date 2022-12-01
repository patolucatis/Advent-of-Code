if __name__ == "__main__":
    path_file = open("path.txt")
    directions = path_file.read().replace("\n", "").split(", ")
    x = 0
    y = 0
    direction = "N"
    index = 0
    compass = ["N", "E", "S", "W"]
    visited = [[0, 0]]
    check = False
    for i in directions:
        index += 1 if i[0] == "R" else -1
        index %= 4
        direction = compass[index]
        for j in range(int(i[1:])):
            x += 1 if direction == "E" else -1 if direction == "W" else 0
            y += 1 if direction == "N" else -1 if direction == "S" else 0
            if [x, y] not in visited:
                visited.append([x, y])
            elif not check:
                print(f"Repeated: {[x, y]}")
                check = True
    print(x, y)
    path_file.close()
