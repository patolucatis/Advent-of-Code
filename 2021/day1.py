if __name__ == '__main__':
    file_depths = open("Sinking.txt", "r")
    depths = []
    for line in file_depths.readlines():
        depths.append(int(line))
    file_depths.close()
    print(depths)
    lowers = 0
    current_depth = depths[0]
    for depth in depths:
        if depth > current_depth:
            lowers += 1
        current_depth = depth
    print(f"{lowers} for single counting")
    lowers_window = 0
    depth_window = sum(depths[:3])
    print(len(depths))
    for i in range(0, len(depths) - 2):
        if depth_window < sum(depths[i:i + 3]):
            lowers_window += 1
        depth_window = sum(depths[i:i + 3])
    print(f"{lowers_window} for window counting")