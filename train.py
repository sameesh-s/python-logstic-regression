with open('dataset.txt', 'r') as f:
    data = f.readlines()

    for line in data:
        words = line.split()
        print words
