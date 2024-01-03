# features/steps/steps.py

from behave import given, when, then

# Definir una variable global para almacenar la lista de tareas
to_do_list = []

@given('la lista de tareas está vacía')
def step_empty_todo_list(context):
    # Limpiar la lista de tareas al inicio de cada escenario
    global to_do_list
    to_do_list = []

@when('el usuario agrega una tarea "{task}" con la descripción "{description}"')
def step_add_task(context, task, description):
    # Agregar la tarea a la lista de tareas con su descripción
    global to_do_list
    to_do_list.append({'task': task, 'description': description, 'completed': False, 'important': False})

@then('la lista de tareas debería contener la tarea "{task}" con la descripción "{description}"')
def step_check_task_in_list(context, task, description):
    # Verificar que la tarea y su descripción estén en la lista de tareas
    global to_do_list
    task_found = False
    for todo in to_do_list:
        if todo['task'] == task and todo['description'] == description:
            task_found = True
            break
    assert task_found, f'Task "{task}" with description "{description}" not found in the to-do list'

@given('la lista de tareas contiene las siguientes tareas:')
def step_populate_todo_list(context):
    # Poblar la lista de tareas desde la tabla del escenario
    global to_do_list
    to_do_list = []
    for row in context.table:
        task = row['Tarea']
        description = row['Descripción']
        status = row['Estado']
        important = row['Importante'] == 'Sí'
        to_do_list.append({'task': task, 'description': description, 'completed': status == 'Completada', 'important': important})

@when('el usuario marca la tarea "{task}" como completada')
def step_mark_task_completed(context, task):
    # Marcar la tarea como completada en la lista de tareas
    global to_do_list
    for todo in to_do_list:
        if todo['task'] == task:
            todo['completed'] = True
            break

@then('la lista de tareas debería mostrar la tarea "{task}" como completada')
def step_check_task_completed(context, task):
    # Verificar que la tarea esté marcada como completada en la lista de tareas
    global to_do_list
    task_completed = False
    for todo in to_do_list:
        if todo['task'] == task and todo['completed']:
            task_completed = True
            break
    assert task_completed, f'Task "{task}" not marked as completed in the to-do list'
