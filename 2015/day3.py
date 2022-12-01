if __name__ == "__main__":
    directions_file = open("directions.txt", "r")
    directions = list(directions_file.read())
    directions_file.close()
    positionX = 0
    positionY = 0
    houses = [[0, 0]]
    for direction in directions:
        positionX += 1 if direction == ">" else 0
        positionX -= 1 if direction == "<" else 0
        positionY += 1 if direction == "^" else 0
        positionY -= 1 if direction == "v" else 0
        if [positionX, positionY] not in houses:
            houses.append([positionX, positionY])
    print(f"We've visited {len(houses)} houses")
    santaX = 0
    santaY = 0
    roboX = 0
    roboY = 0
    houses2 = [[0, 0]]
    for i in range(len(directions)):
        if i % 2 == 0:
            santaX += 1 if directions[i] == ">" else 0
            santaX -= 1 if directions[i] == "<" else 0
            santaY += 1 if directions[i] == "^" else 0
            santaY -= 1 if directions[i] == "v" else 0

        else:
            roboX += 1 if directions[i] == ">" else 0
            roboX -= 1 if directions[i] == "<" else 0
            roboY += 1 if directions[i] == "^" else 0
            roboY -= 1 if directions[i] == "v" else 0
        if [santaX, santaY] not in houses2:
            houses2.append([santaX, santaY])
        if [roboX, roboY] not in houses2:
            houses2.append([roboX, roboY])
    print(houses2)
    print(f"Now we visited {len(houses2)} houses")
