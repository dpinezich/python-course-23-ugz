def volume(width, length, depth=1, color="schwarz"):
    print("Values:", width, length, depth, color)
    print("Volume:", width * length * depth, "Farbe:", color)


volume(4, 6, 2, "red")
volume(2, 12, 7)
volume(5, 8)
volume(4, 7, color="red")