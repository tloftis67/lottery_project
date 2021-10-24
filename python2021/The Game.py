
while True:
        try:
            value = int(input("Please type a number from 1-100"))
        except (ValueError, TypeError):
            print("Not an Integer! Try again")
        else:
            if value >= 1 and value <= 100:
                print("{0} is a number between 1 and 100, congrats!".format(value))
                break
            else:
                print("Value is out of range, try again!")
