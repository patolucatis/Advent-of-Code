if __name__ == "__main__":
    file_packages = open("packages.txt", "r")
    packages = []
    for line in file_packages.readlines():
        packages.append(list(map(int, line.replace("\n", "").split("x"))))
    surfaces = []
    perimeters = []
    volumes = []
    for package in packages:
        surfaces.append([2 * package[1] * package[0], 2 * package[1] * package[2], 2 * package[2] * package[0]])
        perimeters.append([2 * package[1] + 2 * package[0], 2 * package[1] + 2 * package[2],
                           2 * package[2] + 2 * package[0]])
        volumes.append(package[0] * package[1] * package[2])
    total_paper = 0
    for package in surfaces:
        total_paper += sum(package) + min(package) // 2
    total_ribbon = 0
    for i in range(len(packages)):
        total_ribbon += min(perimeters[i]) + volumes[i]
    print(f"Total of paper needed is {total_paper}")
    print(f"Total of ribbon needed is {total_ribbon}")
