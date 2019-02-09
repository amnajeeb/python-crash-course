prompt = "\nCould you please confirm your age? "
prompt += "\nEnter 'quit' to leave: "

while True:
    age = int(input(prompt))
    print(prompt)

    if age != 'quit':

        if age < 3:
            print("Because you're " + str(age) + ", your entrance is free!")
        elif age < 12:
            print("Because you're " + str(age) + ", your ticket is $12.")
        else:
            print("Because you're " + str(age) + ", your ticket is $15.")

    else:
        break
