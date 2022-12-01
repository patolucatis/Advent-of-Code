if __name__ == '__main__':
    file_elevator = open("elevator.txt", "r")
    floors = file_elevator.read()
    file_elevator.close()
    floor = 0
    for move in floors:
        floor += 1 if move == "(" else -1
    print(f"Current floor: {floor}")
    count = 0
    floor2 = 0
    while floor2 >= 0:
        floor2 += 1 if floors[count] == "(" else -1
        count += 1
    print(f"You go down at stage {count}")
