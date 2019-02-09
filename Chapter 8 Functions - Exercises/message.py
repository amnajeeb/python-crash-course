# Exercises p.135

# 8-1


def display_message():
    """Message telling people what I'm learning in this chapter"""
    print("Hello folks, I'm learning Python functions at the moment!")


display_message()


def favorite_book(title):
    """Message displaying my favorite book"""
    print("Hello guys, my favorite book is " + title.title().strip() + "!")


favorite_book('shoe dog')
