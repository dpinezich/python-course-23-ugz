file = open('my_file.txt', 'r')
for line in file:
    line = line.strip()
    print(line)
file.close()
