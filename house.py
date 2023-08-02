name = input("what's your name ? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print ("Slytherin")
    case _:
        input("please update your house detail,what's your house name?" )
        print("Thank you the detail will be updated")
