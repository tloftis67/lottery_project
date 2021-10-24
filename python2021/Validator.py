
def game_int():
    while True:
        try:
            value = int(input("Please type a number from 1-10"))
        except (ValueError, TypeError):
            print("Not an Integer! Try again")
        else:
            if value >= 1 and value <= 10:
                print("{0} is a number between 1 and 10, congrats!".format(value))
                break
            else:
                print("Value is out of range, try again!")






