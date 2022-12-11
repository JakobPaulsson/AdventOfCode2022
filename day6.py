def get_start_of_message(marker_size, input):
    for i in range(len(input) - marker_size):
        current = set([x for x in input[i:i+marker_size]])
        if len(current) == marker_size:
            return i+marker_size

input = open("i.txt").read()
start_of_message = get_start_of_message(4, input)
start_of_message2 = get_start_of_message(14, input)
print("P1:", start_of_message, "P2:", start_of_message2)