def print_day_month_year(dict):
    dict["day"] = dict["day"] + 5
    dict["month"] = dict["month"] - 3

    return dict["day"], dict["month"], dict["year"]


d, m, y = print_day_month_year({"day": 3, "month": 12, "year": 2023})

print(f"Das neue Datum ist der {d}.{m}.{y}")
