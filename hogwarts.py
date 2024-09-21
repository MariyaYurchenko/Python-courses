name = input("What's your name? ").strip().capitalize()

match name:
    case "Harry":
        print("Gryffindor!")
    case "Ron":
        print("Gryffindor!")
    case "Hermione":
        print("Gryffindor!")
    case "Draco":
        print("Slytherin!")
    case _:
        print("Go home muggle.")