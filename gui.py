import functions
import PySimpleGUI as psg
import time

psg.theme("Dark")

clock = psg.Text("", key="clock")
label = psg.Text("Type in a to-do")
input_box = psg.InputText(tooltip="Enter a to-do", key="todo")
add_button = psg.Button("Add")
list_box = psg.Listbox(values=functions.get_todos(), key="todos",
                       enable_events=True, size=[45, 10])
edit_button = psg.Button("Edit")
complete_button = psg.Button("Complete")
exit_button = psg.Button("Exit")

window = psg.Window('To-Do App',
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 18))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%A, %b %d, %Y %H:%M:%S"))

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                psg.popup("Please select a todo first", font=("Helvetica", 18))
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                psg.popup("Please select a todo first", font=("Helvetica", 18))
        case 'Exit':
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case psg.WINDOW_CLOSED:
            break

window.close()
