import collections


def is_valid(name: str):
    part, checksum = name.replace("-", "").replace("]", "").split("[")
    letters = ""
    i = 0
    while not part[i].isdigit():
        letters += part[i]
        i += 1
    numbers = part.replace(letters, "")
    letter_count = collections.Counter(letters)
    ordered = sorted(letter_count.items(), key=lambda letter: (letter[1], letter[0]), reverse=True)
    checksum2 = "".join([i[0] for i in ordered])
    print(checksum2)


if __name__ == "__main__":
    is_valid("not-a-real-room-404[oarel]")