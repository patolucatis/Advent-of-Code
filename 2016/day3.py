from typing import List


def is_triangle(values: List) -> bool:
    return (values[0] < values[1] + values[2]
            and values[1] < values[0] + values[2]
            and values[2] < values[0] + values[1])


if __name__ == "__main__":
    triangles_file = open("triangles.txt")
    count = 0
    count2 = 0
    rows = []
    for line in triangles_file.readlines():
        triangle = [int(i) for i in line.split()]
        rows.append(triangle)
        count += 1 if is_triangle(triangle) else 0
    for i in range(3):
        for j in range(0, len(rows), 3):
            tri = [rows[j][i], rows[j + 1][i], rows[j + 2][i]]
            count2 += 1 if is_triangle(tri) else 0
    print(count)
    print(count2)
    triangles_file.close()
