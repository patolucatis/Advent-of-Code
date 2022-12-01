if __name__ == "__main__":
    file_bitwise = open("bitwise.txt", "r")
    operations = {}
    values = {}
    for line in file_bitwise.readlines():
        operation = line.replace("\n", "").split()
        if operation[0].isdigit() and len(operation) == 3:
            values[operation[-1]] = int(operation[0])
        else:
            if len(operation) == 4:
                operations[operation[-1]] = [operation[0], operation[1]]
            elif operation[1] == "LSHIFT" or operation[1] == "RSHIFT":
                operations[operation[-1]] = [operation[1], [operation[0], int(operation[2])]]
            else:
                operations[operation[-1]] = [operation[1], [operation[0], operation[2]]]
    file_bitwise.close()
    while "a" not in values.keys():
        for result, operation in operations.items():
            if
