from datetime import datetime


# ----------------------------- Colour Adding -----------------------------
def set_colour():

    # Select day type
    print("\n1. Add today\n2. Prev")
    op2 = int(input("Enter Option : "))

    if op2 == 1:
        day = datetime.now().weekday()
    else:
        day = int(input("Enter Day : ")) - 1

    colour = input("Enter Colour : ").lower()

    if colour in days[day]:
        days[day][colour] += 1
        
    else:
        days[day][colour] = 1

    # Update history table
    f1 = open("history.csv", "w")
    f1.write("Day, Colour\n")

    history[day] = colour
    for element in range(len(history)):
        f1.write(str(element + 1) + ", " + history[element] + "\n")
    f1.close()


# ---------------------------- Colour Guessing ----------------------------
def get_colour():
    # Sort by value
    for x in range(len(days)):
        days[x] = dict(reversed(sorted(days[x].items(), key=lambda element: element[1])))

    print("\n1. View tomorrow \n2. Given date")
    op3 = int(input("Enter Option : "))

    if op3 == 1:
        day = datetime.now().weekday() + 1
    else:
        day = int(input("Enter Day : ")) - 1

    new_week_history = history.copy()

    # print(new_week_history[:day], list(days[day].keys())[0], list(days[day].keys())[1])

    # Check last week colour and guess the colour

    print(day, days[day], history[day], new_week_history[:day])
    try:
        if list(days[day].keys())[0] == history[day] or len(days[day]) != 1 or list(days[day].keys())[0] in new_week_history[:day]:
            if list(days[day].keys())[1] not in new_week_history[:day]:
                return list(days[day].keys())[1]
            else:
                return list(days[day].keys())[2]
        else:
            return list(days[day].keys())[0]
    except IndexError:
        print("\nCan't guess the colour. I want more data to guessing process..")


# ---------------------------- Colour2 Guessing ----------------------------
def get_colour2(primary_colour):
    pass


if __name__ == "__main__":

    history = ["", "", "", "", ""]
    days = [{}, {}, {}, {}, {}]
    colour2 = {}

    # Load data file
    f = open("data.csv", "r")
    for i in f:
        item = i.split()
        if "".join(item[0][:len(item[0]) - 1]) == "colour":
            continue
        days[int(item[2]) - 1]["".join(item[0][:len(item[0]) - 1])] = int("".join(item[1][:len(item[1]) - 1]))
    f.close()

    # Load history
    f3 = open("history.csv", "r")
    for i in f3:
        item = i.split()
        if "".join(item[0][:len(item[0]) - 1]) == "Day":
            continue

        history[int("".join(item[0][:1])) - 1] = "".join(item[1][:len(item[1])])
    f3.close()

    # Load colour2 file
    f4 = open("colour2.csv", "r")
    for i in f4:
        pass

    f4.close()

    while True:
        print("\n1. Set\n2. Guess")
        op = int(input("Enter Option : "))
        if op == 1:
            set_colour()

        else:
            result = get_colour()
            print("\nGuessed Primary Colour : ", result)
            print("Guessed Secondary Colour : ", get_colour2(result))

        # Update the data file
        f = open("data.csv", "w")
        f.write("colour, value, day\n")
        for i in range(len(days)):
            for j in days[i]:
                f.write(j + ", " + str(days[i][j]) + ", " + str(i + 1) + "\n")
        f.close()

        if input("\nDo you want get another service (n/y) : ") == "n":
            break
