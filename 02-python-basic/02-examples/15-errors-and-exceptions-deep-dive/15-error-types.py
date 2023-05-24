while True:
    try:
        num = float(input("A positive number: "))
        if num == 0:
            raise RuntimeError("Number equals 0")
        if num < 0:
            raise RuntimeError("Number to small")
        kw = 1.0 / num
        break
    except ValueError:
        print("Error: No number")
    except ZeroDivisionError:
        print("Error: Number 0 found")
    except RuntimeError as e:
        print("Error:", e)
