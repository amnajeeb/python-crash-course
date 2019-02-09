# Filling a dictionary with User Input, p.130

responses = {}

# Set a flag to indicate that the polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input('What is your name? ')
    response = input('Which mountain would you like to climb some day? ')

    # Store responses in dictionary.
    responses[name] = response

    # Find out if anyone is going to take the poll
    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        polling_active = False

    # polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + ' would like to climb the ' + response.title() + ".")


# Code above
# ln.14: create key-value attribute in dictionary responses. name is the key,
# response is the value.
# ln.18: introduces a condition (if response 'no') that could stop the loop
