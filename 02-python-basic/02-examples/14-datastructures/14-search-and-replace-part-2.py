tx = "This is an example phrase"
print("Text:", tx)

if tx.startswith("This"):
    print("Text starts with This")
if not tx.endswith("This"):
    print("Text ends not with This")

tx = tx.replace("is", "was")
print("After replacing:", tx)

z = 48.2
tx = str(z)
tx = tx.replace(".", ",")
print("Number with comma:", tx)