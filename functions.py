# ====================================================
# Creating a function to get todos
# ====================================================
def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
        return todos


# ================= Function ends =====================


# ====================================================
# Creating a function to show todos
# ====================================================
def print_todos(todos_list):
    """ Read a text file and returns a list
    of to-do items.
    """
    print('\n')
    # enumerate() gives access to index of a list
    # It converts each item into a tuple ( index, value )
    for index, item in enumerate(todos_list):
        item = item.strip('\n')
        print(f"{index + 1}- {item}")
    print('\n')


# ================= Function ends =====================


# ====================================================
# Creating a function to write todos in todos.txt
# ====================================================
def write_todos(todos_local):
    """ Write the to-do items in a text file. """
    with open('todos.txt', 'w') as file_local:
        file_local.writelines(todos_local)


# ================= Function ends =====================

# ====================================================
# Creating a function to update UI
# ====================================================
def update_ui(w, todos):
    w['todos'].update(values=todos)
    w['todo'].update(value='')
# ================= Function ends =====================
