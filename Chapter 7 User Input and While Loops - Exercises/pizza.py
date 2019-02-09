prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)

    if topping != 'quit':
        print("I'll add " + topping.title() + " to your pizza!")
    else:
        break

# Code above: ln.4: while the flag is True, ln.7, if user input is NOT 'quit',
# then print that you'll had the input (the topping) to the pizza. Else (i.e.
# if user input IS 'quit'), break the loop.
