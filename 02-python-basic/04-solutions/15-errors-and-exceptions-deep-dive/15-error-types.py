dc = {"Peter": 31, "Julia": 28, "Werner": 35}
print("Dictionary:", dc)
try:
    print(dc[23])
except KeyError:
    print("Key was not found")
