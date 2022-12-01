def count_bits(byte_list, size):
    counters = []
    for i in range(size):
        counter = {"0": 0, "1": 0}
        for byte in byte_list:
            counter[byte[i]] += 1
        counters.append(counter)
    return counters


if __name__ == "__main__":
    file_diagnosis = open("diagnosis.txt")
    diagnosis = []
    for line in file_diagnosis.readlines():
        diagnosis.append(line.replace("\n", ""))
    file_diagnosis.close()
    size = len(diagnosis[0])
    counters = count_bits(diagnosis, size)
    gamma = ""
    epsilon = ""
    for counter in counters:
        gamma += "0" if counter["0"] > counter["1"] else "1"
        epsilon += "0" if counter["0"] < counter["1"] else "1"
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(f"The result for power is {gamma * epsilon}")
    oxygen = ""
    co2 = ""
    o_counters = counters
    c_counters = counters
    o_list = diagnosis
    c_list = diagnosis

