prompt = "\nPlease enter the name of a city you have visited."
prompt += "\nEnter 'quit' when you are finished. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# Ln.4: when a while loop starts with True, it will run forever until it
# reaches a break statement.
