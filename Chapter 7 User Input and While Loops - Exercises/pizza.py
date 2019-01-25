prompt = "\nEnter the toppings you would like to add to your pizza"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break

    print(topping)
