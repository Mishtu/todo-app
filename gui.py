import functions
import PySimpleGUI as psg


label = psg.Text("Type in a to-do")
input_box = psg.InputText(tooltip="Enter a to-do")
add_button = psg.Button("Add")

window = psg.Window('To-Do App', layout=[[label], [input_box, add_button]])
window.read()
window.close()