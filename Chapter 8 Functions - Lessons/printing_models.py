# Modifying a list in a function p.147

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until noe are left.
# Move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model..." + current_design.title() + "...")
    completed_models.append(current_design)

# Display all completed models:

print("\nThe following models have been printed:")
for model in completed_models:
    print('\t' + model.title())


# Now doing it using functions.

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []


def printing_models(unprinted_designs, printed_models):
    """"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design.title() + "...")
        printed_models.append(current_design)


def show_completed_models(printed_models):
    """"""
    print("\nThe following models have been printed:")
    for model in printed_models:
        print('\t' + model.title())


printing_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

print(unprinted_designs)
print(completed_models)
