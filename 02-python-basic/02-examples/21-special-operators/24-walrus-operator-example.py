# 24-walrus-operator-example.py

import random
random.seed()
total = 0
while (total := total + random.randint(1,8)) < 30:
	print("Subtotal:", total)