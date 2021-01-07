import random
import time

mock_data = []
mock_sequence = [2000]

how_many = 60

for i in range(0, how_many): # Start at 0 stop before 60 (that is, a count of 60 items)
    mock_data.append(random.randint(0, 4095)) # a random set of values
    # time.sleep(1)
    mock_sequence.append(mock_sequence[i] + random.randint(-20,20)) # each data member is a random difference from the last

if __name__ == "__main__":
    # print(mock_data, mock_sequence)
    with open('mode_data.txt', 'wt') as f_mock:
        print(mock_data, file=f_mock)
    with open('mode_sequence.txt', 'wt') as f_seq:
        print(mock_sequence, file=f_seq)
