import function
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open ("todos.txt","w") as file:
        pass

#sg.theme("Reddit")
sg.theme("DarkBlue13")

clock = sg.Text("", key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=function.get_todos(),key='todos',enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

#each square bracket is a new line
#layout is list of list
window = sg.Window('My To-Do App',
                    layout=[
                        [clock],
                        [label], 
                        [input_box, add_button],
                        [list_box,edit_button],
                        [complete_button],
                        [exit_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime(r"%b %d, %Y %H:%M:%S"))
    #print(1, event)
    #print("\n" in values['todo'] )
    #print(3, values['todos'][0])
    if event == "Add":
        todos = function.get_todos()
        new_todo = values['todo']+"\n"     #get the new_todo from the user
        todos.append(new_todo)
        function.write_todos(todos)
        window['todos'].update(values=todos)
        window['todo'].update(value='')
    elif event == "Edit":
        try:
            todo_to_edit = values['todos'][0]  #get the value that is selected
            new_todo = values['todo']          #get the new_value that the user input

            todos = function.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo+"\n"

            function.write_todos(todos)

            #import step , to refresh the window
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        except IndexError:
            sg.popup("Please select an item first.", font=('Helvetica', 20))

    elif event =='todos':       #allow user to see what is selected now
        window['todo'].update(value=values['todos'][0])

    elif event == 'Complete':
        try:    
            todo_to_edit = values['todos'][0]  #get the value that is selected
            todos = function.get_todos()
            index = todos.index(todo_to_edit)
            todos.pop(index)
            function.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        except IndexError:
            sg.popup("Please select an item first.", font=('Helvetica', 20))

    elif event == 'Exit':
        break
    elif event==sg.WIN_CLOSED:
        break    #if we use exit() here , the program will stop completely

window.close()



