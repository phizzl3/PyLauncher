# 01.22.2021
"""
Displays a numbered menu to console and returns a corresponding function 
or object based on user number selection using a passed *expanded list/tuple.

Import it and pass it an *expanded list of tuples/lists. It will return list[1]
for your selection by default. Pass the optional listreturn= argument an integer 
to return a different list item. 
"""


def display(*args, listreturn=1):
    """
    Displays menu items [0] from list/tuple pairs/group to console, 
    gets user selection and returns corresponding function/item (defaults to 
    list item index[1] from pair/group.

    Args:
        *args (list/tuple): *Expanded list of list/tuple pairs/groups with info 
               to display to console, and item or function to return if chosen. 
               ex: ('display name', function_to_call)
        listreturn (int, optional): List index of which item to be returned.
                    defaults to 1.

    Returns:
        item/function: Item/Function [1] from corresponding selection.
                       (list/tuple index [1] by default)
    """
    # Number (enumerate) and display the options [0] from args pair starting at 1
    for i, arg in enumerate(args, 1):
        print(f' [{i}]: {arg[0]}')

    # Ask for user input and return the corresponding item/function (defaults to index[1])
    # only if the selection can be found in list.
    while True:
        sel = input('\n Selection: ')
        if sel.isdigit() and int(sel) <= len(args) and int(sel):
            return args[int(sel)-1][listreturn]
        else:
            print('\n Please choose from available selections.')
