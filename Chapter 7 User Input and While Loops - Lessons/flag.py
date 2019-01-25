# Using a flag, p.124
prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program: "

active = True  # this is our flag.

while active:
    message = input(prompt)

    if message == 'quit':
        active = False  # This will stop the program from running.
    else:
        print(message)

# Code above: ln.7: no need to set active as True in the while loop as it has
# already been done on ln.5.
# Meaning of code: WHILE the flag is True, then message is the user input.
# IF input is 'quit', the the flag is set to False and the program ends. ELSE,
# The message is displayed until the input is quit.
