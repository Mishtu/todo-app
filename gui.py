import functions
import PySimpleGUI as psg


label = psg.Text("Type in a to-do")
input_box = psg.InputText(tooltip="Enter a to-do", key="todo")
add_button = psg.Button("Add")

window = psg.Window('To-Do App',
                    layout=[[label], [input_box, add_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
        case psg.WINDOW_CLOSED:
            break

window.close()
