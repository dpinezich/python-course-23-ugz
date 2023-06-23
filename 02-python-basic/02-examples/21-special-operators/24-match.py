x = "Paris"

match x:
    case "Paris":
         print("Frankreich")
    case "Rom":
        print("Italien")
    case "Madrid":
        print("Spanien")
    case _:
        print("Unbekanntes Land")