def has_vowels(name):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for i in name:
        count += 1 if i in vowels else 0
    return count >= 3


def has_double(name):
    for i in range(len(name) - 1):
        if name[i] == name[i + 1]:
            return True
    return False


def not_forbidden(name):
    forbidden = ["ab", "cd", "pq", "xy"]
    for i in forbidden:
        if i in name:
            return False
    return True


def is_nice(name):
    return has_vowels(name) and has_double(name) and not_forbidden(name)


def has_two_gap(name):
    for i in range(len(name) - 2):
        if name[i] == name[i + 2]:
            return True
    return False


def has_two_doubles(name):
    for i in range(len(name) - 3):
        for j in range(i + 2, len(name) - 1):
            if name[i] + name[i + 1] == name[j] + name[j + 1]:
                return True
    return False


def is_nice_2(name):
    return has_two_gap(name) and has_two_doubles(name)


if __name__ == "__main__":
    file_naughtynice = open("naughtynice.txt")
    naughtynice = []
    for line in file_naughtynice.readlines():
        naughtynice.append(line.replace("\n", ""))
    count = 0
    for word in naughtynice:
        count += 1 if is_nice(word) else 0
    print(f"We have {count} nice people")
    count2 = 0
    for word in naughtynice:
        count2 += 1 if is_nice_2(word) else 0
    print(f"Now we have {count2} nice people")
