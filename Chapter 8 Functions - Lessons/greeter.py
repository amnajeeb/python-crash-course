# Defining a function, p.134. Start of Chapter 8 - Functions.


def greet_user(username):
    """Display a simple greeting."""
    print("Hello " + username.title().strip() + "!")


greet_user('sean')

# Code above:
# ln.4: def is the function definition.
# ln.4: between (), we've put username meaning that we'll need to provide
# values for username each time we call the function.
# ln.5: this is a docstring which is a description of the function.
# ln.6: this is the code of the function i.e. what a function does when called.
# ln.9: we call the def greet_user() and we've provide 'sean' as value for
# username so that Python is able to execute the function properly.
