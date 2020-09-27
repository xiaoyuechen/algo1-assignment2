import sys
import random


def rangen(max, filename='nums.txt'):
    f = open(filename, 'w')
    random.seed()

    for _ in range(0, max):
        f.write(str(random.randint(0, max)) + "\n")

    f.close()


if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Wrong number of arguments. Usage: python rangen.py max")
    else:
        rangen(int(sys.argv[1]))
