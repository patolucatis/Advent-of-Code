if __name__ == "__main__":
    code_file = open("bathroom.txt")
    grid = [["X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "1", "X", "X", "X"],
            ["X", "X", "2", "3", "4", "X", "X"],
            ["X", "5", "6", "7", "8", "9", "X"],
            ["X", "X", "A", "B", "C", "X", "X"],
            ["X", "X", "X", "D", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X"]]
    code = ""
    x = 3
    y = 1
    instructions = code_file.read().split("\n")
    for line in instructions:
        for i in line:
            x += 1 if i == "D" and grid[x + 1][y] != "X" else 0
            x -= 1 if i == "U" and grid[x - 1][y] != "X" else 0
            y += 1 if i == "R" and grid[x][y + 1] != "X" else 0
            y -= 1 if i == "L" and grid[x][y - 1] != "X" else 0
        code += grid[x][y]
    print(code)
    code_file.close()
