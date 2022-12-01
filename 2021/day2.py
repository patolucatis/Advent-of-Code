if __name__ == '__main__':
    file_path = open("path.txt", "r")
    path = []
    for line in file_path.readlines():
        directions = line.split()
        path.append((directions[0], int(directions[1])))
    file_path.close()
    x = 0
    y = 0
    for direction in path:
        x += direction[1] if direction[0] == "forward" else 0
        y += direction[1] if direction[0] == "down" else 0
        y -= direction[1] if direction[0] == "up" else 0
    print(f"Final result without aim: {x * y}")
    x2 = 0
    y2 = 0
    aim = 0
    for direction in path:
        aim += direction[1] if direction[0] == "down" else 0
        aim -= direction[1] if direction[0] == "up" else 0
        if direction[0] == "forward":
            x2 += direction[1]
            y2 += aim * direction[1]
    print(f"Final result with aim: {x2 * y2}")
