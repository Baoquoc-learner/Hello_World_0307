# Modifying a List in a Function

"""
# Start with some designs that need to be printed.

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Display all completed models.
# Hiển thị tất cả các giá trị đã hoàn tất
print("\nThe following models have been printed:")

for completed_model in completed_models:
    print(completed_model)
"""
print("\t==================================================")

# cách thứ 2 để chỉnh sửa


def printModels(unprintedDesigns, completedModels):
    """
    simulate printing each design, untill non are left.
    Move each design to completedModels after printing.
    """
    while unprintedDesigns:
        currentDesign = unprintedDesigns.pop()
        print(f"Printing Model: {currentDesign}")
        completedModels.append(currentDesign)


def showCompletedModels(completedModels):
    """
    Show all the models that were printed
    """
    print("\nThe following models have bên printed:")
    for completedModel in completedModels:
        print(completedModel)


unprintedDesigns = ['phone case', 'robot pendant', 'dodecahedron']
completedModels = []

printModels(unprintedDesigns, completedModels)
showCompletedModels(completedModels)
