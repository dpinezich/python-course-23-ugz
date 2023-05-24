tx = "This is an example phrase"
print("Text:", tx)

search = "ex"
print("Searchtext:", search)
print()

num = tx.count(search)
print(f"count: The string {search} appears {num} times")
pos = tx.find(search)
while pos != -1:
    print("Position", pos)
    pos = tx.find(search, pos+1)
pos = tx.rfind(search)
if pos != -1:
    print("rfind: Last time at this position", pos)