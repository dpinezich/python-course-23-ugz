def number_to_position(nr):
    # raiseException
    result = ""
    if nr == 1:
        result = "Keeper"
    elif nr > 1 and nr < 5: #show simplyfiing
        result = "Defender"
    elif nr > 5 and nr < 9:
        result = "Midfielder"
    elif nr > 9:
        result = "Striker"

    return result


def sum_expenses(lst):
    result = 0
    for l in lst:
        result += l

    return l

def sum_expenses_adv(lst, budget = 1000):
    result = 0
    for l in lst:
        result += l
        if result > budget:
            print("You are over budget")
        else:
            print("You still have " + str(budget - result) + " in your budget")

    return l


def show_players(dict):
    for d in dict:
        # print(dict[d])
        print("Name", dict[d]["name"], "Worth", dict[d]["worth"])