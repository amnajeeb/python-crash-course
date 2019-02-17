# Exercise p.159

# 8-15


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
