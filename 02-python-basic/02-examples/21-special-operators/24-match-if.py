x = random.randint(1,10)
print("x * 1.5 =", x * 1.5)

match x * 1.5:
  case x if x < 5:
    print("kleiner Wert")
  case x if x > 11:
    print("großer Wert")
  case _:
    print("mittlerer Wert")