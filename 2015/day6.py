class Garden:
    def __init__(self):
        self.lights = []
        self.bright = []
        for i in range(1000):
            self.lights.append([False] * 1000)
            self.bright.append([0] * 1000)

    def count_lights(self):
        count = 0
        for i in self.lights:
            count += i.count(True)
        return count

    def count_brightness(self):
        count = 0
        for i in self.bright:
            count += sum(i)
        return count

    def turn_on(self, start, end):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                self.lights[i][j] = True
                self.bright[i][j] += 1

    def turn_off(self, start, end):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                self.lights[i][j] = False
                self.bright[i][j] -= 1 if self.bright[i][j] > 0 else 0

    def toggle(self, start, end):
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                self.lights[i][j] = not self.lights[i][j]
                self.bright[i][j] += 2


if __name__ == "__main__":
    instructions_file = open("instructions.txt")
    instructions = []
    for line in instructions_file.readlines():
        full_instruction = line.replace("\n", "").split()
        action = full_instruction[0] + " " + full_instruction[1] if full_instruction[1].isalpha() else full_instruction[0]
        coordinates_start = list(map(int, full_instruction[-3].split(",")))
        coordinates_end = list(map(int, full_instruction[-1].split(",")))
        full_action = (action, coordinates_start, coordinates_end)
        instructions.append(full_action)
    instructions_file.close()
    g = Garden()
    for instruction in instructions:
        if instruction[0] == "turn on":
            g.turn_on(instruction[1], instruction[2])
        if instruction[0] == "turn off":
            g.turn_off(instruction[1], instruction[2])
        if instruction[0] == "toggle":
            g.toggle(instruction[1], instruction[2])
    print(f"We've turned on {g.count_lights()} lights")
    print(f"The total brightness is {g.count_brightness()}")
