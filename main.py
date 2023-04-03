import functions
import time

now = time.strftime("%A, %b %d, %Y %H:%M:%S")
print(f"It is {now}")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            index = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[index] = new_todo + '\n'

            functions.write_todos(todos)
        except ValueError:
            print("Invalid command. The command must contain the number of todo to edit")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = functions.get_todos()

            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo '{todo_to_remove}' was successfully completed!"
            print(message)
        except IndexError:
            print(f"Invalid command: there is no todo with this number!")
            continue
    elif user_action.startswith('exit'):
        break

    else:
        print(f"Hey, there is no command '{user_action}'! >_<")

print("Bye!")
