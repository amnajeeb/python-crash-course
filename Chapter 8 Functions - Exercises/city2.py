prompt_message = "Please indicate your toppings for your pizza: "
print("Please enter 'completed' when finished.")
print("Please enter 'quit' to leave the program.")

toppings = []

while True:
    topping = input(prompt_message)
    if topping != 'completed':
        print("We'll add " + topping.strip() + " to your pizza!")
        toppings.append(topping)

    if topping == 'quit':
        break

    if topping == 'completed':
        print('Here are your toppings for your pizza:')
        for top in toppings:
            print('\t' + top.title().strip())

        print("Your pizza will be ready in 5 minutes!")
        break
