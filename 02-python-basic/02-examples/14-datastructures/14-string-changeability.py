tx = "This is a text"
print(tx)
try:
    tx[4:6] = "was"
except:
    print("Error")
tx = tx[:4] + "was" + tx[7:]
print(tx)
