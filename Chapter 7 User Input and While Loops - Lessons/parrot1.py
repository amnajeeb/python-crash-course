# Start of Chapter 7 - User Input and While Loops, p.117

prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program: "

message = ''
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# Code above: ln.7 defines the condition for the loop to continue running; the
# condition is that the message is NOT 'quit'.
# If the condition is True, ln.8 displays the prompt and triggers the user to
# enter something. Now that the user has entered something, the loop restarts
# and message is checked again. If the word 'quit' was entered, the programme
# ends; otherwise, the prompt is displayed again.

# Ln.6: message is left empty so that python has something to check when
# running the while loop the first time.

# Ln.10: this piece of code is inserted so that the string 'quit' text is NOT
# displayed at the end of the programme (if something other than 'quit' is the
# the input, then it would get printed).
