import functions
import PySimpleGUI as psg


label = psg.Text("Type in a to-do")
input_box = psg.InputText(tooltip="Enter a to-do", key="todo")
add_button = psg.Button("Add")
list_box = psg.Listbox(values=functions.get_todos(), key="todos",
                       enable_events=True, size=[45, 10])
edit_button = psg.Button("Edit")
complete_button = psg.Button("Complete")
exit_button = psg.Button("Exit")

window = psg.Window('To-Do App',
                    layout=[[label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case psg.WINDOW_CLOSED:
            break

window.close()
