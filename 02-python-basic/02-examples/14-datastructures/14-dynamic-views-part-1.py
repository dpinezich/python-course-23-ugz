dc = {"Peter": 31, "Julia": 28, "Werner": 35}
print("Dictionary:", dc)

k = dc.keys()
print("Keys:", k)
for keys in k:
    print(keys)
if "Werner" in k:
    print("Key Werner is included")