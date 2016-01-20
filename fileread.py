with open("dataset.txt") as textFile:
        lines = [line.split() for line in textFile]
        print lines[1][2]
