class Date:
    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year:d}"


class Time:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"


class Period(Date, Time):
    def __init__(self, d, mo, y, h, mi, s):
        Date.__init__(self, d, mo, y)
        Time.__init__(self, h, mi, s)

    def __str__(self):
        return f"{Date.__str__(self)} {Time.__str__(self)}"


d = Date(3, 1, 2022)
print(d)
u = Time(16, 5, 20)
print(u)
z = Period(9, 5, 2022, 9, 35, 8)
print(z)