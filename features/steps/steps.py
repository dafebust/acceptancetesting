from behave import given, when, then

to_do_list = []


# Step definitions for existing scenarios

# Step 1: Given the to-do list is empty
@given('the to-do list is empty')
def step_to_do_list_empty(context):
    # Set the to-do list as an empty list
    global to_do_list
    to_do_list = []


# Step 2: When the user adds a task "{task}"
@when('the user adds a task "{task}"')
def step_add_task(context, task):
    global to_do_list
    to_do_list.append(task)


# Step 3: Then the to-do list should contain "{task}"
@then('the to-do list should contain "{task}"')
def step_check_task(context, task):
    assert task in to_do_list, f'Task "{task}" not found in the to-do list'


# Step 4: When the user marks task "{task}" as completed
@when('the user marks task "{task}" as completed')
def step_mark_task_completed(context, task):
    global to_do_list
    for item in to_do_list:
        if item['Task'] == task:
            item['Status'] = 'Completed'
            break


# Step 5: Then the to-do list should show task "{task}" as completed
@then('the to-do list should show task "{task}" as completed')
def step_check_task_completed(context, task):
    global to_do_list
    for item in to_do_list:
        if item['Task'] == task:
            assert item['Status'] == 'Completed', f'Task "{task}" not marked as completed'
            break


# Step 6: When the user clears the to-do list
@when('the user clears the to-do list')
def step_clear_to_do_list(context):
    global to_do_list
    to_do_list = []


# Step 7: Then the to-do list should be empty
@then('the to-do list should be empty')
def step_check_empty_to_do_list(context):
    global to_do_list
    assert not to_do_list, 'To-do list is not empty'


# Step 8: When the user attempts to mark a task "{task}" as completed
@when('the user attempts to mark a task "{task}" as completed')
def step_attempt_mark_nonexistent(context, task):
    pass


# Step 9: Then the to-do list should still be empty
@then('the to-do list should still be empty')
def step_check_still_empty(context):
    global to_do_list
    assert not to_do_list, 'To-do list is not empty'


# Step 10: Then the to-do list should remain empty
@then('the to-do list should remain empty')
def step_check_remain_empty(context):
    global to_do_list
    assert not to_do_list, 'To-do list is not empty'


# Step 11: When the user edits the task "{task}" to "{new_task}"
@when('the user edits the task "{task}" to "{new_task}"')
def step_edit_task(context, task, new_task):
    global to_do_list
    for item in to_do_list:
        if item['Task'] == task:
            item['Task'] = new_task
            break


# Step 12: Then the to-do list should contain
@then('the to-do list should contain')
def step_check_to_do_list(context):
    global to_do_list
    expected_tasks = context.table
    for expected_task in expected_tasks:
        assert expected_task['Task'] in [item['Task'] for item in to_do_list], \
            f'Task "{expected_task["Task"]}" not found in the to-do list'


# Step 13: When the user removes the task "{task}"
@when('the user removes the task "{task}"')
def step_remove_task(context, task):
    global to_do_list
    to_do_list = [item for item in to_do_list if item['Task'] != task]


# Step 14: When the user lists all tasks
@when('the user lists all tasks')
def step_list_all_tasks(context):
    pass


# Step 15: Then the output should be empty
@then('the output should be empty')
def step_check_empty_output(context):
    pass
