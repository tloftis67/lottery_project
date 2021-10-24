lastnum = int(input("Please type an integer here:"))
counter = 1
while counter <= lastnum:
    print("{0}. This is line: {0}".format(counter))
    counter = counter + 1

while True:

    choice = input("Do you want to add another new employee? yes/no").lower()
    print("choice: {0}".format(choice))
    if choice == "y" or choice == "yes":
        print("Ask a series of questions about a new employee")
    else:
        print("We are done adding employees")
        break
