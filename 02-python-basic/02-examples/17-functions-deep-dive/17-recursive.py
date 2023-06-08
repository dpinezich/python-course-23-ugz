def make_half(value):
    print(value)
    value = value / 2
    if value > 0.05:
        make_half(value)
make_half(3)