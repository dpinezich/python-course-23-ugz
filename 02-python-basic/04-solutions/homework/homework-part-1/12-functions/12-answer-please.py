def what_to_eat(mood):
    if mood == "good":
        return "spaghetti"
    elif mood == "ok":
        return "lasagna"
    else:
        return "pizza"


def what_weather(weather):
    if weather == "sunny":
        return "go outside"
    elif weather == "rainy":
        return "go to the mall"
    else:
        return "stay at home"


def tell_me(weather, mood):
    print("Today is", weather, "I will", what_weather(weather), "and eat",
          what_to_eat(mood), "because I am having a/an", mood, "day")


tell_me("sunny", "ok")
tell_me("rainy", "good")
tell_me("foggy", "spectacular")

