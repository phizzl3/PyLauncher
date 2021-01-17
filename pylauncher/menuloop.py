# 01.17.2021
"""
Displays a numbered menu to console and returns a corresponding function 
or object based on user number selection using a passed *expanded list/tuple.

Import it and pass it an *expanded list of tuples/lists. It will return list[1]
for your selection.
"""

def display_menu(*args):
    """
    Displays menu items [0] from list/tuple pairs to console, 
    gets user selection and returns corresponding function/item [1] from pair.

    Args:
        *args (list/tuple): *Expanded list of list/tuple pairs with info to display to console,
        and item or function to call if chosen. ex: ('display name', function_to_call)

    Returns:
        item/function: Item/Function [1] from corresponding selection, (list/tuple index [1])

    Usage Example:
        display_menu(*options)()  # Displays menu and calls the returned function
    """

    # Number (enumerate) and display the options [0] from args pair starting at 1
    for i, arg in enumerate(args, 1):
        print(f' [{i}]: {arg[0]}')

    # Ask for user input and return the corresponding item/function [1] only if
    # the selection can be found in list.
    while True:
        sel = input('\n Selection: ')
        if sel.isdigit() and int(sel) <= len(args) and int(sel):
            return args[int(sel)-1][1]
        else:
            print('\n Please choose from available selections.')


if __name__ == "__main__":
    # Just a quick test/example to see how it works. 

    opts = (
        ('print', print),
        ('input', input),
    )

    display_menu(*opts)('it works. ')
